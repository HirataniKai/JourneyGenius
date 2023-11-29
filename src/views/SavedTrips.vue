<template>
  <div class="home">
    <h1 class="subtitle-1 grey--text">Saved Trips</h1>
    <p>Two claps I rock</p>

    <v-container class="my-5">
      <v-layout row wrap>
        <v-col xs="12" md="6">
          <v-btn outlined block class="primary">1</v-btn>
        </v-col>
        <v-col xs="12" md="6">
          <v-btn outlined block class="primary">2</v-btn>
        </v-col>
      </v-layout>

      <v-layout row wrap>
        <v-col xs="12" md="6">
          <v-btn outlined block class="primary">1</v-btn>
        </v-col>
        <v-col xs="4" md="2">
          <v-btn outlined block class="primary">2</v-btn>
        </v-col>
        <v-col xs="4" md="2">
          <v-btn outlined block class="primary">3</v-btn>
        </v-col>
        <v-col xs="4" md="2">
          <v-btn outlined block class="primary">4</v-btn>
        </v-col>
      </v-layout>

      <v-layout row wrap>
        <v-flex xs="4" md="3">
          <v-btn outlined block class="success">yay</v-btn>
        </v-flex>
      </v-layout>



    </v-container>


  </div>
</template>
  
<script>
import { defineComponent } from 'vue';


export default defineComponent({

});
</script>
  