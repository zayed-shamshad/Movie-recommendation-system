<template>
  <nav class="bg-red-600 py-4 px-6 w-screen">
    <div class="flex items-center justify-between">
      <!-- User Avatar and Email -->
      <div class="flex items-center">
        <div class="w-10 h-10 rounded-full overflow-hidden cursor-pointer">
          <img v-if="computedUser!=null" :src="user.photoURL" alt="User Avatar" class="w-full h-full object-cover">
          <img v-else src="../assets/avatar.png" alt="User Avatar" class="w-full h-full object-cover">
        </div>
        <span v-if="computedUser==null" class="text-white ml-2 font-semibold cursor-pointer" @click="showMenu('Login')">Sign in</span>
        <span v-else class="text-white ml-2 font-semibold cursor-pointer" @click="showMenu('Logout')">Log out</span>
      </div>

      <!-- Mobile View: Menu Icon -->
      <div class="md:hidden">
        <button @click="toggleMobileMenu">
          <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
            stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
      </div>

      <!-- Desktop View: Navigation Options -->
      <ul class="hidden md:flex space-x-4 text-white text-xl">
        <router-link to="/home">Home</router-link>
        <router-link v-if="computedUser" to="/favourites">Favourites</router-link>
        <router-link to="/movies">Movies</router-link>
        <router-link to="/search">Search</router-link>
      </ul>
    </div>

    <!-- Mobile View: Responsive Menu -->
    <div v-if="showMobileMenu" class="mt-2 md:hidden">
      <ul class="space-y-2 text-white">
        <router-link to="/home">
          <li>Home</li>
        </router-link>
        <router-link 
        v-if="computedUser"
        to="/favourites" 
        >
          <li>Favourites</li>
        </router-link>
        <router-link to="/movies">
          <li>Movies</li>
        </router-link>
        <router-link to="/search">
          <li>Search</li>
        </router-link>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';
import { computed } from 'vue';
import {defineEmits } from 'vue';
import { useUserStore } from '../stores/store';
const userstore = useUserStore();
const user=ref(null)
user.value=userstore.getUser;
console.log(user.value);
const showMobileMenu = ref(false);

const emits = defineEmits(['changeState']);

const computedUser = computed(() => {
  user.value=userstore.getUser;
  return user.value;
});

function showMenu(state) {
  console.log("trying");
  emits("changeState", state);
}


function toggleMobileMenu() {
  showMobileMenu.value = !showMobileMenu.value;
}

</script>

<style>
@media (min-width: 768px) {

  /* Adjust the alignment for desktop view */
  .flex.items-center.justify-between {
    flex-wrap: nowrap;
  }

  /* Hide the mobile menu on desktop view */
  .md\\:hidden {
    display: none;
  }
}
</style>
