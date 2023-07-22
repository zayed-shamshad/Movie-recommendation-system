<template>
    <div  @click="toggle">
            <div class="bar1"></div>
            <div class="bar2"></div>
            <div class="bar3"></div>
        </div>
    <div>
        <ul>
            <li>
                    <router-link to="/" @click="toggle">HOME</router-link>
            </li>
                <li>
                    <router-link to="/movies" @click="toggle">MOVIES</router-link>
                </li>
                <li>
                    <router-link to="/about" @click="toggle">ABOUT US</router-link>

                </li>

            </ul>
        </div>
</template>
<script setup>
import { ref } from 'vue'
const show = ref(false)
const toggle = () => show.value = !show.value

</script>