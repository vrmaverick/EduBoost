"use client";

import Colorization from "./Colorization";
import Navbar from "./Navbar";

export default function Example() {
  return (
    <>
      <div className="text-[#c6d6d5] h-[100vh]">
        <Navbar />

        <div className="relative isolate px-6 pt-14 lg:px-8 flex items-center justify-center h-screen">
          <div className="flex flex-col items-center justify-center">
            <h2 className="text-5xl text-[#E2BFD9] font-semibold drop-shadow-lg">
              Welcome to EduBoost – Revolutionizing Education with AI
            </h2>
            <p className="mt-16 text-xl flex flex-col gap-10">
              EduBoost is an innovative platform designed to transform education
              through cutting-edge AI tools. Empowering both students and
              teachers, EduBoost offers:
              <ul className="flex flex-col gap-5 items-center">
                <li className="">
                  <b className="text-[#00A8CC]">Image Summarizer:</b> Extract
                  key information effortlessly.
                </li>
                <li className="">
                  <b className="text-[#00A8CC]">Image Colorizer:</b> Bring
                  visuals to life with AI-enhanced colors.
                </li>
                <li className="">
                  <b className="text-[#00A8CC]">Image Generator:</b> Create
                  visuals tailored to your learning needs.
                </li>
                <li className="">
                  <b className="text-[#00A8CC]">Gesture-Based AI Calculator:</b>{" "}
                  Solve math problems interactively.
                </li>
              </ul>
              With AI at its core, EduBoost enhances engagement, provides
              real-time feedback, and supports personalized learning
              experiences. Join the future of education with EduBoost!
            </p>
          </div>

          <div
            aria-hidden="true"
            className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
          >
            <div
              style={{
                clipPath:
                  "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
              }}
              className="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#00A8CC] to-[#0C7B93] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
            />
          </div>
        </div>
      </div>
      <div id="section1">
        <Colorization />
      </div>
    </>
  );
}
