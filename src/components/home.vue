<template>
    <div class="w-screen h-screen flex justify-center items-center flex-col">
        <div class="text-2xl w-screen h-full flex flex-col justify-between items-center text-white  bg-gray-900   bg-opacity-50 ">
            <div class="h-1/6 w-screen flex flex-col justify-center items-center">
                 <button
            class="rounded-lg p-4
            btn relative inline-flex items-center justify-start overflow-hidden transition-all bg-red-500 text-white rounded hover:bg-white group
            "
             @click="() => {
                 $router.push('/search');
             }">
      <span className="w-0 h-0 rounded bg-white absolute top-0 left-0 ease-out duration-200 transition-all group-hover:w-full group-hover:h-full -z-1"></span>
      <span className="w-full text-white transition-colors duration-100 ease-in-out group-hover:text-red-500 z-10">
            Get started
      </span>
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
const link="https://image.tmdb.org/t/p/w500"
const data=ref(null)
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
    const res= await axios.get('https://movie-system-api.onrender.com/trending');
    data.value=res.data.results
    console.log(data.value)
})
</script>
<style>

</style>