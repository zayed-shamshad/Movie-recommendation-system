<template>
    <div v-if="loading" class="loading-fav">
        fetching....
    </div>
    <div v-else class="loading-fav">
        <div class="outer-card">
            <div v-for="movie in movies" :key="movie" class="movie-cards">
                {{movie}}
            </div>
        </div>
    </div>
</template>
<script>
import { getAuth} from 'firebase/auth';
import { onAuthStateChanged} from 'firebase/auth';
import { doc,getDoc } from "firebase/firestore";
import { db } from '../firebase.js'

export default {
    name: 'fav',
    data(){
        return{
            loading:true,
            movies:[],
            fav:{}
        }
    },
    mounted(){

        onAuthStateChanged(getAuth(), async (user) => {
            if (user) {
                const docRef = doc(db, "users", user.email);
                const docSnap = await getDoc(docRef);
                if (docSnap.exists()) {
                    this.fav=docSnap.data();
                    this.movies = Object.values(this.fav);

                    this.loading = false;
                }
                else{
                    console.log("mo fav");
                }
                console.log(this.fav);
            } else {
                console.log("No user is signed in");
                // No user is signed in.
            }
       });
      
    },
    }
</script>
<style>

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
    justify-content:center;
    align-items:center;
    height:60px;
    width:300px;
    flex-direction:column;
    z-index: 0;
    background-color:rgba(0,0,0,0.5);
    color:rgb(255, 255, 255);
    margin:10px;
    
}
.outer-card{
    display:flex;
    justify-content:center;
    align-items:center;
    height:80vh;
    width:80vw;
    flex-direction:column;
    z-index: 0;
    background-color:rgba(255, 23, 23, 0.5);
   color:white;
   overflow-y:scroll;
    
}
</style>