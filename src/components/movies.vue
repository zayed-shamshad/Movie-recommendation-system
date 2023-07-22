<template>

<div class="movie-grid">
    <div class="title-trending">
        <h1>Trending Movies</h1>
    </div>
    <div v-if="data==null">
        fetching....
    </div>

    <movie-card v-else
            :style="{
                zIndex: '0',
            }"
            v-for="movie in data.results"
            :key="movie.id"
            :id="movie.id"
            :title="movie.title"
            :overview="movie.overview"
            :links=link + {{movie.poster_path}}
    >
</movie-card>
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
.movie-grid{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
    width:100vw;
    background-color:rgba(0,0,0,0.5);
    margin-top: 10vh;
    overflow-y: scroll;
    z-index: -2;
    height: 85vh;
}
</style>