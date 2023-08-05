<template>
    <div class="">
        <!-- Loading state -->
        <div v-if="loading" class="flex items-center justify-center h-screen w-screen">
            <pulse-loader :loading="load" :color="'red'" :size="'50px'" :margin="'2px'" :speed="'1s'" :trail="'10'"
              :shadow="'0'" :shadowColor="'#fff'" :shadowSize="'0'" :radius="'10px'"></pulse-loader>
        </div>

        <!-- Movies list -->
        <div v-else-if="!loading && !empty" class="min-h-screen">
            <div class="flex flex-row justify-center text-4xl text-white
            title-trending text-xl md:text-4xl
            ">
                Favourites
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <transition-group name="fade">
                    <div v-for="movie in movies" :key="movie.id"
                        class="shadow-lg rounded-lg overflow-hidden bg-white" >
                        <div>
                            <img :src="link + movie.poster_path" alt="Movie Poster" class="w-full h-56 object-cover">
                        </div>
                        <div class="p-4 text-black">
                            <h2 class="text-xl font-semibold mb-2">{{ movie.title.toUpperCase() }}</h2>
                            <p><strong>Overview:</strong> {{ movie.overview }}</p>
                            <p><strong>Release Date:</strong> {{ movie.release_date }}</p>
                            <p><strong>Genres:</strong> {{ movie.genres.map(genre => genre.name).join(', ') }}</p>
                            <p><strong>Runtime:</strong> {{ movie.runtime }} minutes</p>
                            <p><strong>Tagline:</strong> {{ movie.tagline }}</p>
                            <p><strong>Vote Average:</strong> {{ movie.vote_average }}</p>
                            <button @click="trash(movie.id)"
                                class="mt-4 inline-flex items-center px-4 py-2 bg-red-500 text-white rounded-lg focus:outline-none hover:bg-red-600">
                                <font-awesome-icon icon="trash" class="mr-2"></font-awesome-icon>
                                Delete
                            </button>
                        </div>
                    </div>
                </transition-group>
            </div>
        </div>

        <!-- Empty state -->
        <div v-if="empty" class="flex items-center justify-center h-screen">
            <div>
                <font-awesome-icon icon="exclamation-triangle" class="text-red-500 text-8xl"></font-awesome-icon>
            </div>
        </div>
    </div>
</template>

<script>
import { doc,getDoc } from "firebase/firestore";
import { db } from '../firebase.js'
import { setDoc} from "firebase/firestore";
import { useUserStore } from "../stores/store";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import axios from "axios";
export default {
    name: 'fav',
    components: {
        PulseLoader
    },
    data(){
        return{
            loading:true,
            link:"https://image.tmdb.org/t/p/w500",
            fav:[],
            movies:[],
            empty:false,
            user:null,
            userstore:useUserStore()
        }
    },
    watch:{
        movies(){
            if(this.movies.length==0){
                this.empty=true;
            }
            else{
                this.empty=false;
            }
        }
    },
    methods:{
      async trash(movie){
            this.fav=this.fav.filter((m)=>{
                return m!=movie;
            })
            this.movies=this.movies.filter((m)=>{
                return m.id!=movie;
            })
            await setDoc(doc(db, "users", this.user.email)
            , {
                fav:this.fav
            }
            );
        },
       async loaddata(){
             this.user=this.userstore.getUser;
                if (this.user) {
                    const docRef = doc(db, "users", this.user.email);
                    const docSnap = await getDoc(docRef);
                    if (docSnap.exists()) {
                        this.fav = docSnap.data().fav;
                    if(this.fav!=undefined && this.fav.length!=0){
                         this.fav.forEach(async (id) => {
                            const res = await axios.get("https://movie-system-api.onrender.com/movie_data?movie_id="+id);
                            this.movies.push(res.data);
                        })
                        this.loading = false;
                    }
                    else {
                        console.log("no fav");
                        this.loading = false;
                        this.empty = true;
                    }
                }
                }
        }
    },
    mounted(){
        this.loaddata();
    },
    }
</script>
<style>

.trash{
  cursor:pointer;
  color:red;
  transition: all 0.2s ease-in-out;

}
.trash:hover{
    transform:scale(1.3);
}

</style>