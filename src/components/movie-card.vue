<template>
        <div class="bg-gray-900">
               
           <img class="h-5/6 object-cover w-full" :src="links" alt="Movie Poster">

            <div class="flex justify-around items-center h-1/6 flex-col w-full">
                <div class="h-1/2 px-2 text-sm md:text-lg text-white truncate w-full">{{ title.toUpperCase() }}</div>
               <div class="h-1/2 flex justify-between row items-center px-3 w-full">
                   <div class="cursor-pointer" @click="addtofav" v-if="computedUser != null || computedUser != undefined">
                    <div class="text-red-500 text-4xl transition-all hover:scale-150 active:scale-110">
                     <span class="text-xl md:text-4xl">{{ colorofheart ? '❤' : '♡' }}</span>
                    </div>
                 </div>
                   <div v-else>

                   </div>
                <button @click="showModall"  class="text-white hover:scale-110 text-sm md:text-lg">
                    Read More..
                </button>
            </div>
    </div>
      <Teleport to="body">
                <transition name="fade" appear>
                <div class="modal-overlay" v-if="showModal" @click="close"></div>
                </transition>
               <transition name="fade" appear>
                <div v-if="showModal" class="modal
                z-50
                fixed
                top-1/2
                left-1/2
                transform -translate-x-1/2 -translate-y-1/2
                md:w-3/4
                lg:w-1/2
                w-full
                bg-white
                shadow-2xl
                rounded-lg
                p-8
            ">
                <h1 class="
            text-2xl
            md:text-4xl
            font-bold
            text-gray-800

            ">{{ title }}</h1>
               <p class="text-sm md:text-lg
              mt-4
              text-gray-600
           ">{{ overview }}</p>
               <div class="flex flex-row justify-between">
          
               <button class="
              bg-gray-700
                text-white
                px-4
                py-2
                rounded-lg
                hover:bg-gray-900
                transition-all
                duration-200
                ease-in-out
                mt-4
                md:mt-8
           " @click="close">
                Close
               </button>
               <button  class="
                bg-gray-700
                text-white
                px-4
                py-2
                rounded-lg
                hover:bg-gray-900
                transition-all
                duration-200
                ease-in-out
                mt-4
                md:mt-8
           " @click="playTrailer">
                <font-awesome-icon icon="video" class=""></font-awesome-icon>
               </button>
             
                   </div>
               </div>
                </transition>
            </Teleport>

             <Teleport to="body">
                 <transition name="fade" appear>
                    <div class="modal-overlay" v-if="playVideo"></div>
                    </transition>
                      <transition name="fade" appear>
                    <div v-if="playVideo" class="flex
                 flex-col
                  items-center
                   justify-between
                    bg-white fixed
                     top-1/2 left-1/2
                      transform -translate-x-1/2 -translate-y-1/2 z-50
                          md:w-3/4
                            lg:w-1/2
                             w-full
                            shadow-2xl
                            h-1/2
                            md:h-3/4
                            rounded-lg
                      "
                      
                          >
                          <VueYtframe
                        ref="yt"
                        :video-id="trailerID"
                        @ready="onReady"
                        />
                   
                     <button class="
                  bg-gray-700
                text-white
                px-4
                py-2
                rounded-lg
                hover:bg-gray-900
                transition-all
                duration-200
                ease-in-out
                m-2
                 " @click="playVideo = false">
                    <font-awesome-icon icon="close" class=""></font-awesome-icon>
                   </button>
                    </div>
                    </transition>
            </Teleport>
</div>    
</template>
<script setup>
import { computed, onMounted, ref } from 'vue'
import { useUserStore } from "../stores/store";
import { db } from '../firebase.js'
import { arrayUnion } from "firebase/firestore";
import { doc, updateDoc,setDoc, getDoc } from "firebase/firestore";
import axios from "axios";
const props=defineProps({
    id:Number,
    title:String,
    overview:String,
    links:String
})
const userstore=useUserStore();
const user=ref(userstore.user);
const fav=ref([]);
const color=ref(false);
const showModal=ref(false);
const playVideo=ref(false);
const trailerID=ref("");

const onReady = function (event) {
    // access to player in all event handlers via event.target
    event.target.playVideo();
  }

const getTrailer = async () => {
    const response = await axios.get('https://movie-system-api.onrender.com/trailer?id='+props.id)
    trailerID.value =response.data.results.filter((video)=>video.type=="Trailer")[0].key;
}

const playTrailer=async function(){
    await getTrailer();
    showModal.value=false;
    playVideo.value=true;
}
const computedUser=computed(()=>{
    user.value=userstore.user;
    return user.value;
})

const colorofheart=computed(()=>{
    if (fav.value.find((ID) => ID == props.id)) {
        color.value = true;
    }
    else{
        color.value = false;
    }
    return color.value;   
   
})
const getfav=async()=>{
    if (user.value != null) {
        const docRef = doc(db, "users", user.value.email);
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) {
            if (docSnap.data().fav != undefined) {
                fav.value = docSnap.data().fav;
            }
        }
    }
    }

const showModall=function() {
        showModal.value = !showModal.value;
    }

const close=function() {
        showModal.value = false;
    }
 onMounted(async ()=>{
    await getfav();
    let Script = document.createElement("script");
    Script.setAttribute("src", "https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.7.2/vanilla-tilt.js");
    document.head.appendChild(Script);

})
const addtofav=async()=>{
    console.log("i was clicked",props.id,props.title)
    if (user.value != null) {
         if (fav.value.find((ID) =>ID==props.id)) {
              color.value = false;
                fav.value =fav.value.filter((id) => {
                return id != props.id;
            })
            await setDoc(doc(db, "users", user.value.email)
                , {
                    fav: fav.value
                }
            );
           
         }
         else{
            color.value = true;
            await updateDoc(
                doc(db, "users", user.value.email),
                {
                    fav:arrayUnion(props.id)
                }
           )
        }
        await getfav();
    }
}

</script>
<style>
.modal-overlay {
z-index: 40;
 position: fixed;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 background-color: rgba(0, 0, 0, 0.3);
} 

</style>