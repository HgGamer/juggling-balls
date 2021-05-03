import cv2
import numpy as np
import glob
 
img_array = []
imgcount = 0
while(imgcount<469):
    filename = "processed/frame"+str(imgcount)+".png"
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    imgcount = imgcount + 1

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
