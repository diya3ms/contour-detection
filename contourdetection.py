import cv2
import numpy as npdef detectContours(image):
	greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(greyImage,30,200)
	
	
#funtion half only findcontours and draw contour left
def detectContours(image):
	greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(greyImage,30,200)
	
	
capture = cv2.VideoCapture(0)
while(True):
	ret, frame = capture.read()
	cv2.imshow('Original',frame)
	cv2.imshow('Contour detection',detectContours(frame))
	if cv2.waitKey(1) == 13:
		break
capture.release()
cv2.destroyAllWindows()	
