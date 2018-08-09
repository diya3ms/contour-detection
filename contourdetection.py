import cv2
import numpy as np

def detectContours(image):
	greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(greyImage,30,200)
	_,contours,_ = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(image,contours,-1,(0,255,0),2)
	return image
	
capture = cv2.VideoCapture(0)
while(True):
	ret, frame = capture.read()
	cv2.imshow('Original',frame)
	cv2.imshow('Contour detection',detectContours(frame))
	if cv2.waitKey(1) == 13:
		break
capture.release()
cv2.destroyAllWindows()	
