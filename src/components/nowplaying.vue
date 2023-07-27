<template>
    <div class="w-screen min-h-screen">

        <div v-if="data == null" class="flex flex-col justify-center items-center w-screen  h-screen">
            <pulse-loader :loading="load" :color="'red'" :size="'50px'" :margin="'2px'" :speed="'1s'" :trail="'10'"
                :shadow="'0'" :shadowColor="'#fff'" :shadowSize="'0'" :radius="'10px'"></pulse-loader>
        </div>
        <div v-else>
            <div class="title-trending text-xl md:text-4xl">
                Now Playing
            </div>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 overflow-scroll px-2">

                <movie-card v-for="movie in data.results" :key="movie.id" :id="movie.id" :title="movie.title"
                    :overview="movie.overview" :links="link + movie.poster_path">
                </movie-card>
            </div>
        </div>
    </div>
</template>
<script setup>
import movieCard from './movie-card.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'



const router = useRouter();
const path = router.currentRoute.value.name;
const link = "https://image.tmdb.org/t/p/w500";
const data = ref(null);
const options = {
    method: 'GET',
    headers: {
        accept: 'application/json',
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDYzMzQ1MzIxMTQwNDhmN2VlYTA3OGVkMTBlM2EwOSIsInN1YiI6IjYyNmFmOGFlOWI2ZTQ3MDBhNDVhODAyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MIBeEiA5qadK-dRQi1FYcNiZ037hIT-vnZ_hMiCKfm8'
    }
};


const getMovies = async () => {
    const response = await axios.get('https://api.themoviedb.org/3/movie/now_playing', options)
    data.value = response.data
}
getMovies()



</script>
<style>
.title-trending {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 10vh;
    width: 100vw;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    font-size: 2rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5rem;
    z-index: -1;

}
</style>