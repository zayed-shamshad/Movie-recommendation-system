import { createRouter, createWebHistory } from 'vue-router'
import search from '../components/search.vue';
import home from '../components/home.vue';
import fav from '../components/fav.vue';
import movies from '../components/movies.vue';
import moviePage from '../components/moviePage.vue';
import upcoming from '../components/upcoming.vue';
import nowplaying from '../components/nowplaying.vue';
import toprated from '../components/toprated.vue';
import { useUserStore } from '../stores/store';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/movies',
      name: 'movies',
      component: moviePage,
      redirect: '/movies/trending',
      children: [
        {
          path: '/movies/trending',
          name: 'trending',
          component: movies,
        },
        {
          path: '/movies/upcoming',
          name: 'upcoming',
          component: upcoming,
        },
        {
          path: '/movies/nowplaying',
          name: 'nowplaying',
          component: nowplaying,
        },
        {
          path: '/movies/toprated',
          name: 'toprated',
          component: toprated,
        },
      ]
    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/favourites',
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
