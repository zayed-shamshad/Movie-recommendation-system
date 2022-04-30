<template>
<div id="poster-box" data-tilt data-tilt-reverse="true">
   <div> <h4>{{title}}</h4></div>
    <img class="img-responsive" v-bind:src= "link">
    <div> <h4>{{review}}</h4></div>
 </div>
</template>
<script >
export default {
    name:'poster',
    props: {
    title: String,
    link: String,
    review:String,
},
methods:function(){
},
mounted() {
    let Script = document.createElement("script");
    Script.setAttribute("src", "https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.2/vanilla-tilt.js");
    document.head.appendChild(Script);
  }
}
</script>
<style >
#poster-box{
z-index: 100;
width:30vw;
background-color: rgba(255, 255, 255, 0.41);
padding:5px;
display: flex;
border-radius: 20px;
flex-direction: column;
align-content: center;
align-items: center;
margin: 10px;
transform: translateZ(20px);
}
div h4{
background-color: rgb(119, 119, 119);
border-radius: 5px;
margin: 10px;
padding:5px;
}
#poster-box img{
    border-radius: 25px;
}
a{
    font-style: none;
    color:white;
    text-decoration: none;
}
</style>
