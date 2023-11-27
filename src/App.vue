<template>
  <v-app>
    <NavBar/>
    <v-content class="mx-15 mb-15 mt-5">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: 'App',
  components: { NavBar },
  data: () => ({
    
  }),
}
</script> 
 