<template>
    <nav>
      <v-toolbar flat app>
  
        <!-- If we want to utilize the sidebar component -->
        <!-- <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
  
        <!-- Title -->
        <v-toolbar-title class="text-uppercase grey--text mr-5">
          <span class="font-weight-light">Journey</span>
          <span>Genius</span>
        </v-toolbar-title>
  
        <!-- Buttons that link to other parts of the site -->
        <div class="d-flex align-center ml-16">
          <v-btn v-for="button in buttons" :key="button.to" flat color="grey" :to="button.to">
            {{ button.text }}
          </v-btn>
        </div>
  
        <v-spacer></v-spacer>
  
        <v-btn color="grey darken-2" flat>
          <span style="margin-right: 5px;">Login</span>
          <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-toolbar>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        buttons: [
          { text: 'Home', to: '/' },
          { text: 'User Profiling', to: '/UserProfiling' },
          { text: 'Plan Trip', to: '/StartPlanning' },
          { text: 'Saved Trips', to: '/SavedTrips' },
        ],
      };
    },
  };
  </script>
  