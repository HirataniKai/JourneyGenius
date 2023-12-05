<template>
  <v-container>
    <!-- Saved Trips Introduction -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Saved Trips</h2>
        <p>
          Explore and manage your saved adventures effortlessly on our "Saved Trips" page. Easily access
          and review your curated itineraries, and if inspiration strikes or plans change, customize them
          to suit your preferences. This hub is your go-to destination for comprehensive details about
          your planned journeys, allowing you to delve into more information and make adjustments seamlessly.
          Your personalized travel experiences are just a click away on the Saved Trips page.
        </p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Saved Trip Card -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <!-- Title and Delete Button Section -->
          <v-row align="center">
            <v-col cols="8">
              <h2 class="headline">San Francisco, California</h2>
            </v-col>
            <v-col cols="4" class="text-right">
              <v-btn icon>
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </v-col>
          </v-row>

          <!-- Main Content Section -->
          <v-row>
            <!-- Description and Activities Section -->
            <v-col cols="12" md="6">
              <p>
                San Francisco is a vibrant city known for its iconic landmarks, diverse culture, and stunning views.
                Explore the Golden Gate Bridge, visit Alcatraz Island, and stroll through Fisherman's Wharf for a
                taste of the city's rich history and delicious seafood.
              </p>
              <br>
              <h3 class="subtitle-1">Activities:</h3>
              <ul>
                <li>Golden Gate Bridge Sightseeing</li>
                <li>Alcatraz Island Tour</li>
                <li>Fisherman's Wharf Exploration</li>
                <!-- Add more activities as needed -->
              </ul>
            </v-col>

             <!-- Image and Open Itinerary Button Section -->
      <v-col cols="12" md="6">
        <v-row align="center" justify="center">
          <v-img
            src="@/assets/sf.jpeg"
            alt="San Francisco"
            class="mb-3"
            style="width: 100%; border-radius: 8px;"
          ></v-img>
          <v-btn color="primary" class="mt-3" @click="openItinerary">
            Open Itinerary
          </v-btn>
        </v-row>
      </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    openItinerary() {
      // Implement logic to open the itinerary for this saved trip
      console.log('Opening Itinerary...');
    },
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
