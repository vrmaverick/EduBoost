// import { createUserWithEmailAndPassword } from "firebase/auth";
// import React, { useState } from "react";
// import { auth, db } from "./firebase";
// import { setDoc, doc } from "firebase/firestore";
// import { toast } from "react-toastify";
// import { useNavigate } from "react-router-dom";

// function Register() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [fname, setFname] = useState("");
//   const [lname, setLname] = useState("");
//   const navigate = useNavigate();

//   const handleRegister = async (e) => {
//     e.preventDefault();
//     try {
//       await createUserWithEmailAndPassword(auth, email, password);
//       const user = auth.currentUser;
//       console.log(user);
//       if (user) {
//         await setDoc(doc(db, "Users", user.uid), {
//           email: user.email,
//           firstName: fname,
//           lastName: lname,
//           photo: "",
//         });
//       }
//       console.log("User Registered Successfully!!");
//       toast.success("User Registered Successfully!!", {
//         position: "bottom-center",
//       });
//       navigate("/login");
//     } catch (error) {
//       console.log(error.message);
//       toast.error(error.message, {
//         position: "bottom-center",
//       });
//     }
//   };

//   return (
//     <div className="flex items-center justify-center h-screen">
//       <form
//         onSubmit={handleRegister}
//         className="h-[750px] w-[600px] flex flex-col gap-5 items-center justify-center bg-white/5 rounded-lg shadow-lg shadow-[#79D7BE]/50"
//       >
//         <h3 className="font-bold text-4xl text-[#E2BFD9] mb-10">Sign Up</h3>

//         <div className="mb-3">
//           <input
//             type="text"
//             className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
//             placeholder="First name"
//             onChange={(e) => setFname(e.target.value)}
//             required
//           />
//         </div>

//         <div className="mb-3">
//           <input
//             type="text"
//             className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
//             placeholder="Last name"
//             onChange={(e) => setLname(e.target.value)}
//           />
//         </div>

//         <div className="mb-3">
//           <input
//             type="email"
//             className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
//             placeholder="Enter email"
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//         </div>

//         <div className="mb-3">
//           <input
//             type="password"
//             className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
//             placeholder="Enter password"
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </div>

//         <div className="d-grid">
//           <button
//             type="submit"
//             className="text-white bg-[#E2BFD9]/30 border border-gray-300 focus:outline-red-400 hover:text-black hover:bg-[#E2BFD9]/60 focus:ring-4 hover:ring-4 font-medium rounded-full text-md py-2.5 w-[150px] mb-5"
//           >
//             Sign Up
//           </button>
//         </div>
//         <p className="mb-3 text-lg">
//           Already registered?{" "}
//           <a href="/login" className="text-[#79D7BE]">
//             Login
//           </a>
//         </p>
//       </form>
//     </div>
//   );
// }
// export default Register;


import { createUserWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth, db } from "./firebase";
import { setDoc, doc } from "firebase/firestore";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom"; // Import useNavigate

function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const navigate = useNavigate(); // Initialize useNavigate

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      const user = auth.currentUser;
      console.log(user);
      if (user) {
        await setDoc(doc(db, "Users", user.uid), {
          email: user.email,
          firstName: fname,
          lastName: lname,
          photo: ""
        });
      }

      // Redirect to login page
      navigate("/login");
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
        onSubmit={handleRegister}
        className="h-[750px] w-[600px] flex flex-col gap-5 items-center justify-center bg-white/5 rounded-lg shadow-lg shadow-[#79D7BE]/50"
      >
        <h3 className="font-bold text-4xl text-[#E2BFD9] mb-10">Sign Up</h3>

        <div className="mb-3">
          <input
            type="text"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="First name"
            onChange={(e) => setFname(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <input
            type="text"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="Last name"
            onChange={(e) => setLname(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <input
            type="email"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="Enter email"
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <input
            type="password"
            className="bg-transparent/5 border outline-gray-300 text-md rounded-lg focus:ring-[#E2BFD9]/90 focus:outline-[#E2BFD9] block p-2.5 w-[400px]"
            placeholder="Enter password"
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <div className="d-grid">
          <button
            type="submit"
            className="text-white bg-[#E2BFD9]/30 border border-gray-300 focus:outline-red-400 hover:text-black hover:bg-[#E2BFD9]/60 focus:ring-4 hover:ring-4 font-medium rounded-full text-md py-2.5 w-[150px] mb-5"
          >
            Sign Up
          </button>
        </div>
        <p className="mb-3 text-lg">
          Already registered? <a href="/login" className="text-[#79D7BE]">Login</a>
        </p>
      </form>
    </div>
  );
}

export default Register;
