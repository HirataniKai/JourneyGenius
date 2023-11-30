<template>
  <div class="home">
    <v-container fluid class="no-border">
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
          <router-link to='/StartPlanning' >
          <v-btn rounded="lg" size="large" color="deep-purple-accent-2" class="white--text mt-6">
              Start Planning
            </v-btn>
          </router-link>
        </v-card>
      </v-col>
    </v-row>

    <!-- The Most Optimal way to travel -->
    <v-row align="start" justify="start" class="mt-5">
        <v-col>
          <h1 class="headline font-weight-black">
            Discover the Most Optimal Way to Travel        
          </h1>
        </v-col>
      </v-row>


    <!-- Why Our Application is Special Section -->
    <v-row align="center" justify="center" class="my-3" style="background-color: #f5f5f5;">
        <v-col cols="12" md="10" lg="8" class="text-center">
          <v-card class="pa-5">
            <h2 class="headline mb-3">
              What Makes Our Application Special
            </h2>
            <p class="body-1">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
            <p class="body-1">
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </p>
          </v-card>
        </v-col>
      </v-row>

      <v-row align="start" justify="start" class="mt-5">
        <v-col>
          <h1 class="headline font-weight-black">
            The Most Optimal way to travel
          </h1>
        </v-col>
      </v-row>

      <v-row align="center" justify="center" class="my-3 mx-0" style="background-color: #f5f5f5; border-radius: 10px;">
        <v-col cols="12" md="10" lg="8">
          <v-card class="pa-4">
            <h2 class="headline mb-3">
              The Only Tool You'll Ever Need!
            </h2>
            <p class="body-1">
              Say goodbye to the stress of planning and hello to personalized recommendations, efficient itineraries, and seamless dining experiences.
            </p>

            <!-- Features Section -->
            <v-row justify="space-between" class="mt-4">
              <v-col cols="12" md="5">
                <!-- Optimal Route Planning -->
                <v-card class="pa-3 mb-4" style="background-color: #f9f4fa; border-radius: 10px;">
                  <v-icon size="36" class="accent--text">mdi-map-marker-path</v-icon>
                  <h3 class="headline mb-2">Optimal Route Planning</h3>
                  <p class="body-1">
                    Our AI algorithms analyze your preferences to craft the most efficient route, saving you time and effort.
                  </p>
                </v-card>

                <!-- Travel Reel Insights -->
                <v-card class="pa-3 mb-4" style="background-color: #e4f4f9; border-radius: 10px;">
                  <v-icon size="36" class="accent--text">mdi-cellphone</v-icon>
                  <h3 class="headline mb-2">Travel Reel Insights</h3>
                  <p class="body-1">
                    Harness the power of social media by extracting travel insights from Instagram reels and TikToks, and incorporating them into your plans.
                  </p>
                </v-card>
              </v-col>

              <v-col cols="12" md="5">
                <!-- Personalize Your Adventure -->
                <v-card class="pa-3 mb-4" style="background-color: #f4f9e4; border-radius: 10px;">
                  <v-icon size="36" class="accent--text">mdi-pencil</v-icon>
                  <h3 class="headline mb-2">Personalize Your Adventure</h3>
                  <p class="body-1">
                    Shape your journey by freely adding, editing, or deleting activities from your itinerary.
                  </p>
                </v-card>

                <!-- Local Cuisine Recommendations -->
                <v-card class="pa-3 mb-4" style="background-color: #f9ede4; border-radius: 10px;">
                  <v-icon size="36" class="accent--text">mdi-food</v-icon>
                  <h3 class="headline mb-2">Local Cuisine Recommendations</h3>
                  <p class="body-1">
                    Discover local cuisines and hidden gems recommended by our AI, tailored to your taste buds.
                  </p>
                </v-card>
              </v-col>
            </v-row>

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




  <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12 sm4 class="my-3">
            <div class="text-xs-center">
              <h2 class="headline">The best way to share your amazing stuff</h2>
              <span class="subheading">
                No more restrictions, no more limits
              </span>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">public</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">Reach the world</div>
                    </v-card-title>
                    <v-card-text>
                      Show your stuff to the whole community of Endorfine not only to your mum or your friends. We love making good content viral. In this moment Endorfine is used by artists who are not famous but that want to share their works to the world. Unfortunately with other social networks this is hard, slow and sometime expensive.
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">Fast feedback</div>
                    </v-card-title>
                    <v-card-text>
                      Time is important, we don't want you to waste it. Here you can get a massive feedback from real users in minutes. And if your stuff is appreciated you won't only get positive feedback but also lovely and sincere fans
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">share</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">Create new connections</div>
                    </v-card-title>
                    <v-card-text>
                      Imagine if you can directly speak with the world's population. Don't you think it would be easier to find nice people to interact with? Endorfine is both local and global and help you to connect without limitations with people from your city, your state and your universe! 
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>

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

/* Add styles for the additional smaller text */
.subtitle-2 {
  font-size: 1.5rem; /* Adjust the font size as needed */
  color: #757575; /* Use a lighter color of black, adjust as needed */
}

/* Additional styles for the new grid section */
.headline {
  font-size: 3rem;
  font-weight: bold;
  color: #333; /* Adjust the color as needed */
}

.body-1 {
  font-size: 1rem;
  color: #555; /* Adjust the color as needed */
}

</style>
