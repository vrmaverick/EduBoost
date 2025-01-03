import React, { useRef, useState } from "react";
import { Stage, Layer, Line } from "react-konva";
import { MdDelete } from "react-icons/md";
import "./summarization.css";
import Navbar from "./Navbar";

const ScratchPad = () => {
  const [lines, setLines] = useState([]);
  const [outputImage, setOutputImage] = useState(null);
  const stageRef = useRef();

  const handleMouseDown = (e) => {
    const pos = e.target.getStage().getPointerPosition();
    setLines([...lines, { points: [pos.x, pos.y] }]);
  };

  const handleMouseMove = (e) => {
    if (lines.length === 0) return;

    const stage = e.target.getStage();
    const point = stage.getPointerPosition();
    const lastLine = lines[lines.length - 1];
    lastLine.points = lastLine.points.concat([point.x, point.y]);
    setLines([...lines.slice(0, -1), lastLine]);
  };

  const handleCalculate = () => {
    const uri = stageRef.current.toDataURL();
    setOutputImage(uri);
  };

  const handleClear = () => {
    setLines([]);
    setOutputImage(null);
  };

  return (
    <>
      <Navbar />
      <div className="flex flex-col items-center justify-center h-screen m-10">
        <h1 className="text-4xl font-semibold text-[#E2BFD9]">Scratch Pad</h1>
        <div className="flex flex-row items-center justify-evenly gap-10 mt-10">
          {/* Drawing Canvas */}
          <div>
            <div className="canvas-container border border-gray-400 rounded-lg">
              <Stage
                width={500}
                height={500}
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                ref={stageRef}
                style={{ background: "#f0f0f0", cursor: "crosshair" }}
              >
                <Layer>
                  {lines.map((line, i) => (
                    <Line
                      key={i}
                      points={line.points}
                      stroke="#1475cf"
                      strokeWidth={3}
                      tension={0.5}
                      lineCap="round"
                    />
                  ))}
                </Layer>
              </Stage>
            </div>
            <button
              onClick={handleClear}
              className="mt-5 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
            >
              Clear
            </button>
          </div>

          {/* Output Area */}
          <div>
            <div className="output-container border border-gray-400 rounded-lg p-5">
              <h2 className="font-semibold text-2xl">Output</h2>
              {outputImage ? (
                <img
                  src={outputImage}
                  alt="Output"
                  className="mt-5 border border-gray-300"
                  width={500}
                  height={500}
                />
              ) : (
                <p className="text-gray-500 mt-5">No output yet</p>
              )}
            </div>
            <button
              onClick={handleCalculate}
              className="mt-5 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              Calculate
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default ScratchPad;
