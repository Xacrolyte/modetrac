# Modetrac/handgesture

## How to use :scroll:

### 1. Run the script 

```sh
$ python finger_detect.py
```

#### Default threshold is set to 60; change using trackbar. 

```python
		#Variables
		threshold = 60  #Binary threshold

    	#Display threshold value
		def printThreshold(thr):
    	print("! Changed threshold to "+str(thr))
```

### 2. Press b for capturing stable background :camera:

#### Use the other key mapping options as per your needs

```python
	    #Keys
	    k = cv2.waitKey(10)
	    if k == 27:  #ESC to exit
	        camera.release()
	        cv2.destroyAllWindows()
	        break
	    elif k == ord('b'):  #'b' to capture the background
	        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
	        isBgCaptured = 1
	        print( '!!!Background Captured!!!')
	    elif k == ord('r'):  #'r' to reset the background
	        bgModel = None
	        triggerSwitch = False
	        isBgCaptured = 0
	        print ('!!!Reset BackGround!!!')
	    elif k == ord('n'):
	        triggerSwitch = True
```
### 3.  Now bring your hand inside the box :hand:

#### Watch your finger being detected

```python
	    def calculateFingers(res,drawing):
		    hull = cv2.convexHull(res, returnPoints=False)
		    if len(hull) > 3:
		        defects = cv2.convexityDefects(res, hull)
		        if type(defects) != type(None):
		            return True, cnt
		    return False, 0
```

### 4. Contribute :smile:

#### Apply recognition and storage.