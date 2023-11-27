import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import about from '../views/About.vue'
import UserProfiling from '../views/UserProfiling.vue'
import SavedTrips from '../views/SavedTrips.vue'
import StartPlanning from '../views/StartPlanning.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/UserProfiling',
    name: 'UserProfiling',
    component: UserProfiling,
  },
  {
    path: '/StartPlanning',
    name: 'StartPlanning',
    component: StartPlanning,
  },
  {
    path: '/SavedTrips',
    name: 'SavedTrips',
    component: SavedTrips,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
