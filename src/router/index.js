import { createRouter, createWebHistory } from 'vue-router'
import search from '../components/search.vue';
import home from '../components/home.vue';
import fav from '../components/fav.vue';
import movies from '../components/movies.vue';
import about from '../components/about.vue';
import { useUserStore } from '../stores/store';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/movies',
      name: 'Movies',
      component: movies

    },
    {
      path: '/about',
      name: 'about',
      component: about

    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/fav',
      name: 'fav',
      component: fav,
      beforeEnter: (to, from, next) => {
        const store=useUserStore();
        const user = store.getUser;
          if (user) {
            next();
          }
          else {
            next('/');
          }
        }
    },
    {
      path: '/',
      name: 'home',
      component: home,
    },
    { path: '/:pathMatch(.*)*', name: 'not-found', component: home },
  ]
})

export default router
