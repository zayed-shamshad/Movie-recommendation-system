<template>
    <!-- <div class="circle-box">
        <div class="bg-circle">

        </div>
    </div> -->
    <div class="intro">
        <div class="title">
            <div class="title-bg">Movie Recommendation Engine</div>
        </div>
        <button class="get-started" @click="() => {$router.push('/search');
        }">
            Get started
        </button>
        <div class="content">
           With this Movie Recommendation Engine you can find the best movies for you and your friends to watch in no time.

        </div>
    </div>
    <!-- <div class="description">
        <div class="cards" v-for="card in cards" :key="card">
            <div class="card-title">
                {{card.title}}
            </div>
            <div class="card-content">
                {{card.content}}
            </div>
        </div>
    </div> -->
</template>
<script>
export default {
    name: 'home',
    data(){
        return{
            cards: [{ title: "2000+ Movies", content: "More than 2000 movies to choose from" }, { title: "AI based", content: "Latest " }, { title: "", content: "lorem ipsum" }]
        }
    }
}
</script>
<style>
.title-bg{
   /* background:linear-gradient(to right,#ff0000,#fbff00,#660098); */
   background: white;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-position:left;
    background-size:200%;
   /* animation:background-motion 5s ease-in-out infinite alternate;*/
}
.circle-box{
    position: absolute;
    width:100vw;
    height:100vh;;
    z-index:-1;
    overflow:hidden;
    display:flex;
}

.bg-circle{
    display:flex;
    position:absolute;
    width:100px;
    right:0;
    top:50%;
    transform:translateX(50%);
    height:100px;
    border-radius:50%;
    background-color: #e22d2d;
    box-shadow: 0px 0px 0 100px rgb(21, 215, 208), 0px 0px 0 200px rgb(243, 6, 6),0px 0px 0 300px rgb(120, 228, 5);

}
.get-started{
    background-color: #000000;
    color: white;
    padding: 10px;
    border-radius: 5px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
    border:none;
    transition:all 0.2s ease-in-out;
    margin-top:30px;
    margin-bottom: 30px;
}
.get-started:hover{
    transform:scale(1.1);
}
@keyframes background-motion{
    0%{
        background-position:left;
    }
    100%{
        background-position:right;
    }
}
</style>