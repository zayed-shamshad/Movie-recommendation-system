<template>
    <button class="back_button" @click="goback">
        <font-awesome-icon icon="arrow-left"></font-awesome-icon>
    </button>
    <div v-if="loading" class="loading-fav">
        fetching....
    </div>
    <div v-if="!loading && !empty" class="loading-movies">
        <div class="outer-card">
            <transition-group name="list">
                <div v-for="movie in movies" :key="movie.id" class="movie-cards">
      <div class="movie-card-poster">
        <img class="img-responsive" :src="link + movie.poster_path" alt="Movie Poster">
      </div>
      <div>
        <div><h2>{{ movie.title.toUpperCase() }}</h2></div>
        <p><strong>Overview:</strong> {{ movie.overview }}</p>
        <p><strong>Release Date:</strong> {{ movie.release_date }}</p>
        <p><strong>Genres:</strong> {{ movie.genres.map(genre => genre.name).join(', ') }}</p>
        <p><strong>Runtime:</strong> {{ movie.runtime }} minutes</p>
        <p><strong>Tagline:</strong> {{ movie.tagline }}</p>
        <p><strong>Vote Average:</strong> {{ movie.vote_average }}</p>
         <font-awesome-icon icon="trash" class="trash" @click="trash(movie.id)"></font-awesome-icon>
      </div>
    </div>
            </transition-group>
        </div>
    </div>
    <div v-if="empty" class="loading-fav">
        <div class="no-fav-message">
            No movies in your favourite list
        </div>

    </div>
</template>
<script>
import { doc,getDoc } from "firebase/firestore";
import { db } from '../firebase.js'
import { setDoc} from "firebase/firestore";
import { useUserStore } from "../stores/store";
import axios from "axios";
import poster from "./poster.vue";
export default {
    name: 'fav',
    components:{
        poster
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
        goback() {
            this.$router.push('/');
        },
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
                        const options = {
                        method: 'GET',
                        headers: {
                            accept: 'application/json',
                            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZDYzMzQ1MzIxMTQwNDhmN2VlYTA3OGVkMTBlM2EwOSIsInN1YiI6IjYyNmFmOGFlOWI2ZTQ3MDBhNDVhODAyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MIBeEiA5qadK-dRQi1FYcNiZ037hIT-vnZ_hMiCKfm8'
                        }
                    };
                    if(this.fav!=undefined && this.fav.length!=0){
                         this.fav.forEach(async (id) => {
                            const res = await axios.get('https://api.themoviedb.org/3/movie/' +id, options);
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

.no-fav-message{
    font-size:1.5rem;
    text-align:center;
    color:rgb(0, 0, 0);
    background-color:white;
    width:30vw;
    height:30vh;
    display:flex;
    justify-content:center;
    font-family: 'Roboto', sans-serif;
    align-items:center;
    border-radius:10px;
}
.list-enter-active,
.list-leave-active {
    transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
    opacity: 0;
    transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
    position: absolute;
}
.trash{
  cursor:pointer;
  color:red;
  transition: all 0.2s ease-in-out;

}
.trash:hover{
    transform:scale(1.3);
}
.loading-movies{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    flex-direction: column;
    z-index: 1000;
    background-color: rgba(0, 0, 0, 0.5);
    color: aqua;

}
.loading-fav{
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    width:100vw;
    flex-direction:column;
    z-index: 1000;
    background-color:rgba(0,0,0,0.5);
    color:aqua;
}
.movie-cards{
    display:flex;
    justify-content:space-between;
    padding:10px;
    align-items:center;
    height:auto;
    width:80vw; 
    flex-direction:row;
    z-index: 0;
    background-color:white;
    color:rgb(0, 0, 0);
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    margin:10px;
}
.movie-card-poster{
    width:400px;
    z-index: 0;
    padding:5px;
    margin:20px;
    display: flex;
    border-radius: 20px;
    flex-direction: column;
    align-content: center;
    align-items: center;
}

.movie-cards img{
    border-radius: 25px;
}
.outer-card{
    display:flex;
    justify-content:flex-start;
    align-items:center;
    height:85vh;
    width:85vw;
    flex-direction:column;
    z-index: 0;
    background-color:rgba(0, 0, 0, 0.5);
    color:white;
    overflow-y:scroll;
    border-radius:10px;
}

</style>