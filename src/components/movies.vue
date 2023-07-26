<template>

<div class="w-screen px-2">
    
    <div v-if="data==null">
        fetching....
    </div>
    <div v-else >
        <div class="title-trending text-xl md:text-4xl">
           Trending Movies
        </div>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 overflow-scroll">

    <movie-card
            v-for="movie in data.results"
            :key="movie.id"
            :id="movie.id"
            :title="movie.title"
            :overview="movie.overview"
            :links="link+movie.poster_path">
     </movie-card>
    </div>
    </div>
</div>
    
</template>
<script setup>
import movieCard from './movie-card.vue'
import { ref } from 'vue'
import axios from 'axios'

const link="https://image.tmdb.org/t/p/w500";
const data = ref(null);
const options = {
    method: 'GET',
    headers: {
        accept: 'application/json',
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDYzMzQ1MzIxMTQwNDhmN2VlYTA3OGVkMTBlM2EwOSIsInN1YiI6IjYyNmFmOGFlOWI2ZTQ3MDBhNDVhODAyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MIBeEiA5qadK-dRQi1FYcNiZ037hIT-vnZ_hMiCKfm8'
    }
};
const getMovies=async()=>{
    const response=await axios.get('https://api.themoviedb.org/3/trending/movie/day', options)
     data.value=response.data
}
getMovies();
</script>
<style>

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