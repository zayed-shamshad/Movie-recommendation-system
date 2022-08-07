<template>
    <div class="aboutcard">
        Hey !! ,I'm Mohammad Zaid, a tech enthusiast and a web developer,an undergrad at IIT Jodhpur.
        checkout my<a class="portfoliolink" href="https://zayed-shamshad.github.io/portfolio-zs/#/#home" target="blank">Portfolio</a>
    </div>
</template>
<script>
export default {
    name: 'about',
}
</script>
<style>
.aboutcard{
    width:70vw;
    margin-top:30vh;
    margin-left:15vw;
    height:40vh;
    display:flex;
    border-radius: 20px;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background-color:rgba(0,0,0,0.5);
    text-align:center;
    font-size:20px;
    font-family: 'Roboto', sans-serif;
}
.portfoliolink{
    color:aqua;
    text-decoration:none;
}
</style>