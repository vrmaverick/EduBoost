// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getAuth} from "firebase/auth";
import {getFirestore} from "firebase/firestore";
// import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDMYRoakZZkrp3Sd_PmsS5tiI01yblJn0w",
  authDomain: "eduboost-login.firebaseapp.com",
  projectId: "eduboost-login",
  storageBucket: "eduboost-login.firebasestorage.app",
  messagingSenderId: "670030960795",
  appId: "1:670030960795:web:64c905c4b41dccbbbe0e3e",
//   measurementId: "G-PW3B779RNE"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
export const auth=getAuth();
export const db=getFirestore(app);
export default app;