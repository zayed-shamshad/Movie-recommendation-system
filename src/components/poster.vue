<template>
<div id="poster-box" data-tilt data-tilt-reverse="true" @click="showModall">
    <div> <h4>{{title.toUpperCase()}}</h4></div>
    <img class="img-responsive" v-bind:src= "link">
<Teleport to="body">
    <transition name="slide" appear>
    <div class="modal-overlay" v-if="showModal" @click="showModall=false"></div>
   </transition>
   <transition name="slide" appear>
    <div v-if="showModal" class="modal">
    <h1>{{title}}</h1>
   <p>{{review}}</p>
   <button class="but" @click="close">
    Close
   </button>
   </div>
    </transition>
</Teleport>
 </div>
</template>
<script >
export default {
    name:'poster',
    props: {
    title: String,
    link: String,
    review: String,
    },
data(){
    return{
      showModal:false
    }
}
,
methods:{
    showModall:function(){
        this.showModal=!this.showModal;
    },
    close:function(){
        this.showModal=false;
    }
}
    ,
mounted() {
    let Script = document.createElement("script");
    Script.setAttribute("src", "https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.2/vanilla-tilt.js");
    document.head.appendChild(Script);
  }
}
</script>
<style>
#poster-box{
z-index: 100;
width:310px;
padding:5px;
margin:20px;
display: flex;
border-radius: 20px;
flex-direction: column;
align-content: center;
align-items: center;
}

div h4{
border-radius: 5px;
margin: 10px;
padding:5px;
font-size: 1.5rem;
}

#poster-box img{
    border-radius: 25px;
}
a{
    font-style: none;
    color:white;
    text-decoration: none;
}
.modal-overlay {
    z-index: 100000;
 position: fixed;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 background-color: rgba(0, 0, 0, 0.3);
}

.modal {
    z-index: 10000000;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 60%;
    max-width: 400px;
    background-color: #FFF;
    border-radius: 16px;
    padding: 25px;
}
.modal h1{ 
  color: #222;
  font-size: 32px;
  font-weight: 900;
  margin-bottom: 15px;
}
 .modal p{
  color: #666;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 15px;
 }
 
</style>
