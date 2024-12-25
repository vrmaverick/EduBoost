import { signInWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "./firebase";
import { toast } from "react-toastify";
import SignInwithGoogle from "./signInWIthGoogle";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(auth, email, password);
      console.log("User logged in Successfully");
      window.location.href = "/hero";
      toast.success("User logged in Successfully", {
        position: "top-center",
      });
    } catch (error) {
      console.log(error.message);

      toast.error(error.message, {
        position: "bottom-center",
      });
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <form
        onSubmit={handleSubmit}
        className="h-[750px] w-[600px] flex flex-col gap-5 items-center justify-center bg-white/5 rounded-lg shadow-lg shadow-[#79D7BE]/50"
      >
        <h3 className="font-bold text-4xl text-[#E2BFD9] mb-10">Login</h3>

        <div className="">
          <input
            type="email"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="Enter email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <input
            type="password"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <div className="d-grid">
          <button
            type="submit"
            className="text-white bg-[#E2BFD9]/30 border border-gray-300 focus:outline-red-400 hover:text-black hover:bg-[#E2BFD9]/60 focus:ring-4 hover:ring-4 font-medium rounded-full text-md py-2.5 w-[150px] mb-5"
          >
            Submit
          </button>
        </div>
        <p className="mb-3 text-lg">
          New user? <a href="/register" className="text-[#79D7BE]">Register Here</a>
        </p>
        <SignInwithGoogle />
      </form>
    </div>
  );
}

export default Login;
