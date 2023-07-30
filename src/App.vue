 <template>
    <div v-if="!isOnline " class="absolute z-50
            flex
            left-1/2
            transform -translate-x-1/2
             bg-red
             text-white
            shadow-2xl
            rounded-lg
            absolute
            p-4
            ">
        you are offline
    </div>
    
    <transition name="fade">
    <div v-if="state=='Login'" class="
            z-50
            flex 
            flex-col
            items-center
            justify-between
            fixed
            top-1/2
            left-1/2
            transform -translate-x-1/2 -translate-y-1/2
            w-3/4
            transition-all
            duration-200
            ease-in-out
            md:w-1/6
            h-1/6
            text-black
            bg-white
            shadow-2xl
            rounded-lg
            p-4
            ">
               <div class="text-sm md:text-xl lg:text-2xl">
                Sign In
               </div> 
               <div class="w-full flex flex-row justify-between items-center">
                    <button @click="state=''" class="bg-gray-700 text-white p-2
                     rounded-lg">
                        Close
                    </button>
                    <button  @click="googlesignup"
                    
                    >
                        <font-awesome-icon :icon='["fab","google"]'></font-awesome-icon>
                        Google Signup
                    </button>
              </div>
    </div>
    </transition>
    <transition name="fade" mode="out-in">
    <div v-if="state=='Logout'" class="
            z-50
            flex 
            flex-col
            items-center
            justify-between
            fixed
            top-1/2
            left-1/2
            transform -translate-x-1/2 -translate-y-1/2
            transition-all
            duration-200
            ease-in-out
            text-black
            bg-white
            w-3/4
            md:w-1/6
            h-1/6
            shadow-2xl
            rounded-lg
            p-4
            ">
        <h1>
            Logout ?
        </h1>
        <div class="w-full flex flex-row justify-between items-center">
            <button @click="logout">
                <font-awesome-icon icon="sign-out"></font-awesome-icon>
                Logout
            </button>
            <button @click="state=''">
                <font-awesome-icon icon="close"></font-awesome-icon>
                Cancel
            </button>
        </div>
    </div>
    </transition>
    <navbar 
    @changeState="openmenu"
    ></navbar>
    <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
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
        state:'',
        avatar:'./assets/avatar.png',
        store: useUserStore(),
        isOnline:false
    }
  }
,
created(){
    onAuthStateChanged(getAuth(), (user) => {
            console.log("state changed !")
            if (user) {
                this.store.setUser(user);
                console.log("user is still logged in")
            }
            else {
                console.log("user is logged out")
            }
        });
},
mounted(){
    this.isonline();

    // Add an event listener to check online status when the connection changes
    window.addEventListener('online', this.isonline);
    window.addEventListener('offline', this.isonline);
},
    beforeUnmount() {
        // Remove event listeners to avoid memory leaks
        window.removeEventListener('online', this.isonline);
        window.removeEventListener('offline', this.isonline);
    },
methods:{
    isonline() {
            this.isOnline= navigator.onLine;
            console.log(this.isOnline);
        },
    openmenu(state){
        this.state=state;
        console.log(this.state)
        console.log(state)
    }
    ,
    logout(){
        signOut(getAuth()).then(()=>{
            this.state = "";
            this.store.setUser(null);
        });
    },
     googlesignup (){
         var provider = new GoogleAuthProvider();
      
         signInWithPopup(getAuth(), provider).then(function(result) {
               this.store.setUser(result.user);
        }).catch(function(error) {
            console.log(error);
        });
        this.state="";
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
    transition: opacity .5s ease;
}

.fade-enter-from,
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

.list-enter-active,
.list-leave-active {
    transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
    opacity: 0;
    transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
    position: absolute;
}
</style>