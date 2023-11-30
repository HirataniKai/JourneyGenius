<template>
  <v-container>
    <!-- Header -->
    <v-row justify="center">
      <v-col cols="12" md="8" class="mb-4">
        <v-card class="pa-4" style="border: none; background-color: transparent;">
          <h2 style="font-size: 2.5rem; color: black;">Plan Your Next Adventure</h2>
          <p>Our app transforms vacation planning by creating personalized itineraries based on user preferences. Users
            input their budget, location, stay duration, and interests. Using advanced algorithms, the app scans diverse
            travel data to find budget-friendly accommodations, local attractions, and outdoor activities, optimizing the
            itinerary for a cost-effective trip.</p>
        </v-card>
      </v-col>
    </v-row>

    <!-- Section for storing where they want to travel -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h2>Where do you want to travel?</h2>
          <br>
          <v-text-field v-model="travelDestination" label="United States"></v-text-field>
        </v-card>
      </v-col>
    </v-row>

    <!-- Date input components -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h2 class="headline text-deep-purple-accent-2">How Long Is Your Trip?</h2>
          <br>
          <v-row>
            <v-col cols="6">
              <v-text-field v-model="startDate" label="Start Date" readonly
                @click="startDateMenu = !startDateMenu"></v-text-field>
              <v-menu v-model="startDateMenu" :close-on-content-click="false" transition="scale-transition">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="startDate" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="startDate" @input="startDateMenu = false"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="6">
              <v-text-field v-model="endDate" label="End Date" readonly
                @click="endDateMenu = !endDateMenu"></v-text-field>
              <v-menu v-model="endDateMenu" :close-on-content-click="false" transition="scale-transition">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="endDate" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="endDate" @input="endDateMenu = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <!-- Budget selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h2 class="headline text-deep-purple-accent-2">How Much Have You Allocated for Your Expenses?</h2>
          <p>The budget is specifically designated for activities and dining experiences.</p>
          <br>
          <v-row justify="center">
            <v-col cols="4">
              <v-btn color="deep-purple-accent-2" append-icon="$vuetify" stacked @click="selectBudget('cheap')">
                <div>Cheap</div>
                <div class="caption text--secondary">0 - 1000 USD</div>
              </v-btn>
            </v-col>
            <v-col cols="4">
              <v-btn color="deep-purple-accent-2" append-icon="$vuetify" stacked @click="selectBudget('medium')">
                <div>Medium</div>
                <div class="caption text--secondary">1000 - 2500 USD</div>
              </v-btn>
            </v-col>
            <v-col cols="4">
              <v-btn color="deep-purple-accent-2" append-icon="$vuetify" stacked @click="selectBudget('expensive')">
                <div>Expensive</div>
                <div class="caption text--secondary">2500+ USD</div>
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <!-- Travel Companions selection -->
<v-row justify="center">
  <v-col cols="12" md="8">
    <v-card class="pa-4 mb-4">
      <h2 class="headline text-deep-purple-accent-2">Who Are Your Travel Companions?</h2>
      <v-row justify="center" align="center">
        <v-col cols="4">
          <v-btn color="deep-purple-accent-2" max-width="200" @click="selectTravelCompanion('solo')">
            <div>Solo</div>
          </v-btn>
        </v-col>
        <v-col cols="4">
          <v-btn color="deep-purple-accent-2" max-width="200" @click="selectTravelCompanion('group')">
            <div>Group</div>
          </v-btn>
        </v-col>
        <v-col cols="4">
          <v-btn color="deep-purple-accent-2" max-width="200" @click="selectTravelCompanion('couple')">
            <div>Couple</div>
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-col>
</v-row>

  <!-- Generate button -->
  <v-row justify="center" >
      <v-col cols="12" md="8" class="text-center">
        <br>
        <v-btn class="generate-btn" color="deep-purple-accent-2" @click="generateItinerary">
          Generate
        </v-btn>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      startDateMenu: false,
      endDateMenu: false,
      startDate: null,
      endDate: null,
      travelDestination: null,
      selectedBudget: null,
    };
  },
  methods: {
    selectBudget(budget) {
      this.selectedBudget = budget;
    },
    selectTravelCompanion(companion) {
      this.companion = companion;
    },
    generateItinerary() {
      // Add logic for generating the itinerary or route to another view page
      // For example, you can use Vue Router to navigate to a new page
      this.$router.push('/Itinerary'); 
    },
  },
});
</script>

