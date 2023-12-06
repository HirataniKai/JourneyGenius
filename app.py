from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)])

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)])

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)])

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)])

    submit = SubmitField('Login')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return jsonify({"message": "Welcome to the dashboard", "user": current_user.username}), 200


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200


@ app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    form = RegisterForm(data={'username': username, 'password': password})

    if form.validate():
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Registration successful"}), 201

    return jsonify({"message": "Invalid registration data"}), 400


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
