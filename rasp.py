import numpy as np
import cv2

class colorDetect:
	color = "NONE"
	glower = np.array([0,80,0],dtype = "uint8")
	gupper = np.array([180,255,45],dtype = "uint8")
	ylower = np.array([0,120,120],dtype = "uint8")
	yupper = np.array([80,255,255],dtype = "uint8")
	rlower = np.array([0,0,120],dtype = "uint8")
	rupper = np.array([80,80,255],dtype = "uint8")
	kernel = np.ones((3,3),np.uint8)

	def __init__(self,img):
		#GREEN
		bin = cv2.inRange(img,colorDetect.glower,colorDetect.gupper)
		_,contour,hier = cv2.findContours(bin,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contour:
			cv2.drawContours(bin,[cnt],0,255,-1)
		bin = cv2.morphologyEx(bin, cv2.MORPH_OPEN, colorDetect.kernel)
		bin = cv2.erode(bin,colorDetect.kernel,iterations = 1)
		bin = cv2.medianBlur(bin,7)
		_,contour,hierarchy = cv2.findContours(bin.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for c in contour:
			colorDetect.color = "GREEN"
			hull = cv2.convexHull(c)
			cv2.drawContours(img, [hull], -1, (0,255,0), 2)

		#YELLOW
		bin = cv2.inRange(img,colorDetect.ylower,colorDetect.yupper)
		_,contour,hier = cv2.findContours(bin,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contour:
			cv2.drawContours(bin,[cnt],0,255,-1)
		bin = cv2.morphologyEx(bin, cv2.MORPH_OPEN, colorDetect.kernel)
		bin = cv2.erode(bin,colorDetect.kernel,iterations = 1)
		bin = cv2.medianBlur(bin,7)
		_,contour,hierarchy = cv2.findContours(bin.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for c in contour:
			colorDetect.color = "YELLOW"
			hull = cv2.convexHull(c)
			cv2.drawContours(img, [hull], -1, (0,255,255), 2)

		#RED
		bin = cv2.inRange(img,colorDetect.rlower,colorDetect.rupper)
		_,contour,hier = cv2.findContours(bin,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contour:
			cv2.drawContours(bin,[cnt],0,255,-1)
		bin = cv2.morphologyEx(bin, cv2.MORPH_OPEN, colorDetect.kernel)
		bin = cv2.erode(bin,colorDetect.kernel,iterations = 1)
		bin = cv2.medianBlur(bin,7)
		_,contour,hierarchy = cv2.findContours(bin.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for c in contour:
			colorDetect.color = "RED"
			hull = cv2.convexHull(c)
			cv2.drawContours(img, [hull], -1, (0,0,255), 2)
