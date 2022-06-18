<template>
    <div v-if="loading" class="loading-fav">
        fetching....
    </div>
    <div v-if="!loading && !empty" class="loading-movies">
        <div class="outer-card">
            <transition-group name="list">
                <div v-for="movie in movies" :key="movie" class="movie-cards">
                    {{movie}}
                    <font-awesome-icon icon="trash" class="trash" @click="trash(movie)"></font-awesome-icon>
                </div>
            </transition-group>
        </div>
    </div>
    <div v-if="empty" class="loading-fav">
        you have no favourites :(
    </div>
</template>
<script>
import { getAuth} from 'firebase/auth';
import { onAuthStateChanged} from 'firebase/auth';
import { doc,getDoc } from "firebase/firestore";
import { db } from '../firebase.js'
import { setDoc} from "firebase/firestore";
export default {
    name: 'fav',
    data(){
        return{
            loading:true,
            movies:[],
            fav:{},
            empty:false
        }
    },
    watch:{
        movies(){
            if(this.movies.length==0){
                this.empty=true
            }
        }
    },
    methods:{
      async trash(movie){
            var user = getAuth().currentUser;
            delete this.fav[movie];
            await setDoc(doc(db, "users", user.email), this.fav);
            this.loaddata();
        },
        loaddata(){
            onAuthStateChanged(getAuth(), async (user) => {
                if (user) {
                    const docRef = doc(db, "users", user.email);
                    const docSnap = await getDoc(docRef);
                    if (docSnap.exists()) {
                        this.fav = docSnap.data();
                        this.movies = Object.values(this.fav);

                        this.loading = false;
                    }
                    else {
                        console.log("mo fav");
                    }
                    console.log(this.fav);
                } else {
                    console.log("No user is signed in");
                    // No user is signed in.
                }
            });

        }

    },
    mounted(){
        this.loaddata();
    },
    }
</script>
<style>
/* .list-move, */
/* apply transition to moving elements */
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
    height:60px;
    width:500px;
    flex-direction:row;
    z-index: 0;
    background-color:rgba(0,0,0,0.5);
    color:rgb(255, 255, 255);
    margin:10px;
    
}
.outer-card{
    display:flex;
    justify-content:flex-start;
    align-items:center;
    height:85vh;
    width:85vw;
    flex-direction:column;
    z-index: 0;
    background-color:rgba(255, 23, 23, 0.5);
   color:white;
   overflow-y:scroll;
    
}
</style>