<template>
<div class="entry">
<div class="loading" v-if="loading">
    <img src="./assets/loading-23.gif">
</div>

<div class="Error" v-if="showerror" >
   <img src="./assets/please_ta.gif">
    <div class="retry"><button class="retry-button" @click="reset">retry</button></div>
</div>

<div class="successful" v-if="success" > 
  <poster class="movie-poster" v-for="(item, key, index) in movies" v-bind:key= "index" :link= "item" :title= "key"></poster>
   <div class="retry"><button class="retry-button" @click="reset">Back</button></div>
</div>
<div v-if="initial">
<box id='boxx'></box>
<div class="main-search-input-wrap">
     <div class="main-search-input fl-wrap">
         <div class="main-search-input-item"> <input type="text" v-model="message" placeholder="Enter a movie name..."> </div> <button class="main-search-button" @click="makeRequest">Recommend</button>
     </div>
</div>
</div>
</div>
</template>
<script >
import axios from 'axios'
import BOX from './components/BOX.vue'
import poster from './components/poster.vue'
export default{
  name:'App',
  components:{'box':BOX,'poster':poster},
  data() {
      return{
        loading: false,
        success:false,
        initial:true,
        showerror:false,
        movies:"",
        }
  }
,
methods:{
    reset:function(){
        this.initial=true;
        this.showerror=false;
        this.loading=false;
        this.success=false;
        this.message="";
        this.movies="";
    },
    makeRequest:function () {
            this.loading = true
            this.initial=false
            const path="http://localhost:5000/"
            axios.get(path+this.message)
            .then(response => {this.success=true;
            this.initial = false;
            this.loading = false;
            this.showerror = false;
            this.movies=response.data
            }) // code to run on success
            .catch(error => { this.showerror=true; this.initial=false;
            console.log(error)}) // code to run on error
            .finally(() => (this.loading = false)) // set loading to false when request finish
    }
}
}
</script>
<style lang="scss">
.main-search-input {
    background: #fff;
    padding: 0 120px 0 0;
    border-radius: 1px;
    margin-top: 200px;
    box-shadow: 0px 0px 0px 6px rgba(255, 255, 255, 0.3)
}
nav{
    width:100vw;
    height:10vh;
    background-color:black;
    top:0;
    position :relative;
    z-index:10;
}

.fl-wrap {
    float: left;
    width: 100%;
    position: relative
}

.main-search-input:before {
    content: '';
    position: absolute;
    bottom: -40px;
    width: 50px;
    height: 1px;
    background: rgba(255, 255, 255, 0.41);
    left: 50%;
    margin-left: -25px
}

.main-search-input-item {
    float: left;
    width: 100%;
    box-sizing: border-box;
    border-right: 1px solid #eee;
    height: 50px;
    position: relative
}

.main-search-input-item input:first-child {
    border-radius: 100%
}

.main-search-input-item input {
    float: left;
    border: none;
    width: 100%;
    height: 50px;
    padding-left: 20px
}

.main-search-button:hover{
    background: #a59f9f;
    color:rgb(255, 255, 255);
}

.main-search-button {
    position: absolute;
    right: 0px;
    height: 50px;
    width: 120px;
    color: #fff;
    background: #000000;
    top: 0;
    border: none;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
    cursor: pointer
}

.main-search-input-wrap {
    max-width: 500px;
    left:30vw;
    position: relative
}

:focus {
    outline: 0
}

@media only screen and (max-width: 768px) {
    .main-search-input {
        background: rgba(255, 255, 255, 0.2);
        padding: 14px 20px 10px;
        border-radius: 10px;
        box-shadow: 0px 0px 0px 10px rgba(255, 255, 255, 0.0)
    }

    .main-search-input-item {
        width: 100%;
        border: 1px solid #eee;
        height: 50px;
        border: none;
        margin-bottom: 10px
    }

    .main-search-input-item input {
        border-radius: 6px !important;
        background: #fff
    }

    .main-search-button {
        position: relative;
        float: left;
        width: 100%;
        border-radius: 6px
    }
}
body{
    background-image: url("./assets/movie poster 2.jpg");
    background-attachment: fixed;
    width:100vw;
    height:100vh;
    margin:0;
    padding:0;
    z-index: -10;
}
*{
margin: 0;
padding: 0;
}
#boxx{
  height:50vh;
  width:60vw;
  position: absolute;
  top:20vh;
  background-color: rgba(0,0,0,.5);
  color: #fff;
  border-radius: 10px;
  left:20vw;
  border:2px solid white
}
.loading{
    width:60vw;
    height:50vh;
    z-index:20;
    position: absolute;
    top:20vh;
    left:20vw;
    color:white;
    background-color: rgba(0,0,0,.5);
    text-align: center;
    font-size: 10vh;
    border:1px solid white;
    border-radius:20px;
}
.retry{
    margin:50px;
    padding:50px;
}
.retry-button{
    border:none;
    border-radius:5px;
    color:rgb(255, 249, 249);
    height:10vh;
    width:10vw;
    background-color: #000000;
    font-size: 5vh;
}
.retry-button:hover{
    color:rgb(255, 249, 249);
   
    background-color: #ababab;
}
.successful{
    z-index:20;
    position: absolute;
    color:white;
    text-align: center;
    font-size: 3vh;
    display: flex;
    flex-direction: row;
    flex-wrap:wrap;
    margin:0;
    padding: 0;
}
.movie-poster{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
ul{
    list-style: none;
}
.Error{
    display: flex;
    flex-direction: column;
    align-content: center;
    align-items: center;
    width:60vw;
    height:50vh;
    z-index:20;
    position: absolute;
    padding:2vh;
    left:20vw;
    color:white;
    text-align: center;
    font-size: 5vh;
}
.Error img{
    border-radius:20px;
}

.img-responsive {
  width: 20vw;
  max-width:500px;
}
.loading img{
    width:30vw;
    top:10vh;
}

</style>
