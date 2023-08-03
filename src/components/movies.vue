<template>

<div class="w-screen min-h-screen">
    
    <div v-if="load" class="flex flex-col justify-center items-center w-screen h-screen">
         <pulse-loader :loading="load" :color="'red'" :size="'50px'" :margin="'2px'" :speed="'1s'" :trail="'10'"
                  :shadow="'0'" :shadowColor="'#fff'" :shadowSize="'0'" :radius="'10px'"></pulse-loader>
    </div>
    <div v-else>
        <div class="title-trending text-xl md:text-4xl">
           Trending
        </div>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 overflow-scroll px-2">
        <transition-group name="fade" mode="out-in">
            <movie-card
                    v-for="movie in data.results"
                    :key="movie.id"
                    :id="movie.id"
                    :title="movie.title"
                    :overview="movie.overview"
                    :links="link+movie.poster_path">
            </movie-card>
        </transition-group>
    </div>
    </div>
</div>
    
</template>
<script setup>
import movieCard from './movie-card.vue'
import { ref } from 'vue'
import axios from 'axios'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

const load=ref(true)
const link = "https://image.tmdb.org/t/p/w500";
const data = ref(null);

const getMovies_flask = async () => {
    const response = await axios.get('https://movie-system-api.onrender.com/trending')
    data.value = response.data;
    load.value=false;
}
getMovies_flask()

</script>
<style>
.list-enter-active,
.list-leave-active {
    transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
    opacity: 0;
    transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
    position: absolute;
}
.title-trending{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 10vh;
    width: 100vw;
    background-color: rgba(0,0,0,0.5);
    color: white;
    font-size: 2rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5rem;
    z-index: -1;
  
}

</style>