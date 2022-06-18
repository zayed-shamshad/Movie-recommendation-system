import { createRouter, createWebHistory } from 'vue-router'

import search from '../components/search.vue';
import home from '../components/home.vue';
import fav from '../components/fav.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/fav',
      name: 'fav',
      component: fav

    },
    {
      path: '/',
      name: 'home',
      component: home,
    }
  ]
})

export default router
