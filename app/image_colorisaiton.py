import streamlit as st
import cv2
import numpy as np

# Load the model and kernel file paths
prototxt_path = '/workspace/EduBoost/Image_Colorisation/models/colorization_deploy_v2.prototxt'
model_path = '/workspace/EduBoost/Image_Colorisation/models/colorization_release_v2.caffemodel'
kernel_path = '/workspace/EduBoost/Image_Colorisation/models/pts_in_hull.npy'

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
pts = np.load(kernel_path)
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts.astype('float32')]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, dtype='float32')]

def colorize_image(image):
    """ Colorizes a black and white image using OpenCV DNN """
    # Convert image to LAB color space
    normalized = image.astype('float32') / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)

    # Resize image to 224x224 for the model
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50  # Model-specific preprocessing

    # Set input and forward pass through the model
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # Resize the result to the original image size
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]  # Get the original L channel

    # Combine L and ab channels to create the colorized image
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = (255.0 * colorized).astype('uint8')

    return colorized

# Streamlit App
def image_colorisation_page():
    st.title("🎨 Image Colorization🌈")

    # Upload an image
    uploaded_file = st.file_uploader("Upload a grayscale image (png, jpg, jpeg, jfif, webp)", type=["png", "jpg", "jpeg", "jfif", "webp"])
    
    if uploaded_file:
        # Read the image as an OpenCV object
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        bw_image = cv2.imdecode(file_bytes, 1)

        # Display the uploaded image
        st.image(bw_image, caption='Uploaded Image (B&W)', use_column_width=True)
        
        # Colorize the image when the button is clicked
        if st.button("Colorize"):
            with st.spinner("🖌️ Colorizing your image..."):
                colorized_image = colorize_image(bw_image)
            
            # Display the colorized image
            st.image(colorized_image, caption='Colorized Image', use_column_width=True)


