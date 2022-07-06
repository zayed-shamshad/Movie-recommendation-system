<template>
    <div>
        <!-- v-if="state=='LOGOUT'" -->
        <div>
            <img :src="avatar" @click="openprofile" class="openprofile">
        </div>
    </div>
    <div class="profile">
        <div class="profileheader">
            Profile
            <div @click="closeprofile" class="closeprofile">
                <font-awesome-icon icon="close" class="closeprofile"></font-awesome-icon>
            </div>
            <img :src='avatar' class="avatar">
            <div class="username">
                <font-awesome-icon icon="user" class="icons"></font-awesome-icon>
                {{username}}
            </div>
            <div class="username">
                <font-awesome-icon icon="envelope" class="icons"></font-awesome-icon>
                {{email}}
            </div>
            <div @click="openfav();closeprofile()" class="username" v-if="state=='LOGOUT'">
                <font-awesome-icon icon="star" class="icons"></font-awesome-icon>
                favourites
            </div>
            <div @click="login" class="username">
                <font-awesome-icon icon="sign-out" class="icons"></font-awesome-icon>
                {{state}}
            </div>
        </div>
    </div>
    <div class="login" v-if="state=='LOGIN'">
        <div class="close-popup" @click="closepopup">
            <font-awesome-icon icon="close"></font-awesome-icon>
        </div>
        SIGN IN

        <input type="email" v-model="email" placeholder="email">

        <input type="password" v-model="password" placeholder="Password">

        <button @click="submit" class="submit-button">
            <font-awesome-icon icon="sign-in" class="icons"></font-awesome-icon>
            Login
        </button>
        <button class="google-button" @click="googlesignup">
            <font-awesome-icon :icon='["fab","google"]' class="icons"></font-awesome-icon>
            signup with google
        </button>
    </div>
    <div class="logout" v-if="state=='LOGOUT'">
        <div>
            Logout ?
        </div>
        <div>
            <button @click="logout">
                <font-awesome-icon icon="sign-out" class="icons"></font-awesome-icon>
                Logout
            </button>
            <button @click="closeLogout">
                <font-awesome-icon icon="close" class="icons"></font-awesome-icon>
                Cancel
            </button>
        </div>
    </div>
    <div class="container" @click="toggle">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
    </div>
    <div class="menu-bg">

    </div>
    <div class="nav-menu">
        <ul>
            <li>
                <router-link to="/" @click="toggle">HOME</router-link>
            </li>
            <li>
                <router-link to="/movies">MOVIES</router-link>
            </li>
            <li>
                <router-link to="/blog">BlOGS</router-link>
            </li>
            <li>
                <router-link to="/about">ABOUT US</router-link>

            </li>
            <!-- <li @click="login">
                <router-link to="">{{state}}</router-link>
            </li> -->

        </ul>
    </div>

    <router-view v-slot="{ Component }">
        <transition name="fade">
            <component :is="Component" />
        </transition>
    </router-view>

    <div class="footer">
        <font-awesome-icon :icon="['fab','github']"></font-awesome-icon>
        <font-awesome-icon :icon="['fab','instagram']"></font-awesome-icon>
        <font-awesome-icon :icon="['fab','twitter']"></font-awesome-icon>
        <font-awesome-icon :icon="['fab','linkedin']"></font-awesome-icon>
        created by zayed
    </div>
</template>
<style>







@import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Limelight&display=swap');
/* we will explain what these classes do next! */
.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}
.username{
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        display: flex;
        width: 100%;
        justify-content: flex-start;
        align-items: center;
        flex-direction: row;
        font-size: 1rem;
        margin: 5px;

}
.username:hover{
    transform: scale(1.1);
}
.profileheader{
    width:300px;
    height:85vh;
    background-color:transparent;
    z-index:100;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:space-around;
    font-size: 1rem;
}
.icons{
    margin-right:10px;
}
/* .profileheader div::before {
    content: "";
    height: 1px;
    display:flex;
    align-items: center;
    justify-content: center;
    position:absolute;
    width: 0%;
    background: white;
    transform: translateY(25px);
    transition: all 0.3s ease-in-out;

}
.profileheader div:hover::before {
    width: 00%;
} */

.openprofile{
    width:50px;
    height:50px;
    background-color : rgba(0, 0, 0, 0.2);
    z-index:1;
   
    background-size: cover;
    display:flex;
    top:25px;
    right:150px;
    border-radius:50%;
    position:absolute;
    flex-direction:column;
    align-items:center;
    color:white;
    justify-content:space-around;
    border:none;
    cursor:pointer;
    
}
.profile{
    position: fixed;
    width:0vw;
    left:0px;
    top:0vh;;
    height:100vh;
    background: rgba(0, 0, 0, 0.7);
    z-index: 25;
    display:flex;
    justify-content: center;
    align-items: center;
    flex-direction:column;
    font-size:10px;
    transition:all 0.25s ease-in-out;
    overflow-x:hidden;
}
.avatar{
    width:120px;
    height:120px;
    border-radius:50%;
    margin-bottom:20px;
}
.closeprofile {
    width:20px;
    top: 3px;
    right: 5px;
    font-size: 20px;
    color: #fff;
    cursor: pointer;
    position: absolute;
}
.closeprofile:hover {
  color:red;
 transform:translate(0,0) scale(1.1);
}


.logout{
    width: 20vw;
    position: absolute;
    z-index: 20;
    height: 20vh;
    top: 30vh;
    left: 40vw;
    background: rgb(255, 255, 255);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 20px;
    transform: translateY(100%);
    transition: all 0.25s ease-in-out;
    opacity: 0;
    transform: scale(0);
    color: black;
    }
    .logout div:first-child{
        display:flex;
        font-size: 1.3rem;
        border-bottom:rgb(0, 0, 0) solid 1px;
       
        justify-content:space-evenly;
    }
    .logout button{
        background: rgb(255, 255, 255);
        border: none;
        border-radius: 20px;
        padding: 10px;
        font-size: 20px;
        margin-right:10px;
        font-family: 'Cairo', sans-serif;
        color: black;
        transition: all 0.2s ease-in-out;
        cursor:pointer;
    }
    .logout button:hover{
        border: none;
        border-radius: 20px;
        padding: 10px;
        font-size: 20px;
        font-family: 'Cairo', sans-serif;
        color: red;
        cursor:pointer;
    }

.login{
    width:30vw;
    position: absolute;
    z-index:20;
    height:60vh;
    top:20vh;
    left:35vw;
    background: rgb(255, 255, 255);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 20px;
    transform: translateY(100%);
    transition: all 0.3s ease-in-out;
    opacity:0;
    transform:scale(0);
    color:black;
}

.login input{
    width:20vw;
    padding:10px;
    font-size:17px;
    font-family: 'Cairo', sans-serif;
    border:none;
    border-bottom:2px solid black;
}
.login input:focus {
   border-bottom:2px solid green;
   outline:none;
}
.submit-button{
    width:20vw;
    letter-spacing: 10px;
    border-radius: 20px;
    padding:10px;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction: row;
    font-size:17px;
    font-family: 'Cairo', sans-serif;
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    border: 1px solid rgb(0, 0, 0);
    transition: all 0.2s ease-in-out;
}
.google-button{
    width:20vw;
    letter-spacing: 2px;
    border-radius: 20px;
    padding:10px;
    font-size:17px;
    font-family: 'Cairo', sans-serif;
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    border: 1px solid rgb(0, 0, 0);
    transition: all 0.2s ease-in-out;
}
.close-popup{
    position: absolute;
    top:0;
    right:0;
    width:10px;
    padding:10px;
    height:10px;
    border-radius:300px;
    background: rgb(255, 255, 255);
    z-index:10;
    cursor:pointer;
    color:black;
}
.login button:hover{
    background: rgb(0, 0, 0);
    color: rgb(255, 255, 255);
}
.nav-menu{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    position:absolute;
    right:20vw;
    top:20vh;
    background-color:transparent;
    opacity:0;
    transition:all 0.3s ease-in-out;
    font-size:2rem;
    color:white;
    z-index:2;
    width:40vw;
    height:50vh;
    transform: scale(0);
}
.nav-menu-change{
    transform:scale(1);
    opacity: 1;
    display: flex;
}
.nav-menu ul{
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    width:100%;
    height:100%;
    
}
.nav-menu ul li{
    text-decoration: none;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    margin:20px;
    opacity:0.2;
    transition:all 0.2s 0.1s ease-in-out;
}
.nav-menu ul li a{
    text-decoration: none;
    font-style: none;
    color: white;
   
}
.nav-menu-change ul li {
    opacity: 1;
}
.nav-menu-change ul li::before {
    position:absolute;
    content:"";
    width:0;
    background: rgb(255, 255, 255);
    display:flex;
    height:5px;
    align-items:center;
    justify-content:center;
    /* transform:translateY(50px); */
    transition:all 0.2s ease-in-out;
    opacity:0;
}
.nav-menu-change ul li:hover::before {
  opacity:1;
  transform: translateY(24px);  
  width: 100%;
 

}
.nav-menu-change ul li:hover{
   transform:scale(1.1);
}

.container {
    display: inline-block;
    cursor: pointer;
    position:absolute;
    top:30px;
    right:50px;
    z-index:20;
}

.bar1,
.bar2,
.bar3 {
    width: 35px;
    height: 5px;
    background-color: white;
    margin: 6px 0;
    transition: 0.4s;
}

.change .bar1 {
    -webkit-transform: rotate(-45deg) translate(-9px, 6px);
    transform: rotate(-45deg) translate(-9px, 6px);
}

.change .bar2 {
    opacity: 0;
}

.change .bar3 {
    -webkit-transform: rotate(45deg) translate(-8px, -8px);
    transform: rotate(45deg) translate(-8px, -8px);
}
.menu-bg{
    position:absolute;
    top: -50px;
    right: -100px;
    width:0;
    height:0;
    border-radius:50%;
    transition:all 0.4s ease-in-out;
    background:radial-gradient(circle, rgba(255, 0, 0, 0.7) 0%,rgba(255, 0, 0, 0.7) 100%);
    z-index:1;
}
.expand-bg{
    width: 110vw;
    height:110vw;
    transform: translate(18%, -20%);
  
}
.overflow{
    overflow:hidden;
}
body{
    font-family: 'Cairo', sans-serif;
    background: linear-gradient(to right,rgba(71, 202, 231, 0.5),rgba(43, 200, 124, 0.5),rgba(112, 233, 25, 0.5)),url('/assets/mp.jpg');
    background-repeat: no-repeat;
    z-index: -1;
    background-size: cover;
    background-attachment: fixed;
    width:100vw;
    height:100vh;
    color: white;
    position:absolute;
}
*{  margin: 0;
    padding: 0;
}
::-webkit-scrollbar {
    display: none;
}

.intro{
    width:100vw;
    top:0vh;
    position:absolute;
    height:100vh;
    background-color: rgba(0, 0, 0, 0.2);
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: 'Cairo', sans-serif;
    color: #ffffff;
    font-family: 'Limelight', cursive;
    font-size:3rem;
   
}
.description {
    width: 100vw;
    top: 100vh;
    position: absolute;
    height: 100vh;
    background-color: rgba(107, 226, 9, 0.2);
    display: flex;
    flex-direction: row;
    font-family: 'Cairo', sans-serif;
    color: #ffffff;
    justify-content: center;
    align-items: center;
    text-align: center;

}
.cards{
    box-shadow: 5px, 5px, 5px, 5px, rgba(0, 0, 0, 0.2);
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    width:25vw;
    height:250px;
    background-color: rgba(0, 0, 0, 0.2);
    border-radius:10px;
    padding:20px;
    margin:20px;
    font-family: 'Cairo', sans-serif;
    color: #ffffff;
    font-size:2rem;
}
.title{
    display:flex;
    width:80vw;
    height:30vh;
    justify-content:center;
    align-items:center;
    font-size: clamp(40px, 8vw, 80px);
    background:linear-gradient(to right,rgba(6, 255, 226, 0.5),rgba(178, 237, 27, 0.5));
    
}
.content{
    display:flex;
    width:60vw;
    height:20vh;
    justify-content:center;
    align-items:center;
    font-size:1.4rem;
    text-align:center;
    font-family:Cairo, sans-serif;
    background: linear-gradient(to right, rgba(6, 255, 226, 0.5), rgba(178, 237, 27, 0.5));
    
}
.footer{
    bottom:0;
    height:5vh;
    width:100vw;
    background-color:rgb(0,0,0);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Cairo', sans-serif;
    font-size: 1.2rem;
    color: #ffffff;  
    position:fixed;
    padding:0;
    box-shadow: 0px 0px 10px #000;
    margin:0;
    left:0;
}
.footer svg{
    margin:10px;
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

</style>

<script>
import {getAuth , createUserWithEmailAndPassword} from 'firebase/auth';
import {GoogleAuthProvider,signInWithPopup} from 'firebase/auth';
import {onAuthStateChanged,signOut} from 'firebase/auth';
import poster from './components/poster.vue'
import {db} from './firebase.js'
import { doc, setDoc } from "firebase/firestore";
export default{
  name:'App',
  components:{'poster':poster},
  data() {
      return{
        email:'email id',
        username:'username',
        state:'LOGIN',
        avatar:'/assets/avatar.png',
    }
  }
,
mounted(){
    onAuthStateChanged(getAuth(),(user)=>{
        console.log("state changed !")
        if(user){
            console.log("user is still logged in")
            this.state='LOGOUT';
            this.username=user.displayName;
            this.avatar=user.photoURL;
            this.email=user.email;
           // document.getElementsByClassName('openprofile')[0].style.backgroundImage="url("+user.photoURL+")";
        }
        else{
            console.log("user is logged out")
            this.state='LOGIN';
            this.avatar='/assets/avatar.png';
            //document.getElementsByClassName('openprofile')[0].style.backgroundImage = "url(/assets/avatar.png)";
        }
    });

},
methods:{
    openfav(){
        this.$router.push('/fav');
    },
    closeLogout(){
        document.getElementsByClassName('logout')[0].style.transform='scale(0)';
    },
    closeprofile(){
        document.getElementsByClassName('profile')[0].style.width = '0vw';
        document.getElementsByTagName('body')[0].classList.remove('overflow');
    },
    openprofile(){
        document.getElementsByClassName('profile')[0].style.width='30vw';
        document.getElementsByTagName('body')[0].classList.add('overflow');
    },
    logout(){
        this.closeLogout();
        signOut(getAuth()).then(()=>{
            this.state='LOGIN';
            this.username='username';
            this.avatar='/assets/avatar.png';
            this.email='email id';
        });
     
    },
     googlesignup (){
        var provider = new GoogleAuthProvider();
         signInWithPopup(getAuth(), provider).then(function(result) {
            this.avatar = result.user.photoURL;
            this.username = result.user.displayName;
            this.email = result.user.email;
            document.getElementsByClassName('openprofile')[0].style.backgroundImage = 'url('+this.avatar+')';
        }).catch(function(error) {
            console.log(error);
        });
        this.state='LOGOUT';
        this.closepopup();
    },
    closepopup(){
        document.getElementsByClassName('login')[0].style.transform = 'translateY(100%)';
        document.getElementsByClassName('login')[0].style.opacity = '0';
        document.getElementsByClassName('login')[0].style.transform = 'scale(0)';
        document.getElementsByTagName('body')[0].classList.toggle('overflow');
    },

    // submit(){
    //     createUserWithEmailAndPassword(getAuth(),this.email,this.password).then(function(user){
    //         console.log(user);
           
    //     }).catch(function(error){
    //         console.log(error)
    //     })
    //     this.closepopup();


    // },
    login(){
        if(this.state=='LOGIN'){
        document.getElementsByClassName('login')[0].style.transform='translateY(0%)';
        document.getElementsByClassName('login')[0].style.opacity='1';
        document.getElementsByClassName('login')[0].style.transform = 'scale(1)';


        document.getElementsByTagName('body')[0].classList.toggle('overflow');
       this.closeprofile();
        }
        else{
            document.getElementsByClassName('logout')[0].style.transform = 'translateY(0%)';
            document.getElementsByClassName('logout')[0].style.opacity = '1';
            document.getElementsByClassName('logout')[0].style.transform = 'scale(1)';
            document.getElementsByTagName('body')[0].classList.toggle('overflow');
            this.closeprofile();
        }
    },
    toggle:function(){
        document.getElementsByClassName('container')[0].classList.toggle('change');
        document.getElementsByClassName('menu-bg')[0].classList.toggle('expand-bg');
        document.getElementsByTagName('body')[0].classList.toggle('overflow');
        document.getElementsByClassName('nav-menu')[0].classList.toggle('nav-menu-change');
    },
}
}
</script>