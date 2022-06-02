import cv2
import numpy as np
vc = cv2.VideoCapture('video.mp4')
n = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timeF=30
i = 0
img=np.zeros((256,320,3),np.uint8)
def encode(img,frame,num):
    a=[1,0,2]
    for p in range(39,-1,-1):
        k=[]
        for q in range(63):
            if frame[p,q]==255:
                k.append(q)
        if len(k)!=0:
            l=0
            for l in range(64):
                pixel=num*2560+(39-p)*64+l
                img[int(pixel/960),pixel%320,a[int((pixel%960)/320)]]=k[int(l*len(k)/64)]*4
        else:
            for l in range(64):
                pixel=num*2560+(39-p)*64+l
                img[int(pixel/960),pixel%320,a[int((pixel%960)/320)]]=255
while rval:
    if (n % timeF == 0 and rval and i <96):
        frame=cv2.resize(frame,(64,40))
        #frame=cv2.Canny(frame,100,200)
        frame=np.where(frame[:,:,0]*0.114+frame[:,:,1]*0.587+frame[:,:,2]*0.114>127.5,255,0)
        encode(img,frame,i)
        cv2.imshow('frame',frame.astype(np.uint8))
        cv2.imshow('img',img)
        cv2.waitKey(1)
        i += 1
    rval, frame = vc.read()
    n = n + 1
cv2.imwrite('video1.png',img)
