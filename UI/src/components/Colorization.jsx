import React from "react";
import { useState } from "react";
import { MdCloudUpload, MdDelete } from "react-icons/md";
import { AiFillFileImage } from "react-icons/ai";
import "./colorization.css";

const Colorization = () => {
  const [image, setImage] = useState(null);
  const [fileName, setFileName] = useState("No selected file");

  return (
    <>
      <div className="flex flex-col items-center justify-center h-screen m-10">
        <h1 className="text-4xl font-semibold text-[#E2BFD9]">
          Image Colorization
        </h1>
        <div className="flex flex-row items-center justify-evenly gap-10">
          <div>
            <div className="flex gap-10">
              <form
                onClick={() => document.querySelector(".input-field").click()}
                className="mt-10 form-colorize"
              >
                <input
                  type="file"
                  accept="image/*"
                  className="input-field"
                  hidden
                  onChange={({ target: { files } }) => {
                    files[0] && setFileName(files[0].name);
                    if (files) {
                      setImage(URL.createObjectURL(files[0]));
                    }
                  }}
                />

                {image ? (
                  <img src={image} width={700} height={550} alt={fileName} />
                ) : (
                  <>
                    <MdCloudUpload color="#1475cf" size={60} />
                    <p>Browse Files to upload</p>
                  </>
                )}
              </form>
            </div>
          </div>
          <div>
            <form
              
              className="mt-10 form-colorize"
            >
              <output
                className="input-field"
                hidden
                
              />

              <p className="font-semibold text-2xl">Output</p>
            </form>
          </div>
        </div>
        <section className="uploaded-row">
          <AiFillFileImage color="#1475cf" />
          {fileName} -
          <MdDelete
            onClick={() => {
              setFileName("No selected File");
              setImage(null);
            }}
          />
          <span className="upload-content"></span>
          <button
            type="submit"
            className="px-5 py-2 bg-slate-700/70 rounded-md outline outline-[#E2BFD9] text-white hover:scale-110 hover:outline-[#E2BFD9]/70 hover:bg-[#ffe5f8] hover:text-[#000]"
          >
            Colorize
          </button>
        </section>
      </div>
    </>
  );
};

export default Colorization;

