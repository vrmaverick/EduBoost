from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
from io import BytesIO
from PIL import Image
import uvicorn
from colorize import *

app = FastAPI()

# Enable CORS to allow requests from React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

net = Initialize_CaffeModel()

# Paths to the model files (relative to the location of main.py)
# model_path = "./models/colorization_release_v2.caffemodel"
# proto_path = "./models/colorization_deploy_v2.prototxt"
# points_path = "./models/pts_in_hull.npy"

# # Load the model
# net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
# pts = np.load(points_path)
# class8 = net.getLayerId("class8_ab")
# conv8 = net.getLayerId("conv8_313_rh")
# pts = pts.transpose(1, 0).reshape(2, 313, 1, 1)
# net.getLayer(class8).blobs = [pts.astype("float32")]
# net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]


@app.post("/colorize/")
async def colorize_image(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        content = await file.read()
        image = Image.open(BytesIO(content)).convert("RGB")
        image = np.array(image)
        colorize_image = preprocess_Image(image,net)

        # # Convert to grayscale
        # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # # Preprocess the image for the model
        # blob = cv2.dnn.blobFromImage(gray, 1.0, (224, 224), (50, 50, 50))
        # net.setInput(blob)

        # # Predict
        # ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
        # (h, w) = gray.shape[:2]
        # ab = cv2.resize(ab, (w, h))

        # # Combine channels
        # lab = np.concatenate((cv2.split(cv2.cvtColor(image, cv2.COLOR_RGB2LAB))[0:1], ab), axis=2)
        # colorized = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        # colorized = (255.0 * np.clip(colorized, 0, 1)).astype("uint8")

        # Save to buffer and send back
        _, encoded_image = cv2.imencode(".png", colorize_image)
        return JSONResponse(
            content={"image": encoded_image.tobytes().hex()},
            media_type="application/json",
        )

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import JSONResponse
# import numpy as np
# import cv2
# # import os
# from io import BytesIO
# from PIL import Image
# import uvicorn

# app = FastAPI()

# # Paths to the model files
# model_path = "models/colorization_release_v2.caffemodel"
# proto_path = "models/colorization_deploy_v2.prototxt"
# points_path = "models/pts_in_hull.npy"

# # Load the model
# net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
# pts = np.load(points_path)
# class8 = net.getLayerId("class8_ab")
# conv8 = net.getLayerId("conv8_313_rh")
# pts = pts.transpose(1, 0).reshape(2, 313, 1, 1)
# net.getLayer(class8).blobs = [pts.astype("float32")]
# net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# @app.post("/colorize/")
# async def colorize_image(file: UploadFile = File(...)):
#     try:
#         # Read the uploaded file
#         content = await file.read()
#         image = Image.open(BytesIO(content)).convert("RGB")
#         image = np.array(image)

#         # Convert to grayscale
#         gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#         gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

#         # Preprocess the image for the model
#         blob = cv2.dnn.blobFromImage(gray, 1.0, (224, 224), (50, 50, 50))
#         net.setInput(blob)

#         # Predict
#         ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
#         (h, w) = gray.shape[:2]
#         ab = cv2.resize(ab, (w, h))

#         # Combine channels
#         lab = np.concatenate((cv2.split(cv2.cvtColor(image, cv2.COLOR_RGB2LAB))[0:1], ab), axis=2)
#         colorized = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
#         colorized = (255.0 * np.clip(colorized, 0, 1)).astype("uint8")

#         # Save to buffer and send back
#         _, encoded_image = cv2.imencode(".png", colorized)
#         return JSONResponse(
#             content={"image": encoded_image.tobytes().hex()},
#             media_type="application/json"
#         )

#     except Exception as e:
#         return {"error": str(e)}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


