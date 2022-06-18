import { initializeApp } from 'firebase/app'
import { getFirestore } from "firebase/firestore";
const firebaseConfig = {
    apiKey: "AIzaSyDfTT4ihp3HVEaH7dZ0YSijz36PRPFYFGU",
    authDomain: "movie-recommendation-7f0c5.firebaseapp.com",
    projectId: "movie-recommendation-7f0c5",
    storageBucket: "movie-recommendation-7f0c5.appspot.com",
    messagingSenderId: "281670996719",
    appId: "1:281670996719:web:aa2e5ae32628b7fc6c011a",
    measurementId: "G-LYD4L5N2HK"
};

const firebase= initializeApp(firebaseConfig);
const db = getFirestore(firebase);
export {db};

