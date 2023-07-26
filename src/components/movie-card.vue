<template>
        <div class="bg-gray-900">
               
           <img class="h-5/6 object-cover w-full" :src="links" alt="Movie Poster">

            <div class="flex justify-around items-center h-1/6 flex-col w-full">
                <div class="flex justify-center items-center text-center text-lg  text-white font-semibold">{{ title.toUpperCase() }}</div>
                 
               <div class="flex justify-between row items-center px-3 w-full">
                
                   <div class="cursor-pointer" @click="addtofav" v-if="user != null || user != undefined">
                    <div class="text-red-500 text-4xl transition-all hover:scale-150 active:scale-110">
                     <span class="text-xl md:text-4xl">{{ colorofheart ? '❤' : '♡' }}</span>
                    </div>
                 </div>
                   <div v-else>

                   </div>
                <button @click="showModall"  class="text-white hover:scale-110">
                    Read More..
                </button>
            </div>
            </div>
            </div>
      
         <Teleport to="body">
            <transition name="fade" appear>
            <div class="modal-overlay" v-if="showModal"></div>
            </transition>
           <transition name="slide" appear>
            <div v-if="showModal" class="modal">
            <h1>{{ title }}</h1>
           <p>{{ overview }}</p>
           <button class="but" @click="close">
            Close
           </button>
           <button  class="but" @click="playTrailer">
            watch trailer
           </button>
           </div>
            </transition>
        </Teleport>

         <Teleport to="body">
             <transition name="fade" appear>
                <div class="modal-overlay" v-if="showModal"></div>
                </transition>
                  <transition name="slide" appear>
                <div v-if="playVideo" class="modal">
                 <YouTube 
                src="https://www.youtube.com/watch?v=jNQXAC9IVRw" 
                @ready="onReady"
                ref="youtube" />
                 <button class="but" @click="playVideo=false">
                Close
               </button>
                </div>
                </transition>
        </Teleport>
          
</template>
<script setup>
import { computed, onMounted, ref } from 'vue'
import { useUserStore } from "../stores/store";
import { db } from '../firebase.js'
import { arrayUnion } from "firebase/firestore";
import { doc, updateDoc,setDoc, getDoc } from "firebase/firestore";
import YouTube from 'vue3-youtube'
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

const onReady = function (event) {
    // access to player in all event handlers via event.target
    event.target.playVideo();
  }

const playTrailer=function(){
    showModal.value=false;
    playVideo.value=true;
}

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
 .but{
    background-color: #222;
    color: #FFF;
    border: none;
    padding: 10px;
    border-radius: 16px;
    font-size: 16px;
    font-weight: 900;
    cursor: pointer;
    margin-top: 15px;
 }
 

</style>