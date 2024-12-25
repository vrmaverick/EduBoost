import "./App.css";
import React, { useEffect, useState } from "react";

import Hero from "./components/Hero";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Summarization from "./components/Summarization";
import Login from "./components/Login";
import SignUp from "./components/Register";

import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { auth } from "./components/firebase";

function App() {
  const [user, setUser] = useState();
  useEffect(() => {
    auth.onAuthStateChanged((user) => {
      setUser(user);
    });
  });
  return (
    <>
      <Router>
        <Routes>
          <Route path="/register" element={<SignUp />} />
          <Route
            path="/"
            element={user ? <Navigate to="/hero" /> : <Login />}
          />
          <Route path="/login" element={<Login />} />
          <Route path="/hero" element={<Hero />} />
          <Route path="/summarization" element={<Summarization />} />
        </Routes>
        <ToastContainer />
      </Router>
    </>
  );
}

export default App;
