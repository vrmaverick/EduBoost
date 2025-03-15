import cv2
import matplotlib as plt
from segment import detect_contours
import tensorflow as tf
from preprocess import binarize,resize_pad
import numpy as np
from solve import SolveEquation
from freeupspace import delete_image
class_names = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', 'div', 'times', 'y']

def Load_Model():
    new_model = tf.keras.models.load_model('eqn-detect1 -model')
    print("Model Loaded")
    return new_model

def Calculator(flag,image_dir,IMAGE,img_path):
    if flag == 1:
        # print("The flag is set to 1")
        input_image = cv2.imread(img_path) 
        ret, bw_img = cv2.threshold(input_image,127,255,cv2.THRESH_BINARY)
        # print("Now the image will be displayed")
        # plt.imshow(bw_img)
        # plt.show()
        
        # print("Saving image as savedimage.jpg")
        cv2.imwrite('equation_images/savedimage.jpg', bw_img)

        input_image_cpy = bw_img.copy()
        print("Detecting_contours")
        keep = detect_contours(image_dir+'savedimage.jpg')
        print(f"Length of keep{len(keep)}")
        print("updating image path to savedimage.jpg")
        img_path = image_dir+'savedimage.jpg'
        print(img_path)

    # now we have new img_path which is updated, keep , input_img_copy
    else:
        input_image = cv2.imread(img_path, 0) 
        input_image_cpy = input_image.copy()
        keep = detect_contours(image_dir+IMAGE)
        print(len(keep))

    model = Load_Model()
    eqn_list = []
    input_image = cv2.imread(img_path, 0) 
    # print("Image read from new path")
    inverted_binary_img = binarize(input_image)
    # print("Convert image to binary majority 1 and rest 0")'
    # print("now further processing")
    for (x, y, w, h) in sorted(keep, key = lambda x: x[0]):
        img = resize_pad(inverted_binary_img[y:y+h, x:x+w], (45, 45), 0)
        # print("Now Predicting using the model (Each segmented part of eqn then later combining)")
        pred_class = class_names[np.argmax(model.predict(tf.expand_dims(tf.expand_dims(img, 0), -1)))]
        if pred_class == "times":
            pred_class = "*"
        elif pred_class == "div":
            pred_class = "/"
        # elif pred_class ==
        # elif pred_class == ""
        eqn_list.append(pred_class)
        print(pred_class)
    # print("now once we get the appended eqn list now printing it")
    eqn = "".join(eqn_list)
    print(eqn)
    exp,result = SolveEquation(eqn)
    if exp == "none":
        print(result)
    else:
        print(f"Expression: {exp} = {result}")
    #Clearing up Space
    delete_image(img_path)

if __name__ == "__main__":

    image_dir = "equation_images/" # Directory where the image will be saved
    flag = 1#flag =1 for handwritten images,0 for drawn images
    IMAGE = "lineareqy4.png"
    img_path = "equation_images/"+IMAGE
    # #plt.imshow(img_path)
    # #plt.show()
    # if flag == 1:
    #     # print("The flag is set to 1")
    #     input_image = cv2.imread(img_path) 
    #     ret, bw_img = cv2.threshold(input_image,127,255,cv2.THRESH_BINARY)
    #     # print("Now the image will be displayed")
    #     # plt.imshow(bw_img)
    #     # plt.show()
        
    #     # print("Saving image as savedimage.jpg")
    #     cv2.imwrite('equation_images/savedimage.jpg', bw_img)

    #     input_image_cpy = bw_img.copy()
    #     print("Detecting_contours")
    #     keep = detect_contours(image_dir+'savedimage.jpg')
    #     print(f"Length of keep{len(keep)}")
    #     print("updating image path to savedimage.jpg")
    #     img_path = image_dir+'savedimage.jpg'
    #     print(img_path)

    # # now we have new img_path which is updated, keep , input_img_copy
    # else:
    #     input_image = cv2.imread(img_path, 0) 
    #     input_image_cpy = input_image.copy()
    #     keep = detect_contours(image_dir+IMAGE)
    #     print(len(keep))

    # model = Load_Model()
    # eqn_list = []
    # input_image = cv2.imread(img_path, 0) 
    # # print("Image read from new path")
    # inverted_binary_img = binarize(input_image)
    # # print("Convert image to binary majority 1 and rest 0")'
    # # print("now further processing")
    # for (x, y, w, h) in sorted(keep, key = lambda x: x[0]):
    #     img = resize_pad(inverted_binary_img[y:y+h, x:x+w], (45, 45), 0)
    #     # print("Now Predicting using the model (Each segmented part of eqn then later combining)")
    #     pred_class = class_names[np.argmax(model.predict(tf.expand_dims(tf.expand_dims(img, 0), -1)))]
    #     if pred_class == "times":
    #         pred_class = "*"
    #     elif pred_class == "div":
    #         pred_class = "/"
    #     # elif pred_class ==
    #     # elif pred_class == ""
    #     eqn_list.append(pred_class)
    #     print(pred_class)
    # # print("now once we get the appended eqn list now printing it")
    # eqn = "".join(eqn_list)
    # print(eqn)
    # SolveEquation(eqn)
    # #Clearing up Space
    # delete_image(img_path)