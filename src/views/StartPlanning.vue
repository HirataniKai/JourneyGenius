<template>
  <v-container>
    <!-- Header -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Plan Your Next Adventure</h2>
        <p>Our app transforms vacation planning by creating personalized itineraries based on user preferences. Users
          input their budget, location, stay duration, and interests. Using advanced algorithms, the app scans diverse
          travel data to find budget-friendly accommodations, local attractions, and outdoor activities, optimizing the
          itinerary for a cost-effective trip.</p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Section for storing where they want to travel -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h3 class="headline text-deep-purple-accent-2">Where do you want to travel?</h3>
          <br>
          <v-text-field v-model="travelDestination" label="United States"></v-text-field>
        </v-card>
      </v-col>
    </v-row>

   <!-- Date input components -->
<v-row justify="center">
  <v-col cols="12" md="8">
    <v-card class="pa-4 mb-4">
      <h3 class="headline text-deep-purple-accent-2">How Long Is Your Trip?</h3>
      <br>
      <v-row>
        <!-- Start Date -->
        <v-col cols="6">
          <v-menu max-width="290">
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="startDate"
                label="Start Date"
                prepend-icon="mdi-calendar-range"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="startDate"></v-date-picker>
          </v-menu>
        </v-col>

        <!-- End Date -->
        <v-col cols="6">
          <v-menu max-width="290">
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="endDate"
                label="End Date"
                prepend-icon="mdi-calendar-range"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="endDate"></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
    </v-card>
  </v-col>
</v-row>


    <!-- Budget selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">How Much Have You Allocated for Your Expenses?</h3>
          <p>The budget is specifically designated for activities and dining experiences.</p>
          <br>
          <v-row justify="center">
            <v-col v-for="budget in budgets" :key="budget.value" class="mb-2">
              <v-btn class="budget-btn" stacked="" :color="budget.selected ? 'deep-purple' : 'deep-purple-accent-2'"
                @click="selectBudget(budget)">
                <v-icon v-if="budget.value === 'cheap'">mdi-cash-remove</v-icon>
                <v-icon v-if="budget.value === 'medium'">mdi-cash</v-icon>
                <v-icon v-if="budget.value === 'expensive'">mdi-cash-multiple</v-icon>
                <div>{{ budget.label }}</div>
                <div class="caption text--secondary">{{ budget.range }}</div>
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Travel Companions selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Who Are Your Travel Companions?</h3>
          <v-row justify="center">
            <v-col v-for="companion in travelCompanions" :key="companion.value" cols="4">
              <v-btn class="companion-btn" :color="companion.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="selectTravelCompanion(companion)">
                <v-icon v-if="companion.value === 'solo'">mdi-account</v-icon>
                <v-icon v-if="companion.value === 'group'">mdi-account-group-outline</v-icon>
                <v-icon v-if="companion.value === 'couple'">mdi-heart</v-icon>
                <div>{{ companion.label }}</div>
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Generate button -->
    <v-row justify="center">
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
      budgets: [
        { label: 'Cheap', value: 'cheap', range: '0 - 1000 USD', selected: false },
        { label: 'Medium', value: 'medium', range: '1000 - 2500 USD', selected: false },
        { label: 'Expensive', value: 'expensive', range: '2500+ USD', selected: false },
      ],
      travelCompanions: [
        { label: 'Solo', value: 'solo', selected: false },
        { label: 'Group', value: 'group', selected: false },
        { label: 'Couple', value: 'couple', selected: false },
      ],
      selectedDate: null,
      isDatePickerVisible: false,
      travelDestination: null,
      selectedBudget: null,
    };

  },
  methods: {
    showDatePicker() {
      this.isDatePickerVisible = true;
    },
    hideDatePicker() {
      this.isDatePickerVisible = false;
    },
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
    selectBudget(selectedBudget) {
      this.budgets.forEach((budget) => {
        budget.selected = budget === selectedBudget;
      });
    },
    selectTravelCompanion(selectedCompanion) {
      this.travelCompanions.forEach((companion) => {
        companion.selected = companion === selectedCompanion;
      });
    }
    
  },
});
</script>

<style>
.companion-btn {
  width: 100%;
  margin-top: 8px;
}

.budget-btn {
  width: 100%;
  margin-top: 8px;
}
</style>




<!-- <v-row> -->
          <!-- <v-col cols="6">
              <v-text-field v-model="startDate" label="Start Date" readonly @click="startDateMenu = !startDateMenu"></v-text-field>
              <v-menu v-model="startDateMenu" :close-on-content-click="false" transition="scale-transition" offset-y>
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="startDate" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="startDate" @input="startDateMenu = false"></v-date-picker>
              </v-menu>
            </v-col> -->

          <!-- <v-col cols="6">
              <v-text-field v-model="endDate" label="End Date" readonly
                @click="endDateMenu = !endDateMenu"></v-text-field>
              <v-menu v-model="endDateMenu" :close-on-content-click="false" transition="scale-transition">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="endDate" readonly v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="endDate" @input="endDateMenu = false"></v-date-picker>
              </v-menu>
            </v-col>
          </v-row> -->