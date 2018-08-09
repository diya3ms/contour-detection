import cv2
import numpy as np
capture = cv2.VideoCapture(0)
while(True):
	ret, frame = capture.read()
	cv2.imshow('Original',frame)
	cv2.imshow('Contour detection',detectContours(frame))
	if cv2.waitKey(1) == 13:
		break
capture.release()
cv2.destroyAllWindows()	
