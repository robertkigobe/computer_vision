
import cv2
path = '/Users/robertkigobe/Documents/My_Research/My_Python/Computer_vision/images/norumbega.png'
img = cv2.imread(path)

while True:

	cv2.imshow('Road',img)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()