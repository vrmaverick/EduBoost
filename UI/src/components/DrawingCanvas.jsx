// import { useState, useEffect, useRef } from 'react';
// import { Pencil, Eraser, Undo, Redo, Save, Share2, Trash2, Grid, Calculator } from 'lucide-react';
// import { HexColorPicker } from "react-colorful";

// const DrawingCanvas = () => {
//   const canvasRef = useRef(null);
//   const [isDrawing, setIsDrawing] = useState(false);
//   const [tool, setTool] = useState('pen');
//   const [ctx, setCtx] = useState(null);
//   const [lastX, setLastX] = useState(0);
//   const [lastY, setLastY] = useState(0);
//   const [penSize, setPenSize] = useState(5);
//   const [eraserSize, setEraserSize] = useState(20);
//   const [penColor, setPenColor] = useState('#000F55');
//   const [undoStack, setUndoStack] = useState([]);
//   const [redoStack, setRedoStack] = useState([]);
//   const [showGrid, setShowGrid] = useState(false);
//   const [showColorPicker, setShowColorPicker] = useState(false);
//   const [isSolving, setIsSolving] = useState(false);
//   const [result, setResult] = useState('');

//   useEffect(() => {
//     const canvas = canvasRef.current;
//     const context = canvas.getContext('2d');
    
//     const setCanvasSize = () => {
//       canvas.width = window.innerWidth;
//       canvas.height = window.innerHeight - 60;
//       context.strokeStyle = penColor;
//       context.lineJoin = 'round';
//       context.lineCap = 'round';
//       context.lineWidth = tool === 'pen' ? penSize : eraserSize;
//       if (showGrid) drawGrid(context);
//     };

//     setCanvasSize();
//     setCtx(context);
//     saveToUndoStack();

//     window.addEventListener('resize', setCanvasSize);
//     return () => window.removeEventListener('resize', setCanvasSize);
//   }, []);

//   useEffect(() => {
//     if (ctx) {
//       ctx.strokeStyle = tool === 'pen' ? penColor : '#ffffff';
//       ctx.lineWidth = tool === 'pen' ? penSize : eraserSize;
//     }
//   }, [tool, penColor, penSize, eraserSize, ctx]);

//   const drawGrid = (context) => {
//     const canvas = canvasRef.current;
//     const gridSize = 20;
    
//     context.save();
//     context.strokeStyle = '#ddd';
//     context.lineWidth = 0.5;

//     for (let x = 0; x <= canvas.width; x += gridSize) {
//       context.beginPath();
//       context.moveTo(x, 0);
//       context.lineTo(x, canvas.height);
//       context.stroke();
//     }

//     for (let y = 0; y <= canvas.height; y += gridSize) {
//       context.beginPath();
//       context.moveTo(0, y);
//       context.lineTo(canvas.width, y);
//       context.stroke();
//     }

//     context.restore();
//   };

//   const saveToUndoStack = () => {
//     const canvas = canvasRef.current;
//     setUndoStack(prev => [...prev, canvas.toDataURL()]);
//     setRedoStack([]); // Clear redo stack when new action is performed
//   };

//   const handleUndo = () => {
//     if (undoStack.length > 1) {
//       const prevState = undoStack[undoStack.length - 2];
//       const img = new Image();
//       img.src = prevState;
//       img.onload = () => {
//         ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
//         ctx.drawImage(img, 0, 0);
//         if (showGrid) drawGrid(ctx);
//       };
      
//       setRedoStack(prev => [...prev, undoStack[undoStack.length - 1]]);
//       setUndoStack(prev => prev.slice(0, -1));
//     }
//   };

//   const handleRedo = () => {
//     if (redoStack.length > 0) {
//       const nextState = redoStack[redoStack.length - 1];
//       const img = new Image();
//       img.src = nextState;
//       img.onload = () => {
//         ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
//         ctx.drawImage(img, 0, 0);
//         if (showGrid) drawGrid(ctx);
//       };
      
//       setUndoStack(prev => [...prev, nextState]);
//       setRedoStack(prev => prev.slice(0, -1));
//     }
//   };

//   const clearCanvas = () => {
//     if (ctx) {
//       ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
//       if (showGrid) drawGrid(ctx);
//       saveToUndoStack();
//     }
//   };

//   const saveCanvas = () => {
//     const link = document.createElement('a');
//     link.download = 'math-notes.png';
//     link.href = canvasRef.current.toDataURL();
//     link.click();
//   };

//   const shareCanvas = () => {
//     canvasRef.current.toBlob((blob) => {
//       const file = new File([blob], 'math-notes.png', { type: 'image/png' });
//       if (navigator.share && navigator.canShare({ files: [file] })) {
//         navigator.share({
//           files: [file],
//           title: 'Math Notes',
//         });
//       } else {
//         saveCanvas();
//       }
//     });
//   };

//   const solveEquations = async () => {
//     try {
//       setIsSolving(true);
//       setResult(''); // Clear previous result
//       const canvas = canvasRef.current;
      
//       // Convert canvas to base64
//       const base64Image = canvas.toDataURL('image/png').split(',')[1];
  
//       const response = await fetch('http://localhost:3001/api/solve', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({
//           image: base64Image
//         }),
//       });
  
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
  
//       const data = await response.json();
      
//       // Display result from Gemini
//       if (data.result) {
//         setResult(data.result); // Set new result
//       } else {
//         alert('No solution provided. Please try again.');
//       }
//     } catch (error) {
//       console.error('Error solving equations:', error);
//       alert('Failed to solve equations. Please try again.');
//     } finally {
//       setIsSolving(false);
//     }
//   };

//   const startDrawing = (e) => {
//     e.preventDefault();
//     const rect = canvasRef.current.getBoundingClientRect();
//     const x = (e.clientX || e.touches[0].clientX) - rect.left;
//     const y = (e.clientY || e.touches[0].clientY) - rect.top;
    
//     setIsDrawing(true);
//     setLastX(x);
//     setLastY(y);
//   };

//   const draw = (e) => {
//     if (!isDrawing) return;
//     e.preventDefault();

//     const rect = canvasRef.current.getBoundingClientRect();
//     const x = (e.clientX || e.touches[0].clientX) - rect.left;
//     const y = (e.clientY || e.touches[0].clientY) - rect.top;

//     ctx.beginPath();
//     ctx.moveTo(lastX, lastY);
//     ctx.lineTo(x, y);
//     ctx.stroke();

//     setLastX(x);
//     setLastY(y);
//   };

//   const stopDrawing = () => {
//     if (isDrawing) {
//       setIsDrawing(false);
//       saveToUndoStack();
//     }
//   };

//   return (
//     <div className="flex flex-col h-screen">
//       <div className="flex justify-between p-4 bg-gray-100">
//         {/* Left section - Undo/Redo */}
//         <div className="flex gap-2">
//           <button
//             className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
//             onClick={handleUndo}
//             title="Undo"
//           >
//             <Undo className="w-6 h-6" />
//           </button>
//           <button
//             className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
//             onClick={handleRedo}
//             title="Redo"
//           >
//             <Redo className="w-6 h-6" />
//           </button>
//         </div>

//         {/* Center section - Tools */}
//         <div className="flex gap-4">
//           <button
//             className={`p-2 rounded-lg ${tool === 'pen' ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
//             onClick={() => setTool('pen')}
//             title="Pen"
//           >
//             <Pencil className="w-6 h-6" />
//           </button>
//           <button
//             className={`p-2 rounded-lg ${tool === 'eraser' ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
//             onClick={() => setTool('eraser')}
//             title="Eraser"
//           >
//             <Eraser className="w-6 h-6" />
//           </button>
//           <button
//             className={`p-2 rounded-lg ${showGrid ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
//             onClick={() => setShowGrid(!showGrid)}
//             title="Toggle Grid"
//           >
//             <Grid className="w-6 h-6" />
//           </button>
//           <button
//             className={`p-2 rounded-lg ${isSolving ? 'bg-gray-400' : 'bg-gray-200 hover:bg-gray-300'}`}
//             onClick={solveEquations}
//             disabled={isSolving}
//             title="Solve Equations"
//           >
//             <Calculator className="w-6 h-6" />
//           </button>
//         </div>

//         {/* Right section - Save/Share/Delete */}
//         <div className="flex gap-2">
//           <button
//             className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
//             onClick={saveCanvas}
//             title="Save"
//           >
//             <Save className="w-6 h-6" />
//           </button>
//           <button
//             className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
//             onClick={shareCanvas}
//             title="Share"
//           >
//             <Share2 className="w-6 h-6" />
//           </button>
//           <button
//             className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
//             onClick={clearCanvas}
//             title="Clear"
//           >
//             <Trash2 className="w-6 h-6" />
//           </button>
//         </div>
//       </div>

//       {/* Add Results Display */}
//       <div className="fixed top-20 right-4 p-4 bg-white rounded-lg shadow-lg max-w-xs">
//         {result && (
//           <p className="text-sm text-gray-800">{result}</p>
//         )}
//       </div>

//       {/* Side controls */}
//       <div className="fixed left-4 top-1/2 transform -translate-y-1/2 flex flex-col gap-4 bg-white p-4 rounded-lg shadow-lg">
//         <button
//           className="w-8 h-8 rounded-full bg-gray-200 hover:bg-gray-300"
//           onClick={() => setShowColorPicker(!showColorPicker)}
//           title="Color Picker"
//           style={{ backgroundColor: penColor }}
//         />
//         {showColorPicker && (
//           <div className="absolute top-12 left-0 z-10">
//             <HexColorPicker color={penColor} onChange={setPenColor} />
//           </div>
//         )}
//       </div>

//       <div className="fixed right-4 top-1/2 transform -translate-y-1/2">
//         <div className="p-2 bg-white shadow-lg rounded-xl border-2 border-gray-300">
//           <div className="relative h-64 w-12 bg-gray-200 rounded-lg overflow-hidden">
//             <input
//               type="range"
//               min={tool === 'pen' ? "1" : "10"}
//               max={tool === 'pen' ? "20" : "50"}
//               value={tool === 'pen' ? penSize : eraserSize}
//               onChange={(e) => {
//                 if (tool === 'pen') {
//                   setPenSize(parseInt(e.target.value));
//                 } else {
//                   setEraserSize(parseInt(e.target.value));
//                 }
//               }}
//               className="absolute w-64 h-12 -rotate-90 -translate-x-28 translate-y-28 appearance-none bg-transparent cursor-pointer outline-none"
//               style={{
//                 WebkitAppearance: 'none',
//                 MozAppearance: 'none',
//                 '&::-webkit-slider-thumb': {
//                   WebkitAppearance: 'none',
//                   appearance: 'none'
//                 },
//                 '&::-moz-range-thumb': {
//                   appearance: 'none'
//                 },
//                 '&::-webkit-slider-runnable-track': {
//                   background: 'transparent'
//                 },
//                 '&::-moz-range-track': {
//                   background: 'transparent'
//                 }
//               }}
//             />
//             <div 
//               className="absolute bottom-0 left-0 right-0 border bg-gray-400"
//               style={{
//                 height: `${((tool === 'pen' ? penSize : eraserSize) - (tool === 'pen' ? 1 : 10)) / 
//                         (tool === 'pen' ? 19 : 40) * 100}%`
//               }}
//             />
//             <div 
//               className="absolute w-12 h-6 bg-white rounded-md shadow-md -translate-x-0 transform cursor-pointer pointer-events-none border border-gray-300"
//               style={{
//                 top: `calc(${100 - ((tool === 'pen' ? penSize : eraserSize) - (tool === 'pen' ? 1 : 10)) / 
//                       (tool === 'pen' ? 19 : 40) * 100}% - 12px)`
//               }}
//             />
//           </div>
//         </div>
//       </div>
      
//       <canvas
//         ref={canvasRef}
//         className="flex-1 bg-white cursor-crosshair touch-none"
//         onMouseDown={startDrawing}
//         onMouseMove={draw}
//         onMouseUp={stopDrawing}
//         onMouseOut={stopDrawing}
//         onTouchStart={startDrawing}
//         onTouchMove={draw}
//         onTouchEnd={stopDrawing}
//       />
//     </div>
//   );
// };

// export default DrawingCanvas;

import { useState, useEffect, useRef } from 'react';
import { Pencil, Eraser, Undo, Redo, Save, Share2, Trash2, Grid, Calculator } from 'lucide-react';
import { HexColorPicker } from "react-colorful";

const DrawingCanvas = () => {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [tool, setTool] = useState('pen');
  const [ctx, setCtx] = useState(null);
  const [lastX, setLastX] = useState(0);
  const [lastY, setLastY] = useState(0);
  const [penSize, setPenSize] = useState(5);
  const [eraserSize, setEraserSize] = useState(20);
  const [penColor, setPenColor] = useState('#000F55');
  const [undoStack, setUndoStack] = useState([]);
  const [redoStack, setRedoStack] = useState([]);
  const [showGrid, setShowGrid] = useState(false);
  const [showColorPicker, setShowColorPicker] = useState(false);
  const [isSolving, setIsSolving] = useState(false);
  const [result, setResult] = useState('');
  
  // InkML data tracking
  const [currentStroke, setCurrentStroke] = useState([]);
  const [allStrokes, setAllStrokes] = useState([]);
  const [startTime, setStartTime] = useState(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    
    const setCanvasSize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight - 60;
      context.strokeStyle = penColor;
      context.lineJoin = 'round';
      context.lineCap = 'round';
      context.lineWidth = tool === 'pen' ? penSize : eraserSize;
      if (showGrid) drawGrid(context);
    };

    setCanvasSize();
    setCtx(context);
    saveToUndoStack();

    window.addEventListener('resize', setCanvasSize);
    return () => window.removeEventListener('resize', setCanvasSize);
  }, []);

  useEffect(() => {
    if (ctx) {
      ctx.strokeStyle = tool === 'pen' ? penColor : '#ffffff';
      ctx.lineWidth = tool === 'pen' ? penSize : eraserSize;
    }
  }, [tool, penColor, penSize, eraserSize, ctx]);

  // Convert strokes to InkML format
  const convertToInkML = () => {
    // Create a basic InkML structure
    let inkML = `<?xml version="1.0" encoding="UTF-8"?>
<ink xmlns="http://www.w3.org/2003/InkML">
  <definitions>
    <timestamp id="ts" value="0"/>
  </definitions>
  <annotationXML>
    <annotation type="truth">Unknown</annotation>
  </annotationXML>`;
    
    // Add trace format
    inkML += `
  <traceFormat>
    <channel name="X" type="decimal"/>
    <channel name="Y" type="decimal"/>
    <channel name="T" type="decimal"/>
  </traceFormat>`;
    
    // Add each stroke as a trace
    allStrokes.forEach((stroke, index) => {
      if (stroke.length > 0 && tool === 'pen') { // Only include pen strokes, not eraser strokes
        inkML += `
  <trace id="${index}">`;
        
        // Add points in format "x y t"
        stroke.forEach(point => {
          inkML += `${point.x} ${point.y} ${point.t}, `;
        });
        
        // Remove trailing comma and space
        inkML = inkML.slice(0, -2);
        
        inkML += `</trace>`;
      }
    });
    
    // Close the InkML document
    inkML += `
</ink>`;
    
    return inkML;
  };

  const drawGrid = (context) => {
    const canvas = canvasRef.current;
    const gridSize = 20;
    
    context.save();
    context.strokeStyle = '#ddd';
    context.lineWidth = 0.5;

    for (let x = 0; x <= canvas.width; x += gridSize) {
      context.beginPath();
      context.moveTo(x, 0);
      context.lineTo(x, canvas.height);
      context.stroke();
    }

    for (let y = 0; y <= canvas.height; y += gridSize) {
      context.beginPath();
      context.moveTo(0, y);
      context.lineTo(canvas.width, y);
      context.stroke();
    }

    context.restore();
  };

  const saveToUndoStack = () => {
    const canvas = canvasRef.current;
    setUndoStack(prev => [...prev, canvas.toDataURL()]);
    setRedoStack([]); // Clear redo stack when new action is performed
  };

  const handleUndo = () => {
    if (undoStack.length > 1) {
      const prevState = undoStack[undoStack.length - 2];
      const img = new Image();
      img.src = prevState;
      img.onload = () => {
        ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
        ctx.drawImage(img, 0, 0);
        if (showGrid) drawGrid(ctx);
      };
      
      setRedoStack(prev => [...prev, undoStack[undoStack.length - 1]]);
      setUndoStack(prev => prev.slice(0, -1));
      
      // Remove the last stroke from allStrokes
      if (allStrokes.length > 0) {
        setAllStrokes(prev => prev.slice(0, -1));
      }
    }
  };

  const handleRedo = () => {
    if (redoStack.length > 0) {
      const nextState = redoStack[redoStack.length - 1];
      const img = new Image();
      img.src = nextState;
      img.onload = () => {
        ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
        ctx.drawImage(img, 0, 0);
        if (showGrid) drawGrid(ctx);
      };
      
      setUndoStack(prev => [...prev, nextState]);
      setRedoStack(prev => prev.slice(0, -1));
    }
  };

  const clearCanvas = () => {
    if (ctx) {
      ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
      if (showGrid) drawGrid(ctx);
      saveToUndoStack();
      
      // Clear all strokes
      setAllStrokes([]);
    }
  };

  const saveCanvas = () => {
    const link = document.createElement('a');
    link.download = 'math-notes.png';
    link.href = canvasRef.current.toDataURL();
    link.click();
  };

  const shareCanvas = () => {
    canvasRef.current.toBlob((blob) => {
      const file = new File([blob], 'math-notes.png', { type: 'image/png' });
      if (navigator.share && navigator.canShare({ files: [file] })) {
        navigator.share({
          files: [file],
          title: 'Math Notes',
        });
      } else {
        saveCanvas();
      }
    });
  };

  const solveEquations = async () => {
    try {
      setIsSolving(true);
      setResult(''); // Clear previous result
      
      // Convert drawing to InkML
      const inkMLData = convertToInkML();
      
      // Get image data as well (as backup or for debugging)
      const canvas = canvasRef.current;
      const base64Image = canvas.toDataURL('image/png').split(',')[1];
  
      const response = await fetch('http://localhost:3001/api/solve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          inkml: inkMLData,
          image: base64Image
        }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      
      // Display result from model
      if (data.result) {
        setResult(data.result);
      } else {
        alert('No solution provided. Please try again.');
      }
    } catch (error) {
      console.error('Error solving equations:', error);
      alert('Failed to solve equations. Please try again.');
    } finally {
      setIsSolving(false);
    }
  };

  const startDrawing = (e) => {
    e.preventDefault();
    const rect = canvasRef.current.getBoundingClientRect();
    const x = (e.clientX || e.touches?.[0]?.clientX) - rect.left;
    const y = (e.clientY || e.touches?.[0]?.clientY) - rect.top;
    
    setIsDrawing(true);
    setLastX(x);
    setLastY(y);
    
    // Start tracking a new stroke with timestamp
    setStartTime(Date.now());
    setCurrentStroke([{ x, y, t: 0 }]); // First point has time 0
  };

  const draw = (e) => {
    if (!isDrawing) return;
    e.preventDefault();

    const rect = canvasRef.current.getBoundingClientRect();
    const x = (e.clientX || e.touches?.[0]?.clientX) - rect.left;
    const y = (e.clientY || e.touches?.[0]?.clientY) - rect.top;

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(x, y);
    ctx.stroke();

    setLastX(x);
    setLastY(y);
    
    // Add point to current stroke with timestamp relative to stroke start
    const currentTime = Date.now();
    const relativeTime = currentTime - startTime;
    setCurrentStroke(prev => [...prev, { x, y, t: relativeTime }]);
  };

  const stopDrawing = () => {
    if (isDrawing) {
      setIsDrawing(false);
      saveToUndoStack();
      
      // Save current stroke to all strokes
      if (currentStroke.length > 0) {
        setAllStrokes(prev => [...prev, currentStroke]);
        setCurrentStroke([]);
      }
    }
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="flex justify-between p-4 bg-gray-100">
        {/* Left section - Undo/Redo */}
        <div className="flex gap-2">
          <button
            className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            onClick={handleUndo}
            title="Undo"
          >
            <Undo className="w-6 h-6" />
          </button>
          <button
            className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            onClick={handleRedo}
            title="Redo"
          >
            <Redo className="w-6 h-6" />
          </button>
        </div>

        {/* Center section - Tools */}
        <div className="flex gap-4">
          <button
            className={`p-2 rounded-lg ${tool === 'pen' ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
            onClick={() => setTool('pen')}
            title="Pen"
          >
            <Pencil className="w-6 h-6" />
          </button>
          <button
            className={`p-2 rounded-lg ${tool === 'eraser' ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
            onClick={() => setTool('eraser')}
            title="Eraser"
          >
            <Eraser className="w-6 h-6" />
          </button>
          <button
            className={`p-2 rounded-lg ${showGrid ? 'bg-blue-500 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
            onClick={() => setShowGrid(!showGrid)}
            title="Toggle Grid"
          >
            <Grid className="w-6 h-6" />
          </button>
          <button
            className={`p-2 rounded-lg ${isSolving ? 'bg-gray-400' : 'bg-gray-200 hover:bg-gray-300'}`}
            onClick={solveEquations}
            disabled={isSolving}
            title="Solve Equations"
          >
            <Calculator className="w-6 h-6" />
          </button>
        </div>

        {/* Right section - Save/Share/Delete */}
        <div className="flex gap-2">
          <button
            className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            onClick={saveCanvas}
            title="Save"
          >
            <Save className="w-6 h-6" />
          </button>
          <button
            className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            onClick={shareCanvas}
            title="Share"
          >
            <Share2 className="w-6 h-6" />
          </button>
          <button
            className="p-2 rounded-lg bg-gray-200 hover:bg-gray-300"
            onClick={clearCanvas}
            title="Clear"
          >
            <Trash2 className="w-6 h-6" />
          </button>
        </div>
      </div>

      {/* Add Results Display */}
      <div className="fixed top-20 right-4 p-4 bg-white rounded-lg shadow-lg max-w-xs">
        {result && (
          <p className="text-sm text-gray-800">{result}</p>
        )}
        {isSolving && (
          <p className="text-sm text-gray-600">Processing...</p>
        )}
      </div>

      {/* Side controls */}
      <div className="fixed left-4 top-1/2 transform -translate-y-1/2 flex flex-col gap-4 bg-white p-4 rounded-lg shadow-lg">
        <button
          className="w-8 h-8 rounded-full bg-gray-200 hover:bg-gray-300"
          onClick={() => setShowColorPicker(!showColorPicker)}
          title="Color Picker"
          style={{ backgroundColor: penColor }}
        />
        {showColorPicker && (
          <div className="absolute top-12 left-0 z-10">
            <HexColorPicker color={penColor} onChange={setPenColor} />
          </div>
        )}
      </div>

      <div className="fixed right-4 top-1/2 transform -translate-y-1/2">
        <div className="p-2 bg-white shadow-lg rounded-xl border-2 border-gray-300">
          <div className="relative h-64 w-12 bg-gray-200 rounded-lg overflow-hidden">
            <input
              type="range"
              min={tool === 'pen' ? "1" : "10"}
              max={tool === 'pen' ? "20" : "50"}
              value={tool === 'pen' ? penSize : eraserSize}
              onChange={(e) => {
                if (tool === 'pen') {
                  setPenSize(parseInt(e.target.value));
                } else {
                  setEraserSize(parseInt(e.target.value));
                }
              }}
              className="absolute w-64 h-12 -rotate-90 -translate-x-28 translate-y-28 appearance-none bg-transparent cursor-pointer outline-none"
              style={{
                WebkitAppearance: 'none',
                MozAppearance: 'none',
                '&::-webkit-slider-thumb': {
                  WebkitAppearance: 'none',
                  appearance: 'none'
                },
                '&::-moz-range-thumb': {
                  appearance: 'none'
                },
                '&::-webkit-slider-runnable-track': {
                  background: 'transparent'
                },
                '&::-moz-range-track': {
                  background: 'transparent'
                }
              }}
            />
            <div 
              className="absolute bottom-0 left-0 right-0 border bg-gray-400"
              style={{
                height: `${((tool === 'pen' ? penSize : eraserSize) - (tool === 'pen' ? 1 : 10)) / 
                        (tool === 'pen' ? 19 : 40) * 100}%`
              }}
            />
            <div 
              className="absolute w-12 h-6 bg-white rounded-md shadow-md -translate-x-0 transform cursor-pointer pointer-events-none border border-gray-300"
              style={{
                top: `calc(${100 - ((tool === 'pen' ? penSize : eraserSize) - (tool === 'pen' ? 1 : 10)) / 
                      (tool === 'pen' ? 19 : 40) * 100}% - 12px)`
              }}
            />
          </div>
        </div>
      </div>
      
      <canvas
        ref={canvasRef}
        className="flex-1 bg-white cursor-crosshair touch-none"
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={stopDrawing}
        onMouseOut={stopDrawing}
        onTouchStart={startDrawing}
        onTouchMove={draw}
        onTouchEnd={stopDrawing}
      />
    </div>
  );
};

export default DrawingCanvas;