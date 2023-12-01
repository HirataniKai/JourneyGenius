import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import 'vuetify/dist/vuetify.min.css';
//import 'materialize-css/dist/css/materialize.min.css';


loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
