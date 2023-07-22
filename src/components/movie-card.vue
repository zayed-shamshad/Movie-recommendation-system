<template>
    <div class="movie-box">
            <poster :title="title" :link=links :review="overview">
            </poster>
        <div class="bottom-buttons">
            <div @click="addtofav" class="heart" v-bind:style="{ color: colorofheart }" v-if="user!=null || user!=undefined">❤</div>
        </div>
        </div>
</template>
<script setup>
import poster from './poster.vue'
import { computed, onMounted, ref } from 'vue'
import { defineProps } from 'vue'
import { useUserStore } from "../stores/store";
import { db } from '../firebase.js'
import { arrayUnion } from "firebase/firestore";
import { doc, updateDoc,setDoc, getDoc } from "firebase/firestore";

const props=defineProps({
    id:Number,
    title:String,
    overview:String,
    links:String
})
const userstore=useUserStore();
const user=ref(userstore.user);
const fav=ref([]);

const colorofheart=computed(()=>{
    if (fav.value.find((ID) => ID == props.id)) {
        color.value = "red";
    }
    else{
        color.value = "pink";
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
 onMounted(async ()=>{
    await getfav();
})


const addtofav=async()=>{
    console.log("i was clicked",props.id,props.title)
    if (user.value != null) {
         if (fav.value.find((ID) =>ID==props.id)) {
              color.value = "pink";
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
            color.value = "red";
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