import cv2
import numpy as np
import matplotlib.pyplot as plt

############
##FUNCTION##
############

def drawCircle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(blank_img,x,y,100,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(blank_img,x,y,100,(255,0,0),-1)

cv2.namedWindow(winname='My_Drawing')
cv2.setMouseCallback('My_Drawing',drawCircle)


###########################
##SHOW IMAGE WITH OPEN CV##
###########################
blank_img = np.zeros(shape=(512,512,3))

while True:

	cv2.imshow('My_Drawing',blank_img)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()

