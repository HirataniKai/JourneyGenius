<template>
  <div class="home">
    <v-container fluid>
    <!-- Top Section -->
    <v-row align="center" justify="center" class="my-3">
      <v-col cols="12" md="10" lg="8" class="text-center">
        <v-card class="pa-5">
          <h2 class="display-1 font-weight-black">
            Generate Timeless 
          </h2>
          <h2 class="display-1 font-weight-black">
            Vacation Itineraries with
          </h2>
          <h2 class="display-1 font-weight-black mb-2">
            <span class="text-deep-purple-accent-2">Journey Genius</span>
          </h2>
          <!-- Additional smaller text -->
          <h3 class="subtitle-1 text-grey-darken-2">
            This application serves as your dedicated travel curator, crafting distinctive itineraries 
          </h3>
          <h3 class="subtitle-1 text-grey-darken-2">
            tailored to your interests and budget. 
          </h3>

          <!-- "Start Now" -->
          <v-btn rounded="lg" size="large" color="deep-purple-accent-2" class="white--text mt-6">
              Start Now
            </v-btn>
        </v-card>
      </v-col>
    </v-row>



    <!-- Two Boxes Section -->
    <v-row>
      <v-col cols="12">
        <v-row>
          <!-- Box 1 -->
          <v-col cols="12" md="6">
            <v-card class="pa-5">
              <h3 class="headline">Box 1</h3>
              <p>Box 1 content goes here.</p>
            </v-card>
          </v-col>

          <!-- Box 2 -->
          <v-col cols="12" md="6">
            <v-card class="pa-5">
              <h3 class="headline">Box 2</h3>
              <p>Box 2 content goes here.</p>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>

  </div>
</template>

<script>
import { defineComponent } from 'vue';


export default defineComponent({
  
});
</script>

<style scoped>

/* Adjust the font size to make it larger */
.display-1 {
  font-size: 4rem; /* You can adjust this value as needed */
}
</style>
