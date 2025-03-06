import numpy as np 
import cv2
from cv2 import dnn
import matplotlib.pyplot as plt

def Initialize_CaffeModel():
    try:
        print("loading models.....")
        net = cv2.dnn.readNetFromCaffe('./models/colorization_deploy_v2.prototxt','./models/colorization_release_v2.caffemodel')
        pts = np.load('./models/pts_in_hull.npy')
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2,313,1,1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype='float32')]
    except:
        print("Error in loading models")
    return net

    # try:
    #     net.setInput(cv2.dnn.blobFromImage(L))
    #     ab = net.forward()[0, :, :, :].transpose((1,2,0))
    #     ab = cv2.resize(ab, (image.shape[1],image.shape[0]))
    #     L = cv2.split(lab)[0]
    # except:
    #     print("Error in setting input")
    # Colorize(image,L,ab,axis=2)

def Colorize(image,L,net,lab,axis=2):

    try:
        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1,2,0))
        ab = cv2.resize(ab, (image.shape[1],image.shape[0]))
        L = cv2.split(lab)[0]
    except:
        print("Error in setting input")

    try:
        colorized = np.concatenate((L[:,:,np.newaxis], ab), axis)
        colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized,0,1)
        colorized = (255 * colorized).astype("uint8")
        Display(image,colorized)
    except:
        print("Error in colorizing")
    return colorized

def Display(og,colorized):
    image = cv2.cvtColor(og, cv2.COLOR_BGR2RGB)
    # cv2.imshow("Original",image)
    plt.imshow(image)
    plt.axis("off")  # Hide axes
    plt.show()
    colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
    plt.imshow(colorized)
    plt.axis("off")  # Hide axes
    plt.show()


def preprocess_Image(image,net):
    # try:
    #     image = cv2.imread(path)
    # except:
    #     print("Error: unable to read image")
    # image = cv2.imread('./test_colorization/Gandhi-and-Sarojini-Naidu-featured-1366x768.webp')
    try:
        scaled = image.astype("float32")/255.0
        lab = cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)
        resized = cv2.resize(lab,(224,224))
        L = cv2.split(resized)[0]
        L -= 50
        # print(L)
    except:
        print("Error: unable to process image")
    # Initialize_CaffeModel(L,image,lab)
    Colorize(image,L,net,lab,axis=2)
    # return L,image,lab

if __name__=="__main__":
    import os

    path = "E:/EDUBOOST/Sample/test_colorization/50263418938_79a0f6e789_k-1024x729.jpg"
    if os.path.exists(path):
        print("Path exists.")
    else:
        print("Path does not exist.")
    # path = './test_colorization/Landscape.jpg'
    net = Initialize_CaffeModel()
    image = cv2.imread(path)
    # path = input("Relative_Image_path:(./test_colorization/bw.jpg)")
    preprocess_Image(image,net)
    # print(L)



# # if __name__=="__main__":
# image = cv2.imread('bw.jpg')
# # image = cv2.imread('./test_colorization/Gandhi-and-Sarojini-Naidu-featured-1366x768.webp')
# scaled = image.astype("float32")/255.0
# lab = cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)


# resized = cv2.resize(lab,(224,224))
# L = cv2.split(resized)[0]
# L -= 50


# net.setInput(cv2.dnn.blobFromImage(L))
# ab = net.forward()[0, :, :, :].transpose((1,2,0))

# ab = cv2.resize(ab, (image.shape[1],image.shape[0]))

# L = cv2.split(lab)[0]
# colorized = np.concatenate((L[:,:,np.newaxis], ab), axis=2)

# colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
# colorized = np.clip(colorized,0,1)

# colorized = (255 * colorized).astype("uint8")


# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # cv2.imshow("Original",image)
# plt.imshow(image)
# plt.axis("off")  # Hide axes
# plt.show()
# colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)

# plt.imshow(colorized)
# plt.axis("off")  # Hide axes
# plt.show()
# # cv2.imshow("Colorized",colorized)
# # cv2.waitKey(0)
# # Mode                 LastWriteTime         Length Name
# # ----                 -------------         ------ ----
# # -a----        02-01-2025     11:26         173311 50263418938_79a0f6e789_k-1024x729.jpg
# # -a----        02-01-2025     11:26         116842 Gandhi-and-Sarojini-Naidu-featured-1366x768.webp
# # -a----        02-01-2025     11:26          15138 images (2).jpg
# # -a----        02-01-2025     11:26         392929 Myth_of_Etana.jpg
# # -a----        02-01-2025     11:26         111286 social-media-dimensions.webp