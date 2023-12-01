<template>
    <v-container fluid>
      <v-row align="center" justify="center" class="my-5">
        <v-col cols="12" sm="8" md="6" lg="4">
          <v-card class="elevation-10 pa-8" outlined>
            <v-img
              alt="Login Background"
              class="mb-4"
            ></v-img>
  
            <v-form @submit.prevent="login">
              <v-text-field
                v-model="username"
                label="Username"
                outlined
                prepend-icon="mdi-account"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                outlined
                prepend-icon="mdi-lock"
                required
              ></v-text-field>
  
              <v-row justify="center">
                <v-btn color="primary" class="mr-4 mb-3" type="submit">
                  Login
                </v-btn>
                <v-btn text @click="forgotPassword" class="mb-3">Forgot Password?</v-btn>
              </v-row>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        // Implement your login logic here
        console.log('Logging in...');
      },
      forgotPassword() {
        // Implement your forgot password logic here
        console.log('Forgot Password clicked...');
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  