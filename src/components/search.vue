<template>
    <div class="search-outerbox">
        <div class="search-innerbox">
            <input type="text" v-model="movie" placeholder="Enter the movie name...">
            <button @click="makeRequest" class="search-movie">
                Search
            </button>
        </div>
    </div>
    <button class="back_button" @click="goback">
        <font-awesome-icon icon="arrow-left"></font-awesome-icon>
    </button>
    <div class="movie-outerbox">
        <div class="image-bg1">
        </div>
        <div class="image-bg2">
        </div>
        <div class="image-bg3">
        </div>
        <transition name="fade" appear>
            <div class="initial" v-if="!load && !errornotfound && initial">

            </div>
            <div class="wave" v-else-if="load && !errornotfound && !initial">
                <pulse-loader :loading="load" :color="'red'" :size="'50px'" :margin="'2px'" :speed="'1s'" :trail="'10'"
                    :shadow="'0'" :shadowColor="'#fff'" :shadowSize="'0'" :radius="'10px'"></pulse-loader>
            </div>
            <div class="movie-box" v-else-if="!errornotfound && !load && !initial">
                <font-awesome-icon icon="close" @click="closebox"></font-awesome-icon>
                <movie-card :id="movies[ind].id" :title="movies[ind].title" :overview="movies[ind].overview" :links="movies[ind].poster_path">
                </movie-card>
                <div class="bottom-buttons">
                    <button @click="changemovieback">
                        <font-awesome-icon icon="chevron-left"></font-awesome-icon>
                    </button>
                    <button @click="changemovie">
                        <font-awesome-icon icon="chevron-right"></font-awesome-icon>
                    </button>
                </div>
            </div>
            <div v-else-if="errornotfound && !load && !initial" class="error">
                <font-awesome-icon icon="exclamation-triangle" class="erroricon"></font-awesome-icon>
                <p>Error</p>
            </div>
        </transition>

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
            ind: 0,
            initial: true,
            errornotfound: false,
        }
    },
    methods: {
        goback() {
            this.$router.push('/');
        },
        closebox() {
            this.initial = true;
        },
        changemovieback() {
            if (this.ind > 0) {
                this.ind--;
            }
            else {
                this.ind = this.movies.length - 1;
            }
        },
        changemovie() {
            if (this.ind < this.movies.length - 1) {
                this.ind++;
            }
            else {
                this.ind = 0;
            }
        },
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
.back_button{
    top:10px;
    left:10px;
    position:absolute;
    z-index:1;
    width:50px;
    height:50px;
    background-color:transparent;
    border-radius:10px;
    padding:10px;
    color:white;
    font-size: 1.4rem;
    cursor:pointer;

}
.image-bg1{
    background:url('/assets/harley.jpg');
    background-size: cover;
    /* -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; */
    width:400px;
    line-height: 10px;
    height: 60vh;
    top:5vh;
    position:absolute;
    font-size: 5px;
    font-weight: bold;
    left:10px;
    border-radius: 30px;
}
.image-bg2 {
    background: url('/assets/2001.jpg');
    background-size: cover;
    /* -webkit-background-clip: text; */
    /* -webkit-text-fill-color: transparent; */
    width: 400px;
    line-height: 5px;
    height: 60vh;
    top: 5vh;
    position: absolute;
    font-size: 10px;
    font-weight: bold;
    left: 50vw;
    transform: translateX(-50%);
    border-radius:30px;
}
.image-bg3{
    background: url('/assets/blackwidow.jpg');
    background-size: cover;
    /* -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; */
    width: 400px;
    line-height: 5px;
    height: 60vh;
    top: 5vh;
    position: absolute;
    font-size: 10px;
    font-weight: bold;
    right: 10px;
    border-radius: 30px;
}
.movie-outerbox{
    display:flex;
    position:absolute;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    height:80vh;
    width:100vw;
    top:20vh;
    background:linear-gradient(to right,rgb(255, 0, 0) , rgb(255, 255, 255), rgb(255, 0, 0));
    z-index:-10;
    
}

.search-title{
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    font-family: 'Limelight', cursive;
}
.heart{
    font-size: 2.5em;
    cursor:pointer;
    transition: all 0.24s ease-in-out;
    margin-top: 70px;
}
.heart:hover{
    transform:scale(1.2);

}

.filled-in {
    font-weight: 900;
}

.bottom-buttons{
    display:flex;
    justify-content: space-evenly;
    flex-direction: column;
    margin:10px;
}
.bottom-buttons button{
    height:30px;
    width:80px;
    border-radius:5px;
    border:none;
    background-color: rgb(31, 20, 17);
    color:white;
    font-size: 1rem;
    font-weight: bold;
    transition:all 0.2s ease-in-out;
    cursor:pointer;
    margin-top: 70px;
}
.bottom-buttons button:hover{
    transform:scale(1.2);
    color:white;

}
.erroricon{
    font-size: 5em;
    color:red;
    margin-top: 10px;
}
.error{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 300px;
    width: 300px;
    background-color: rgb(31, 20, 17);
    color: white;
    font-size: 1.5rem;
    font-weight: bold;
    border-radius: 10px;
    margin-top: 10vh;
    padding: 10px;
     z-index: 100;
     box-shadow: 0px 0px 10px rgb(0, 0, 0, 0.5);

}
.movie-box{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 10px;
    background:linear-gradient(to right,rgb(0, 0, 0) , rgb(255, 0, 0));
    box-shadow: 0px 0px 10px rgb(0,0,0,0.5);
    border-radius: 10px;
    box-shadow: 0px 0px 10px #000;
    padding: 10px;
    z-index:100;
}
.search-outerbox{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    height: 20vh;
    position:absolute;
    background:url('/assets/johnwick.jpg');
    background-size: stretch;
    box-shadow: 0px 0px 20px #000;
    border-radius: 10px;
}

.search-outerbox input{
    width: 400px;
    height: 25px;
    border-radius: 5px;
    border: none;
    background-color: #fff;
    font-size: 20px;
    color: #000;
    margin: 10px;
    padding:10px;
    outline:none;
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
    z-index:0;
    margin:10px;
    transition: all 0.2s ease-in-out;
}

.search-movie:hover{
    transform:scale(1.1);
    background-color:red;
}
.search-innerbox{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: transparent;
    border-radius: 10px;
    position:relative;
    padding: 10px;
    top:0;
}
.initial{
    background-color: transparent;
    width: 100vw;
    height: 80vh;
    position: absolute;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

}
.wave {
    background-color: transparent;
    width: 100vw;
    height: 80vh;
    position: absolute;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    z-index: 100;
}

.wave-inner {
    width: 10px;
    height: 15vh;
    margin: 5px;
    z-index: 100;
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