import cv2
import numpy as np
import argparse
from collections import deque

#Start Live feed
device = cv2.VideoCapture(0)


#Points
points = deque(maxlen=64)

#Infinite Loop
while True:

    ret, frame = device.read()
    
    #Convert color from RBG to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Range for Blue
    lower_range = np.array([100,70,70])
    upper_range = np.array([120,255,255])
    
    #Mask
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.inRange(hsv,lower_range,upper_range)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    #Color filter AND
    bitwise_1 = cv2.bitwise_and(frame, frame, mask=mask)

    #Count
    counts, h = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]

    #Center
    center = None

    #Line
    if len(counts) > 0:
        #Circle
        circle = max(counts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(circle)

        #Moment
        moment = cv2.moments(circle)

        center = (int(moment["m10"]/moment["m00"]), int(moment["m01"]/moment["m00"])) 

        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        points.appendleft(center)

        for i in range(1,len(points)):
            if points[i-1] is None or points[i] is None:
                continue
            thick = int(np.sqrt(len(points) / float(i + 1))*2.5)
            cv2.line(frame, points[i-1], points[i], (0, 0, 255), thick)

    #Show
    cv2.imshow("Show1", frame)

    #Exit Infinte loop
    if cv2.waitKey(1) == 13:
        break

device.release()
cv2.destroyAllWindows()