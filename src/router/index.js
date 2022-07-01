import { createRouter, createWebHistory } from 'vue-router'
import { getAuth } from 'firebase/auth';
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
      component: fav,
      beforeEnter: (to, from, next) => {
        getAuth().onAuthStateChanged(user => {
          if (user) {
            next();
          }
          else {
            next('/');
          }
        }
        );
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
