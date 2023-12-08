<template>
    <v-container>
        <!-- Title and Information Section -->
        <v-row>
            <v-col cols="12" md="6">
                <div style="margin-top: 50px;">
                    <h1 class="headline" style="font-size: 2em;">Welcome to San Francisco!</h1>
                    <h2 class="subtitle">Explore the City by the Bay</h2>
                    <p>
                        San Francisco is a vibrant city known for its iconic landmarks,
                        diverse neighborhoods, and rich history. Whether you're interested
                        in exploring the Golden Gate Bridge, visiting Fisherman's Wharf,
                        or enjoying the cultural scene in the Mission District, San
                        Francisco has something for everyone.
                    </p>
                    <br>
                    <hr>
                </div>

                <!-- New Section: Activities, Landmarks, Places to Eat, Shopping Spots -->
                <div style="margin-bottom: 30;">
                    <br>
                    <h2 class="section-title">Discover San Francisco - Overview</h2>

                    <!-- Activities Section -->
                    <div class="section-content">
                        <h3>Activities</h3>
                        <ul>
                            <li>Explore Golden Gate Park</li>
                            <li>Take a cruise on the Bay</li>
                            <li>Attend a Giants baseball game at Oracle Park</li>
                        </ul>
                    </div>

                    <!-- Landmarks Section -->
                    <div class="section-content">
                        <h3>Iconic Landmarks</h3>
                        <ul>
                            <li>Golden Gate Bridge</li>
                            <li>Alcatraz Island</li>
                            <li>Painted Ladies in Alamo Square</li>
                        </ul>
                    </div>

                    <!-- Places to Eat Section -->
                    <div class="section-content">
                        <h3>Places to Eat</h3>
                        <ul>
                            <li>Taste clam chowder at Boudin Bakery</li>
                            <li>Try dim sum in Chinatown</li>
                            <li>Dine with a view at Waterbar</li>
                        </ul>
                    </div>


                </div>
            </v-col>

            <!-- Image Section -->
            <v-col cols="12" md="6" class="image-container" style="margin-top: 38px;">
                <v-img src="@/assets/SFBridge.jpeg" alt="San Francisco" class="fill-height"></v-img>
            </v-col>

            <!-- New Section: Map of San Francisco -->
            <div class="" style="margin-bottom: 30px;">
                <hr>
                <br>
                <h2 class="section-title" style="text-align: center;">Explore San Francisco - Map</h2>
                <p>
                    Explore this interactive map showcasing the locations of your selected points of interest,
                    encompassing your chosen accommodation, transportation options, planned activities, and
                    other areas of interest!
                </p>
                <br>
                <div style="position: relative; overflow: hidden; border-radius: 8px;">
                    <!-- Replace YOUR_GOOGLE_MAPS_EMBED_CODE with the actual embed code from Google Maps -->
                    <iframe width="100%" height="300" frameborder="0" style="border: 0; border-radius: 8px;"
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d100940.18159925131!2d-122.52000105328746!3d37.757671315006284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1701922231766!5m2!1sen!2sus"
                        allowfullscreen></iframe>
                </div>
            </div>

            <!-- New Section: Estimated Costs -->
            <div class="" style="margin-bottom: 30px; max-width: none;">
                <h2 class="section-title">Estimated Costs (USD)</h2>
                <div class="section-content">
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-icon color="deep-purple-accent-2">mdi-bed</v-icon> Accommodation: $100-$200 per night
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-icon color="deep-purple-accent-2">mdi-bus</v-icon> Transportation: $20-$50 per day
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-icon color="deep-purple-accent-2">mdi-food</v-icon> Food: $20-$40 per meal
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-icon color="deep-purple-accent-2">mdi-walk</v-icon> Activities: $20-$50 per activity
                        </v-col>
                    </v-row>
                </div>
            </div>



            <!-- Two buttons on the bottom -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8" class="text-center">
                    <router-link to="/Itinerary">
                        <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                            style="min-width: 150px;">
                            Customize
                        </v-btn>
                    </router-link>

                    <router-link to="/GeneratedItinerary2">
                        <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                            Generate
                        </v-btn>
                    </router-link>
                </v-col>
            </v-row>

        </v-row>

    </v-container>
</template>
  
<script>
export default {
    name: 'SanFranciscoPage',
};
</script>
  
<style scoped>
/* Custom styles for the information and new sections */
.info-container {
    padding: 16px;
    background-color: #fff;
    /* You can customize the background color */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    /* Optional: Add a subtle box shadow */
    margin-bottom: 16px;
}

.image-container {
    display: flex;
    align-items: flex-start;
}

.section-title {
    font-size: 1.8em;
    margin-bottom: 16px;
}

.section-content {
    margin-bottom: 24px;
}

.section-content h3 {
    font-size: 1.5em;
    margin-bottom: 8px;
}

.section-content ul {
    list-style-type: disc;
    /* Change 'disc' to 'circle' or 'square' if desired */
    padding-left: 20px;
    /* Adjust as needed */
}

.section-content ul li {
    margin-bottom: 4px;
}





/* Custom styles for the Estimated Costs section */
.estimated-costs {
    margin-top: 30px;
    /* Adjust as needed */
}

.estimated-costs h2 {
    font-size: 1.8em;
    margin-bottom: 16px;
}

.estimated-costs .section-content {
    margin-bottom: 16px;
}

.estimated-costs .section-content h3 {
    font-size: 1.5em;
    margin-bottom: 8px;
}
</style>
  