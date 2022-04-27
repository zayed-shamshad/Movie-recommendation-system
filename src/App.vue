<template>
<nav>
</nav>
<div class="entry"><box id='boxx'>lol</box>
<div class="loading" v-if="loading">
    Loading....
</div>
<div class="loading" v-if="showerror">
    error 404 :((((
    <div class="retry"><button class="retry-button" @click="reset">retry</button></div>
</div>
<div class="loading" v-if="success">
    sucessfull !
    the recommended movie is {{this.ans}}
    <div class="retry"><button class="retry-button" @click="reset">Back</button></div>
</div>
<div v-if="initial">
<div class="main-search-input-wrap">
     <div class="main-search-input fl-wrap">
         <div class="main-search-input-item"> <input type="text" v-model="message" placeholder="Enter a movie name..."> </div> <button class="main-search-button" @click="makeRequest">GO !</button>
     </div>
 </div>
</div>
</div>
</template>
<script>
import axios from 'axios'
import BOX from './components/BOX.vue'
export default{
  name:'App',
  components:{'box':BOX},
  data() {
      return{
        loading: false,
        success:false,
        initial:true,
        showerror:false,
        ans:""
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
        this.ans="";
    },
    makeRequest:function () {
            this.loading = true
            const path="http://localhost:5000/"
            axios.get(path+this.message)
            .then(response => {this.success=true;
            this.initial = false;
            this.loading = false;
            this.showerror = false;
            console.log(response.data);
            this.ans=response.data
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
    position :absolute;
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

.main-search-button {
    background: #4DB7FE
}

.main-search-button {
    position: absolute;
    right: 0px;
    height: 50px;
    width: 120px;
    color: #fff;
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
.entry{
  background-image: url("./assets/movie poster 2.jpg");
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
}
.retry{
    position: relative;
    padding: 10vh;
}
.retry-button{
    border:none;
    border-radius:5px;
    color:rgb(255, 249, 249);
    height:5vh;
    width:5vw;
    background-color: #4DB7FE;
}
</style>
