<template>
    <div class="w-screen h-screen flex justify-center items-center flex-col">
        <div class="text-4xl w-screen h-full flex flex-col justify-between items-center text-white  bg-gray-900   bg-opacity-50 ">
            <div class="h-1/6 w-screen flex flex-col justify-center items-center">
                 <button
            class="text-white bg-red-500 rounded-lg p-4"
             @click="() => {
                 $router.push('/search');
             }">
                Get started
            </button>
        </div>
         <div class="w-4/5 h-5/6 flex justify-center items-center">
                <Carousel :settings="settings" :breakpoints="breakpoints" :wrap-around="true" :autoplay="1000" >
                    <Slide v-for="item in data" :key="item.id">
                        <div class="w-full h-full flex justify-center items-center">
                            <img :src="link+item.poster_path" alt="movie poster" class="w-full h-full object-cover">

                        </div>
                    </Slide>
                </Carousel>
        </div>
    </div>
        
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide,Pagination, Navigation } from 'vue3-carousel'
import axios from 'axios'
import movieCard from './movie-card.vue'

const link="https://image.tmdb.org/t/p/w500"
const data=ref(null)
const options = {
    method: 'GET',
    headers: {
        accept: 'application/json',
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDYzMzQ1MzIxMTQwNDhmN2VlYTA3OGVkMTBlM2EwOSIsInN1YiI6IjYyNmFmOGFlOWI2ZTQ3MDBhNDVhODAyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MIBeEiA5qadK-dRQi1FYcNiZ037hIT-vnZ_hMiCKfm8'
    }
};

const settings={
     itemsToShow: 1,
    snapAlign: 'center',
}
const breakpoints={
        // 700px and up
        700: {
            itemsToShow: 3.5,
            snapAlign: 'center',
        },
        // 1024 and up
        1024: {
            itemsToShow: 5,
            snapAlign: 'start',
        },
}
onMounted(async()=>{
    const res=await axios.get("https://api.themoviedb.org/3/trending/movie/day",options)
    data.value=res.data.results
    console.log(data.value)
})
</script>
<style>

</style>