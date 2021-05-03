from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageChops
import sys
import math
import time
import numpy as np

def ColorDistance(c1, c2):
    (r1,g1,b1) = c1
    (r2,g2,b2) = c2
    return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

def getneighbours(x1,y1,x2,y2):
    coords = []
    if(x1>0):
        coords.append((x1-1,y1))
    if(y1>0):
        coords.append((x1,y1-1))
    if(x1<x2-1):
        coords.append((x1+1,y1))
    if(y1<y2-1):
        coords.append((x1,y1+1))
    return coords

imgcount = 467
main_start_time = time.time()
while(imgcount<469):
    start_time = time.time()
    img = Image.open("export/frame"+str(imgcount)+".png")
    cpyimg = Image.open("export/frame"+str(imgcount)+".png")
    width, hight = img.size
    
    x=0
    y = 0
    count = 0
    while(y<hight):
        while(x<width):
        
            if ColorDistance((148,206,219),img.getpixel((x,y)))<30 :
                img.putpixel((x,y), (255,165,0))
                count = count + 1
            else:
                img.putpixel((x,y), (0,0,0))
                r,g,b = img.getpixel((x,y))
            x=x+1
        y=y+1
        x=0

    matches = []    
    checklist = []  
    neighbours = []   
    neighbourmatches = [] 
    x=0
    y = 0
    markers = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
    c = 0
    while(y<hight):
        while(x<width):
            if(img.getpixel((x,y)) ==  (255,165,0)): ##első találáat
                
                checklist.append((x,y))
                matches.append((x,y))
                while(len(checklist)>0):
                
                    neighbours = []
                    for item in checklist:
                        neighbours = neighbours + getneighbours(item[0],item[1],width,hight)
                    checklist = []
                    for item in neighbours:
                        if(img.getpixel(item) == (255,165,0)):
                            if item not in matches :
                                checklist.append(item)
                                matches.append(item)      
                #print(len(matches))
                most_left = 1000000
                most_right = 0
                most_top = 1000000
                most_bottom = 0
                if(len(matches)>20):
                    for item in matches:
                        _x, _y = item
                        if(_x>most_right):
                            most_right=_x
                        if(_x<most_left):
                            most_left = _x
                        if(_y>most_bottom):
                            most_bottom = _y
                        if(_y<most_top):
                            most_top = _y
                        #img.putpixel(item,markers[c])
                    draw = ImageDraw.Draw(cpyimg)
                    draw.rectangle((most_left-10,most_top-10,most_right+10,most_bottom+10),outline=(255,0,0))
                else:
                    for item in matches:
                        pass
                        #img.putpixel(item,(0,0,0))
                    c=c+1
                    if(c==len(markers)):
                        c=0
                matches = []
            x=x+1
        y=y+1
        x=0
    cpyimg.save("processed/frame"+str(imgcount)+".png")
    print(str(imgcount)+"/468 "+str(str(round((time.time() - start_time), 2)))+" s")
    imgcount = imgcount + 1

    #cpyimg.show()
print("Total time:"+str(str(round((time.time() - main_start_time), 0)))+" s")
intp = input()
