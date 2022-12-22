import numpy as np       
import cv2
import glob
import imutils

image_paths = glob.glob('unstitchedImages/*.jpg')      #Here glob module is used to load all the .jpg filetypes inside the unstitchesImage folder.
images=[]                                          #It is an empty list where we are going to store all of our images.

   #And here inside for loop we are going to use opencv to read in the images from these image paths.
for image in image_paths:
    img = cv2.imread(image)
    images.append(img)          #Here we are appending all the loaded images into the empty list created above.
    cv2.imshow("Image",img)     #cv2. imshow() method is used to display the loaded images.
    cv2.waitKey(0)              #Here we are waiting for a key press before we load and append our next image.


imagestitcher=cv2.Stitcher_create()   #This fuction is used to stitch loaded images properly.

error, stitched_img=imagestitcher.stitch(images)  #error if it could not find enough keypoints to actually math the images. 

if not error:
    cv2.imwrite("stitchedOutput.png",stitched_img)  #It is a method used to save image in a currently working directory.
    cv2.imshow("stitched Image",stitched_img)
    cv2.waitKey(0)
    