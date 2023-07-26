<template>

    <div class="w-screen h-screen flex bg-gray-100 justify-center items-center flex-col">
        <div class="text-4xl">
            Movie App
        </div>
        <button
        class="text-white bg-red-500 rounded-lg p-4"
         @click="() => {
            $router.push('/search');
        }">
            Get started
        </button>
    </div>
</template>
<script>
import YouTube from 'vue3-youtube'
export default {
    name: 'home',
}
</script>
<style>

</style>