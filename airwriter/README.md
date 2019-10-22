# Modetrac/airwriting

## How to use :scroll:

### 1. Run the script 

```sh
$ python air_writer.py
```

#### Color is set to blue; change accordingly

```python
    #Range for Blue
    lower_range = np.array([100,70,70])
    upper_range = np.array([120,255,255])
```

### 2. Find a pen or an object to track according to your color range :pen:

#### Change values for optimization

```python
    #Mask
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.inRange(hsv,lower_range,upper_range)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    #Color filter AND
    bitwise_1 = cv2.bitwise_and(frame, frame, mask=mask)
```
### 3. Contribute :smile:

#### Apply neural network using keras/tensorflow 