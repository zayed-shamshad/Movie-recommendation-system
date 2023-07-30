<template>
    <div class="w-screen min-h-screen">
      <div class="flex space-x-4 w-screen bg-gray-700 bg-opacity-70 flex flex-row justify-center ">
        <router-link
            to="/movies/trending"
            class="transform transition-all duration-200 ease-in-out px-2"

            :class="selectedLink == 'trending' ? 'bg-red-600' : ''"
            
            @click="selectLink('trending')"
         >Trending</router-link>
        <router-link
            to="/movies/toprated"
             class=" transform transition-all duration-200 ease-in-out  px-2"
               :class="selectedLink == 'toprated' ? 'bg-red-600' : ''"
           
            @click="selectLink('toprated')"
         >Top Rated</router-link>
        <router-link
            to="/movies/upcoming"
             class="transform transition-all duration-200 ease-in-out px-2"
               :class="selectedLink == 'upcoming' ? 'bg-red-600' : ''"
           
            @click="selectLink('upcoming')"
       >Upcoming</router-link>
        <router-link
            to="/movies/nowplaying"
             class="transform transition-all duration-200 ease-in-out px-2"
               :class="selectedLink == 'nowplaying' ? 'bg-red-600' : ''"
            
            @click="selectLink('nowplaying')"
        >Now Playing</router-link>
    </div>
      <router-view v-slot="{ Component }">
            <!-- <transition name="fade"> -->
                <component :is="Component" />
            <!-- </transition> -->
        </router-view>
    </div>
</template>
<script setup>
import { ref } from 'vue';
const selectedLink = ref('trending');

const selectLink = (link) => {
    selectedLink.value = link;
};
</script>
<style>

</style>