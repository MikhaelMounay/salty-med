// import firebase from "firebase";
// import "firebase/database";
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyDmzEUgMieIOq1lqzRgbWOztIECXSuHCNs",
  authDomain: "salty-mediterranean.firebaseapp.com",
  databaseURL:
    "https://salty-mediterranean-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "salty-mediterranean",
  storageBucket: "salty-mediterranean.appspot.com",
  messagingSenderId: "1013315367632",
  appId: "1:1013315367632:web:3c46078864e93a2e7424d5",
  measurementId: "G-92VYY9C3PW",
};

const firebaseApp = initializeApp(firebaseConfig);

// export default firebase.database();
export default firebaseApp;
