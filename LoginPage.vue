<template>
  <v-app>
    <v-content>
      <v-card width="500" class="mx-auto mt-9">
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-text-field v-model="username" label="Username" prepend-icon="mdi-account-circle"/>
          <v-text-field 
            v-model="password"
            label="Password" 
            :type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"/>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="deep-purple-accent-2" @click="register">Register</v-btn>
          <v-btn color="deep-purple-accent-2" @click="login">Login</v-btn>
        </v-card-actions>
      </v-card>
      <br>
    </v-content>

    <v-footer dark padless>
      <v-card class="flex" flat tile>
        <v-card-title class="teal">
          <v-spacer></v-spacer>
          <v-btn v-for="icon in icons" :key="icon" class="mx-4" dark icon>
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-title>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
// Import Axios at the top of your script
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    return {
      showPassword: false,
      username: '',
      password: ''
    };
  },
  methods: {
    register() {
      // Implement your registration logic here
      // Make an AJAX request to Flask application
      const url = 'http://localhost:8000/api/RegisterUser'; //The localhost port I have Flask running on

      // Check if both username and password are provided
      if (!this.username || !this.password) {
        this.message = 'Username and password are required.';
        console.error('Username and password are required.');
        return;
      }

      // Use Axios library for AJAX requests
      // Make sure to install Axios using npm or yarn before using it
      // Send the username and password to the Flask API
      axios.post(url, { username: this.username, password: this.password })
        .then(response => {
          console.log('User registered successfully!', response);
          this.message = 'User registered successfully.';
          this.login();
        })
        .catch(error => {
          console.error('Error registering user', error);
          if (error.response) {
            if (error.response.status === 400) {
              console.error('Registration failed: Username already exists.');
              this.message = 'Registration failed: Username already exists.';
            } else {
              console.error('Registration failed: Server error.');
              this.message = 'Error registering.';
            }
          } else {
            this.message = 'Network error or server unreachable.';
          }
        });
      console.log('Registering...');
    },
    login() {
      // Implement your login logic here
      // Make an AJAX request to Flask application
      const url = 'http://localhost:8000/api/LoginUser'; //The localhost port I have Flask running on

      // Check if both username and password are provided
      if (!this.username || !this.password) {
        this.message = 'Username and password are required.';
        console.error('Username and password are required.');
        return;
      }

      axios.post(url, { username: this.username, password: this.password }, { withCredentials: true })

        .then(response => {
          console.log('User logged in successfully!', response);

          // Store the user token or session ID in a secure HTTP-only cookie
          Cookies.set('login_token', response.data.token, { httpOnly: true });
          
          this.message = 'User logged in successfully.';

          this.checkLoginStatus(); //Not sure where to put this yet
        })
        .catch(error => {
          console.error('Error logging in', error);
          // Handle different status codes and display appropriate messages
          if (error.response) {
            if (error.response.status === 401) {
              console.error('Login failed: Incorrect username or password.');
              this.message = 'Incorrect username or password.';
            } else {
              console.error('Login failed: Server error.');
              this.message = 'Error logging in.';
            }
          } else {
            this.message = 'Network error or server unreachable.';
          }
        });

      console.log('Logging in...');
    },
    logout() {
      const url = 'http://localhost:8000/api/LogoutUser'; // Update with your Flask app's URL

      // Remove the user token or session ID from the cookie
      Cookies.remove('login_token', { httpOnly: true });

      // Send a request to the Flask API to handle logout
      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.message = 'Logout successful.';
        })
        .catch(error => {
          console.error('Error logging out', error);
          this.message = 'Error logging out.';
        });
    },
    checkLoginStatus() {
      const url = 'http://localhost:8000/api/check_login_status'; // Update with your Flask app's URL

      // Send a request to the Flask API to check the login status
      axios.get(url, { withCredentials: true })
        .then(response => {
          console.log('Login status:', response.data.message);
          this.message = response.data.message;
        })
        .catch(error => {
          console.error('Error checking login status', error);
          this.message = 'Error checking login status.';
        });
    },
  }
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
