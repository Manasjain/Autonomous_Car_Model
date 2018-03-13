import RPi.GPIO as GPIO
import numpy as np
import cv2
import rasp
import time

cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
p=GPIO.PWM(16,50)
q=GPIO.PWM(18,50)
p.start(0)
q.start(0)
previous="NONE"

while(True):
	
	# Capture frame-by-frame
	ret, img = cap.read()
	
	#Shrink frame size
	w = 300
	dim = (w, int(w * img.shape[0] / img.shape[1]))
	img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	
	# Call color detect function
	detect = rasp.colorDetect(img)
	
	# Display the resulting frame
	cv2.imshow('Preview',img)
	print (rasp.colorDetect.color)

	current=rasp.colorDetect.color
	if current==previous:
		continue
	else:
		if current=="NONE":
			continue
		if current=="RED":
			for i in range(50):
				p.ChangeDutyCycle(50-i)
				q.ChangeDutyCycle(50-i)
			p.ChangeDutyCycle(0)
			q.ChangeDutyCycle(0)
		if current=="GREEN":
			for i in range(50):
				p.ChangeDutyCycle(i)
				q.ChangeDutyCycle(i)
			p.ChangeDutyCycle(50)
			q.ChangeDutyCycle(50)

	if cv2.waitKey(1) & 0xFF == 27:
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
