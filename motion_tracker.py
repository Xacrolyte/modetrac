import cv2
import numpy as np
import requests

#Main
def main():
      
      #Frame Dimension
      width = 800
      height = 800

      #Capture window
      capwindow = cv2.VideoCapture(0)
      #capwindow = cv2.VideoCapture('http://10.103.121.102:8080/shot.jpg')

#      capwindow.set(3,width)
#      capwindow.set(4,height)

      #Frame condition
      if capwindow.isOpened():
      	ret, frame = capwindow.read()
      	#True and matrix
      else:
      	ret = False

      #original
      ret, frame1 = capwindow.read()

      #Movement
      ret, frame2 = capwindow.read()

      #Color substraction
      #ret, frame3 = capwindow.read()
      
      #while true
      while ret:
      	#Average background difference
      	difference = cv2.absdiff(frame1, frame2)

      	#Video processing
      	grey = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
      	blur = cv2.GaussianBlur(grey, (7,7), 0)
      	ret, threshold = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
      	dilated = cv2.dilate(threshold, np.ones((7,7), np.uint8), iterations=1)
      	eroded = cv2.erode(dilated, np.ones((7,7), np.uint8), iterations=1)
      	
      	#Contouring
      	contour, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      	cv2.drawContours(frame2, contour, -1, (0,255,0), 2)
      
    
    		#Display
      	cv2.imshow("Original", frame1)
      	cv2.imshow("Movement", frame2)
      	#cv2.imshow("Color Substraction", frame3)

      	#For exit (13 = enter)
      	if cv2.waitKey(1)==13:
      		break

      	frame2 = frame1
      	ret, frame1 = capwindow.read()

      cv2.destroyAllWindows()
      capwindow.release()

if __name__ == '__main__':
	main()


