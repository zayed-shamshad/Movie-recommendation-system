<template>
<div class="h-screen w-screen flex flex-col justify-between
 bg-image-1
  md:bg-image-2
  lg:bg-image-3
">
   <div class="flex items-center justify-between px-4 bg-gray-800 h-1/6 bg-opacity-10" >
      <!-- Search input and button centered -->
      <div class="flex items-center justify-center mx-auto opacity-100">
        <input type="text" v-model="movie" placeholder="Enter the movie name..." class="text-black px-4 py-1 rounded-l-lg focus:outline-none focus:ring focus:border-blue-300">
        <button @click="makeRequest"
        @keyup.enter="makeRequest" 
         class="px-4 py-1 bg-red-500 text-white rounded-r-lg">
          Recommend
        </button>
      </div>
    </div>

  <div class="flex items-center justify-center w-screen h-5/6 
 ">

      <div v-if="initial" class="flex flex-col items-center text-black justify-center h-full">
      </div>

      <div v-else-if="load && !errornotfound && !initial" class="flex flex-col items-center justify-center h-full">
        <pulse-loader :loading="load" :color="'red'" :size="'50px'" :margin="'2px'" :speed="'1s'" :trail="'10'"
          :shadow="'0'" :shadowColor="'#fff'" :shadowSize="'0'" :radius="'10px'"></pulse-loader>
      </div>

     <div v-else-if="movies.length !== 0 || (!errornotfound && !load && !initial)" class="flex flex-col items-center justify-center h-full p-2">
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 overflow-scroll">
        <transition-group name="list" appear>
        <movie-card
          v-for="movi in movies"
          :key="movi.id"
          :id="movi.id"
          :title="movi.title"
          :overview="movi.overview"
          :links="movi.poster_path"
        ></movie-card>
        </transition-group>
      </div>
    </div>

      <div v-else-if="errornotfound && !load && !initial" class="flex flex-col p-2 text-lg text-black items-center justify-center bg-white rounded-lg">
        <!-- Content for the error state -->
        <font-awesome-icon icon="exclamation-triangle" class="text-red-500 text-2xl md:text-8xl"></font-awesome-icon>
        <p>Error !</p>
      </div>
    </div>
</div>

</template> 

<script>
import axios from 'axios'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import movieCard from './movie-card.vue'

export default {
    name: 'search',
    components: {
        PulseLoader
        , movieCard
    },
    data() {
        return {
            load:true,
            movies: [],
            movie: '',
            initial: true,
            errornotfound: false,
        }
    },
    methods: {
        async makeRequest() {
            this.initial = false;
            this.errornotfound = false;
            this.load = true;
            const path = "http://127.0.0.1:5000/movie?s="+this.movie;
            console.log(this.movie);
            try{
                const response =await axios.get(path)
                this.movies=response.data;
                console.log(this.movies);
                if(this.movies.length==0){
                    this.errornotfound = true;
                    this.load = false;
                    this.initial = false;
                    return;
                }
                this.errornotfound = false;
                this.load = false;
                this.initial = false;
                this.ind=0;
            }
            catch(error){
                    this.errornotfound = true;
                    this.load = false;
                    this.initial = false;
                    console.log(error)
                }
        }
    }
}
</script>

 <style>


</style> 