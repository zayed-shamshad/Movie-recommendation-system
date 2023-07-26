 <template>
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
        SIGN In
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
    <navbar 
    :user="store.user"
    ></navbar>
    <router-view v-slot="{ Component }">
        <transition name="fade">
            <component :is="Component" />
        </transition>
    </router-view>
    <foot></foot>
</template> 


<script>
import {getAuth} from 'firebase/auth';
import {GoogleAuthProvider,signInWithPopup} from 'firebase/auth';
import {onAuthStateChanged,signOut} from 'firebase/auth';
import { useUserStore } from './stores/store.js'
import footer from './components/footer.vue'
import navbar from './components/navbar.vue'
export default{
  name:'App',
  components:{
  'foot':footer,
    'navbar':navbar
},
  data() {
      return{
        email:'email id',
        username:'username',
        state:'LOGIN',
        avatar:'./assets/avatar.png',
        store:useUserStore(),
    }
  }
,
created(){
    onAuthStateChanged(getAuth(), (user) => {
            console.log("state changed !")
            if (user) {
                this.store.setUser(user);
                console.log("user is still logged in")
                this.state = 'LOGOUT';
                this.username = user.displayName;
                this.avatar = user.photoURL;
                this.email = user.email;
            }
            else {
                console.log("user is logged out")
                this.state = 'LOGIN';
                this.avatar = './assets/avatar.png';
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
        document.getElementsByClassName('profile')[0].style.width='90vw';
        document.getElementsByTagName('body')[0].classList.add('overflow');
    },
    logout(){
        this.closeLogout();
        this.store.setUser(null);
        signOut(getAuth()).then(()=>{
            this.state='LOGIN';
            this.username='username';
            this.avatar='./assets/avatar.png';
            this.email='email id';
        });
     
    },
     googlesignup (){
        var provider = new GoogleAuthProvider();
         signInWithPopup(getAuth(), provider).then(function(result) {
            this.store.setUser(result.user);
            this.avatar = result.user.photoURL;
            this.username = result.user.displayName;
            this.email = result.user.email;
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
}
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Limelight&display=swap');


.footerlink {
    color: white;
    text-decoration: none;
}

/* we will explain what these classes do next! */
.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

.username {
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

.username:hover {
    transform: scale(1.1);
}

.profileheader {
    width: 300px;
    height: 85vh;
    background-color: transparent;
    z-index: 100;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    font-size: 1rem;
}

.icons {
    margin-right: 10px;
}

.profile {
    position: fixed;
    width: 0vw;
    left: 0px;
    top: 0vh;
    ;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    z-index: 25;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-size: 10px;
    transition: all 0.25s ease-in-out;
    overflow-x: hidden;
}

.closeprofile {
    width: 20px;
    top: 3px;
    right: 5px;
    font-size: 20px;
    color: #fff;
    cursor: pointer;
    position: absolute;
}

.closeprofile:hover {
    color: red;
    transform: translate(0, 0) scale(1.1);
}


.logout {
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

.logout div:first-child {
    display: flex;
    font-size: 1.3rem;
    border-bottom: rgb(0, 0, 0) solid 1px;

    justify-content: space-evenly;
}

.logout button {
    background: rgb(255, 255, 255);
    border: none;
    border-radius: 20px;
    padding: 10px;
    font-size: 20px;
    margin-right: 10px;
    font-family: 'Cairo', sans-serif;
    color: black;
    transition: all 0.2s ease-in-out;
    cursor: pointer;
}

.logout button:hover {
    border: none;
    border-radius: 20px;
    padding: 10px;
    font-size: 20px;
    font-family: 'Cairo', sans-serif;
    color: red;
    cursor: pointer;
}

.login {
    width: 30vw;
    position: absolute;
    z-index: 20;
    height: 30vh;
    top: 30vh;
    left: 35vw;
    background: rgb(255, 255, 255);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 20px;
    transform: translateY(100%);
    transition: all 0.3s ease-in-out;
    opacity: 0;
    transform: scale(0);
    color: black;
}

.login input {
    width: 20vw;
    padding: 10px;
    font-size: 17px;
    font-family: 'Cairo', sans-serif;
    border: none;
    border-bottom: 2px solid black;
}

.login input:focus {
    border-bottom: 2px solid green;
    outline: none;
}

.submit-button {
    width: 20vw;
    letter-spacing: 10px;
    border-radius: 20px;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    font-size: 17px;
    font-family: 'Cairo', sans-serif;
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    border: 1px solid rgb(0, 0, 0);
    transition: all 0.2s ease-in-out;
}

.google-button {
    width: 20vw;
    letter-spacing: 2px;
    border-radius: 20px;
    padding: 10px;
    font-size: 17px;
    font-family: 'Cairo', sans-serif;
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    border: 1px solid rgb(0, 0, 0);
    transition: all 0.2s ease-in-out;
}

.close-popup {
    position: absolute;
    top: 0;
    right: 0;
    width: 10px;
    padding: 10px;
    height: 10px;
    border-radius: 300px;
    background: rgb(255, 255, 255);
    z-index: 10;
    cursor: pointer;
    color: black;
}

.login button:hover {
    background: rgb(0, 0, 0);
    color: rgb(255, 255, 255);
}

body {
    font-family: 'Cairo', sans-serif;
    background: linear-gradient(to right, rgba(71, 202, 231, 0.5), rgba(43, 200, 124, 0.5), rgba(112, 233, 25, 0.5)), url('/assets/mp.jpg');
    background-repeat: no-repeat;
    z-index: -1;
    background-size: cover;
    background-attachment: fixed;
    width: 100vw;
    height: 100vh;
    color: white;
    position: absolute;
}

* {
    margin: 0;
    padding: 0;
}

::-webkit-scrollbar {
    display: none;
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