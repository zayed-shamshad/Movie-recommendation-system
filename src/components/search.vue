<template>
    <div class="search-outerbox">
        <div class="wave">
            <div v-for="i in 30" :key='i' class="wave-inner" :id="i">
            </div>
        </div>
        <div v-if="searched" class="movie-box">
           
                <font-awesome-icon icon="close" @click="searched=false"></font-awesome-icon>
            <poster :title="movies[ind]" :link="links[ind]" :review="overview[ind]">
            </poster>
            <div class="bottom-buttons">
                <div>
                    Get more info
                </div>
                <button @click="changemovie">
                    Next
                </button>
                <div @click="addtofav" class="heart">❤</div>
            </div>
        </div>
        <div class="search-innerbox" v-if="!searched">
            <div class="search-title">
                Type in the name of the movie
            </div>
            <input type="text" v-model="movie" placeholder="Enter the movie name...">
            <button @click="makeRequest" class="search-movie">
                Search
            </button>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import poster from './poster.vue'
import {db} from '../firebase.js'
import { doc, setDoc, getDoc } from "firebase/firestore";
import { getAuth } from "firebase/auth";
import { onAuthStateChanged} from 'firebase/auth';
export default {
    name: 'search',
    components: {
        poster
    },
    data(){
        return{
            movies:[],
            overview:[],
            movie:'eg: batman...',
            searched:false,
            links:[],
            ind:0,
            fav:{}
        }
    },
    mounted(){
        console.log("i ran")
        this.wave();
        console.log(this.fav);
        onAuthStateChanged(getAuth(), async (user) => {
            if (user) {
                const docRef = doc(db, "users", user.email);
                const docSnap = await getDoc(docRef);
                if (docSnap.exists()) {
                    this.fav=docSnap.data();
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
    methods:{
        wave(){
          const k = document.getElementsByClassName('wave-inner');
          for (let i = 0; i < k.length; i++) {
              k[i].style.animation = 'wave 1s ease-in-out infinite';
              k[i].style.animationDelay = i * 0.05 + 's';
              k[i].style.backgroundColor = "red";
          }
            },
        async addtofav(){
            var user = getAuth().currentUser;
            if (this.movies[this.ind] in this.fav){
                document.getElementsByClassName('heart')[0].style.color = "yellow";
                delete this.fav[this.movies[this.ind]];
            }
            else{
            this.fav[this.movies[this.ind]] = this.movies[this.ind];
            document.getElementsByClassName('heart')[0].style.color = "blue";
            }
            await setDoc(doc(db, "users",  user.email),this.fav);

        },
        changemovie(){
           
            if(this.ind<this.movies.length-1){
                this.ind++;
            }
          
            else{
                this.ind=0; }

            if (this.movies[this.ind] in this.fav) {
                document.getElementsByClassName('heart')[0].style.color = "blue";
            }
            else{
                document.getElementsByClassName('heart')[0].style.color = "yellow";
            }
        },
        makeRequest(){
            const path = "https://movie-api-backend-a-z.herokuapp.com/"
            document.getElementsByClassName('wave')[0].style.display="flex";
           document.getElementsByClassName('search-innerbox')[0].style.display = "none";
            this.wave();
            axios.get(path + this.movie)
                .then(response => {
                    this.searched = true,
                    this.movies = Object.keys(response.data['1'])
                    this.overview = Object.values(response.data['2'])
                    this.links= Object.values(response.data['1'])
                }) 
                .catch(error => {
                    console.log(error)
                }) 
                .finally(() => (
                    document.getElementsByClassName('wave')[0].style.display = "none",
                    document.getElementsByClassName('search-innerbox')[0].style.display = "flex"
                ));
                setTimeout(() => {
                    if (this.movies[this.ind] in this.fav) {
                        document.getElementsByClassName('heart')[0].style.color = "yellow";
                        delete this.fav[this.movies[this.ind]];
                    }
                    else {
                        this.fav[this.movies[this.ind]] = this.movies[this.ind];
                        document.getElementsByClassName('heart')[0].style.color = "blue";
                    }
                }, 3000);
        }
    }
}
</script>
<style>

.search-title{
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    font-family: 'Limelight', cursive;
}
.heart{
    font-size: 1.5em;
    cursor:pointer;
    transition: all 0.24s ease-in-out;
}
.heart:hover{
    transform:scale(1.2);
    
}

.filled-in {
    font-weight: 900;
}

.bottom-buttons{
    width:70%;
    display:flex;
    justify-content: space-between;
    flex-direction: row;
    justify-content:space-between;
    margin:10px;
}

.bottom-buttons button{
    height:30px;
    width:80px;
    border-radius:5px;
    border:none;
    background-color: rgb(161, 0, 0);
    color:white;
    font-size: 1rem;
    font-weight: bold;
    transition:all 0.2s ease-in-out;
    cursor:pointer;
}
.bottom-buttons button:hover{
    background-color: red;
    color:white;
}
.movie-box{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    background:linear-gradient(to right, #2e8acc, rgb(193, 230, 28));
    border-radius: 10px;
    box-shadow: 0px 0px 10px #000;
    padding: 10px;
}
.search-outerbox{
    display: flex;
    left:50vw;
    top:50vh;
    transform: translate(-50%,10vh);
   
    justify-content: center;
    flex-direction: column;
    align-items: center;
    width: 80vw;
    height: 80vh;
    position:absolute;
    background-color: rgba(202, 0, 0, 0.5);
    border-radius: 10px;
    top:0;
}
.search-outerbox input{
    width: 300px;
    height: 30px;
    border-radius: 10px;
    border: none;
    background-color: #fff;
    font-size: 20px;
    color: #000;
    margin: 10px;
    padding:10px;
}
.search-movie{
    width: 100px;
    height: 40px;
    border-radius: 10px;
    border: none;
    background-color: rgb(255, 0, 0);
    font-size: 20px;
    color: rgb(255, 255, 255);
    cursor:pointer;
    z-index:10000;
    margin:10px;
    transition: all 0.2s ease-in-out;
   
}
.search-movie:hover{
    transform:scale(1.1);
    background-color:red;

}
.search-innerbox{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 50vw;
    height: 50vh;
    background-color: transparent;
    border-radius: 10px;
    position:relative;
    padding: 10px;
    top:0;
}
.wave {
    background-color: rgba(0,0,0,0.5);
    width: 50vw;
    height: 50vh;
    top: 50vh;
    left: 50vw;
    transform: translate(-70%, -35vh);
    position: absolute;

    display: none;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.wave-inner {
    width: 10px;
    height: 10vh;
    margin: 10px;
}

@keyframes wave {
    0% {
        transform: translateY(0) scale(1);

         /* transform: rotate(0deg); */
    }

    25% {
        transform: translateY(-100px) scale(0);

        /* transform: rotate(90deg); */
    }

    50% {
        transform: translateY(0) scale(1);

        /* transform: rotate(0deg); */
    }

    75% {
        transform: translateY(100px) scale(0);

        /* transform: rotate(90deg); */
    }

    100% {
        transform: translateY(0) scale(1);

        /* transform: rotate(0deg); */
    }

}


</style>