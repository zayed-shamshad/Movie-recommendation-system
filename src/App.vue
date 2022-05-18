<template>
<div class="entry">
<div class="loading" v-if="loading">
    <img src="./assets/loading-23.gif">
</div>

<div class="Error" v-if="showerror" >
   <img src="./assets/Try-again.jpg">
    <div class="retry"><button class="retry-button" @click="reset">retry</button></div>
</div>

<div class="successful" v-if="success" > 

  <poster class="movie-poster" v-for="(item, key, index) in movies" v-bind:key= "index" :link= "item" :title= "key" :review= "overview[key]"></poster>
  <div class="back"><button class="back-button" @click="reset">Back</button></div>
</div>
<div v-if="initial">
<box id='boxx'></box>
<div class="main-search-input-wrap">
     <div class="main-search-input fl-wrap">
         <div class="main-search-input-item">
         <input type="text" v-model="message" placeholder="Enter a movie name..."> 
         </div>
          <button class="main-search-button" @click="makeRequest">Recommend</button>
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
        overview:"",
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
        this.overview="";
    },
    makeRequest:function () {
            this.loading = true
            this.initial=false
            const path="https://movie-api-backend-a-z.herokuapp.com/"
            axios.get(path+this.message)
            .then(response => {this.success=true;
            this.initial = false;
            this.loading = false;
            this.showerror = false;
            this.movies=response.data['1']
            this.overview=response.data['2']
            console.log(this.movies)
            console.log(this.overview)
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
    margin-top: 40vh;
    margin-left: auto;
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
    position: relative;
}

.main-search-input:before {
    content: '';
    position: absolute;
    bottom: -40px;
    width: 50px;
    height: 1px;
    background: rgba(255, 255, 255, 0.41);
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
    padding-left:20px;
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
    right:30vw;
    position: absolute;
}
:focus {
    outline: 0
}
@media only screen and (max-width: 768px) {
   
    .main-search-input {
        background: rgba(255, 255, 255, 0.2);
        padding: 10px;
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
        background: rgb(255, 255, 255);
        position: relative;
        float: left;
        width: 88%;
        border-radius: 6px
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
  border-radius: 25px;
  left:20vw;
  transition: 0.4s ease-out;
  &:hover{
      box-shadow: 6px 6px rgba(203, 203, 203, 0.8);
  }
}
.loading{
    width:60vw;
    height:50vh;
    z-index:20;
    position: absolute;
    top:25vh;
    left:20vw;
    color:white;
    background-color: rgba(0,0,0,.5);
    text-align: center;
    font-size: 10vh;
    border-radius:25px;
}
.retry{
    margin:50px;
    padding:50px;
}
.back{
    margin:20px;
    padding:20px;
    position:fixed;
    transform: translateZ(20px);
    right:5px;
    bottom:5px;
    z-index: 1000;
}
.retry-button{
    border:2px solid white;
    border-radius:10px;
    color:rgb(255, 249, 249);
    height:7vh;
    width:9vw;
    background-color: #000000;
    font-size: 2.4vw;
}
.retry-button:hover{
    color:rgb(255, 249, 249);
    background-color: #ababab;
}
.back-button{
    border:2px solid white;
    border-radius:5px;
    color:rgb(255, 249, 249);
    height:6vh;
    width:9vw;
    background-color: #000000;
    font-size: 2.4vw;
}
.back-button:hover{
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
    height:50vh;
    width:100%;
    z-index:20;
    top:100px;
    position: absolute;
    color:white;
    text-align: center;
    font-size: 5vh;
}
.Error img{
    border-radius:20px;
    width:36vh;
}

.img-responsive {
  width: 20vw;
  max-width:500px;
}
.loading img{
    width:37vh;
    top:23vh;
}
.fade-enter-active,
.fade-leave-active {
 transition: opacity .5s;
}

.fade-enter,
.fade-leave-to {
 opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
 transition: transform .5s;
}

.slide-enter,
.slide-leave-to {
 transform: translateY(-50%) translateX(100vw);
}

.but {
 appearance: none;
 outline: none;
 border: none;
 background: none;
 cursor: pointer;
 display: inline-block;
 padding: 15px 25px;
 background-image: linear-gradient(to right, #CC2E5D, #FF5858);
 border-radius: 8px;
 
 color: #FFF;
 font-size: 18px;
 font-weight: 700;
 
 box-shadow: 3px 3px rgba(0, 0, 0, 0.4);
 transition: 0.4s ease-out;
 }
 .but :hover{
  box-shadow: 6px 6px rgba(0, 0, 0, 0.6);
 }

</style>
