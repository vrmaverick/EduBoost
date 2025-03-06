from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from typing import Optional
import os
import tempfile
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class SolveRequest(BaseModel):
    inkml: str
    image: Optional[str] = None

class SolveResponse(BaseModel):
    result: str

@app.post("/api/solve", response_model=SolveResponse)
async def solve_equation(request: SolveRequest):
    try:
        # Create a temporary file to save the InkML data
        with tempfile.NamedTemporaryFile(suffix=".inkml", delete=False) as temp_inkml:
            temp_inkml.write(request.inkml.encode('utf-8'))
            temp_inkml_path = temp_inkml.name
        
        logger.info(f"Saved InkML data to {temp_inkml_path}")
        
        # If you also want to save the image for debugging
        if request.image:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
                img_data = base64.b64decode(request.image)
                temp_img.write(img_data)
                temp_img_path = temp_img.name
            logger.info(f"Saved image data to {temp_img_path}")
        
        # Call your model with the InkML file
        # Example: Using a command-line model
        try:
            # Replace with your actual model command
            result = subprocess.run(
                ["python", "your_model_script.py", "--input", temp_inkml_path],
                capture_output=True,
                text=True,
                check=True
            )
            model_output = result.stdout.strip()
            logger.info(f"Model output: {model_output}")
            
            # Clean up temporary files
            os.unlink(temp_inkml_path)
            if request.image:
                os.unlink(temp_img_path)
                
            return SolveResponse(result=model_output)
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Model execution failed: {e.stderr}")
            # Clean up temporary files
            os.unlink(temp_inkml_path)
            if request.image:
                os.unlink(temp_img_path)
            raise HTTPException(status_code=500, detail=f"Model execution failed: {e.stderr}")
            
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# For testing - return dummy result
@app.post("/api/solve/test", response_model=SolveResponse)
async def test_solve(request: SolveRequest):
    # Just return a dummy result without processing
    return SolveResponse(result="2x + 3 = 7, x = 2")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)