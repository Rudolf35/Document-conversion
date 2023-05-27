import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys

def printsave(*a):
    file = open('d:\\document.txt','a')
    print(*a)
    print(*a, file=file)
    file.close()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img = cv2.imread('paper.jpg')
draw = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
canny = cv2.Canny(gray,75,200)
#cv2.imshow('scan',canny)
#cv2.waitKey(0)

cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(cnts))
cv2.drawContours(draw, cnts, -1, (0,255), 0)
#cv2.imshow('scan', draw)
#cv2.waitKey(0)

cnts = sorted(cnts, key = cv2.contourArea, reverse= True)[:5]
for c in cnts:
    peri = cv2.arcLength(c,True)
    verticles = cv2.approxPolyDP(c,0.02*peri,True)
    if len(verticles) == 4:
        break
pts = verticles.reshape(4, 2)
for x, y in pts:
    cv2.circle(draw, (x,y) , 10 , (0,255,0), -1)
    
#cv2.imshow('scan', draw)
#cv2.waitKey(0)
merged = np.hstack((img, draw))

sm = pts.sum(axis = 1)
diff = np.diff(pts,axis = 1)

topleft = pts[np.argmin(sm)]
bottomright = pts[np.argmax(sm)]
topright = pts[np.argmin(diff)]
bottomleft = pts[np.argmax(diff)]

pts1 = np.float32([topleft, topright, bottomright, bottomleft])

w1 = abs(bottomright[0]-bottomleft[0])
w2 = abs(topright[0] - topleft[0])
h1 = abs(topright[1] - bottomright[1])
h2 = abs(topleft[1]-bottomleft[1])
width = max([w1,w2])
height = max([h1,h2])

pts2 = np.float32([[0,0],[width-1,0], [width-1, height-1], [0,height-1]])

mat = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, mat, (width,height))
cv2.imshow('scan', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

cv2.imshow('scan', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

printsave(pytesseract.image_to_string(thresh, lang='kor'))











