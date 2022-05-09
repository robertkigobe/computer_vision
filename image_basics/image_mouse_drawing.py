import cv2
import numpy as np
import matplotlib.pyplot as plt

############
##VARIABLES#
############

drawing = False
ix,iy = -1,-1




############
##FUNCTION##
############

def draw_rectangle(event,x,y,flags,params):
    
    global ix,iy,drawing
        
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(blank_img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(blank_img,(ix,iy),(x,y),(0,255,0),-1)
            

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)


###########################
##SHOW IMAGE WITH OPEN CV##
###########################
blank_img = np.zeros((512,512,3))

while True:

    cv2.imshow('my_drawing',blank_img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()