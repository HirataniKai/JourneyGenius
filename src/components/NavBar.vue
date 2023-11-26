<template>
    <nav>
        <v-toolbar flat app>

            <!-- If we want to utilize the sidebar component -->
            <!-- <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->


            <!-- Title -->

            <v-toolbar-title class="text-uppercase grey--text">
                <span class="font-weight-light">Journey</span>
                <span>Genius</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>
            <!-- Buttons that link to other parts of the site -->
            <v-btn flat color="grey" to="/">
                Home
            </v-btn>
            <v-btn flat color="grey" to="/startPlanning">
                User Profiling
            </v-btn>
            <v-btn flat color="grey" to="/startPlanning">
                Start Planning
            </v-btn>
            <v-btn flat color="grey" to="/about">
                Your Trips
            </v-btn>
            <v-btn flat color="grey">
                <span style="margin-right: 8px;">Sign Out</span>
                <v-icon right>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-toolbar>

        <!-- This is the sidebar component -->
        <!-- <v-navigation-drawer
        v-model="drawer"
        location="left"
        temporary
      >
        <v-list
          :items="items"
        ></v-list>
      </v-navigation-drawer>

      <v-main style="height: 500px;">
    </v-main> -->


    </nav>
</template>

<script>
export default {
    // Sidebar component
    // data: () => ({
    //   drawer: false,
    //   group: null,
    //   items: [
    //     {
    //       title: 'Foo',
    //       value: 'foo',
    //     },
    //     {
    //       title: 'Bar',
    //       value: 'bar',
    //     },
    //     {
    //       title: 'Fizz',
    //       value: 'fizz',
    //     },
    //     {
    //       title: 'Buzz',
    //       value: 'buzz',
    //     },
    //   ],
    // }),

    // watch: {
    //   group () {
    //     this.drawer = false
    //   },
    // },
}
</script>
