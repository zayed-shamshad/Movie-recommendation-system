import { createApp } from 'vue'
import router from './router/index.js'
import App from './App.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
// import {initializeApp} from 'firebase/app'
// import { getFirestore } from "firebase/firestore";

const app = createApp(App)
library.add(fas, fab)
// const firebaseConfig = {
//     apiKey: "AIzaSyDfTT4ihp3HVEaH7dZ0YSijz36PRPFYFGU",
//     authDomain: "movie-recommendation-7f0c5.firebaseapp.com",
//     projectId: "movie-recommendation-7f0c5",
//     storageBucket: "movie-recommendation-7f0c5.appspot.com",
//     messagingSenderId: "281670996719",
//     appId: "1:281670996719:web:aa2e5ae32628b7fc6c011a",
//     measurementId: "G-LYD4L5N2HK"
// };

// const firebaseapp=initializeApp(firebaseConfig);
// const db = getFirestore(firebaseapp);
app.use()
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
