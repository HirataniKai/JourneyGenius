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
      console.log('Registering...');
    },
    login() {
      // Implement your login logic here
      console.log('Logging in...');
    }
  }
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
