import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { auth, db } from "./firebase";
import { toast } from "react-toastify";
import { setDoc, doc } from "firebase/firestore";
import Google from "../assets/google_logo.svg";

function SignInwithGoogle() {
  function googleLogin() {
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider).then(async (result) => {
      console.log(result);
      const user = result.user;
      if (result.user) {
        await setDoc(doc(db, "Users", user.uid), {
          email: user.email,
          firstName: user.displayName,
          photo: user.photoURL,
          lastName: "",
        });
        toast.success("User logged in Successfully", {
          position: "top-center",
        });
        window.location.href = "/hero";
      }
    });
  }
  return (
    <>
      <p className="">--Or continue with--</p>
      <div
        style={{ display: "flex", justifyContent: "center", cursor: "pointer" }}
        onClick={googleLogin}
      >
        <div className="bg-white rounded-full w-[250px] py-2 flex gap-2 items-center justify-center text-sm text-gray-700 outline hover:outline-[#79D7BE] hover:scale-105">
          <img src={Google} width={"30px"} />
          <p>Continue with Google</p>
        </div>
      </div>
    </>
  );
}
export default SignInwithGoogle;
