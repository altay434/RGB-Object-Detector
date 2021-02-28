import cv2
import numpy as np

camera = cv2.VideoCapture(0)
def nothing():
    pass

while True:
    _,frame = camera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    kernal = np.ones((5,5),"uint8")
    
    #red color l[150,170,70] h[179,255,255]
    low_red = np.array([150, 170, 70])
    high_red = np.array([179, 255, 255])
    
    red_mask = cv2.inRange(hsv, low_red, high_red)
    dilated_redmask = cv2.dilate(red_mask, kernal)
    blured_redmask = cv2.GaussianBlur(dilated_redmask, (5,5), 4/6)
    res_red = cv2.bitwise_and(frame, frame, mask = blured_redmask)
    
    contours_red, hierarchy = cv2.findContours(blured_redmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i=0
    for pic, contour in enumerate(contours_red):
        area = cv2.contourArea(contour)
        if area > 3000 :
            i+=1
            if i == 2:             #with this line i draw only one rectangle.
                break
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (100,50,40), 4)
            print("Red found")
    #blue color l[100,135,40] h[115,255,255]
    low_blue = np.array([100, 135, 40])
    high_blue = np.array([115, 255, 255])

    blue_mask = cv2.inRange(hsv, low_blue, high_blue)
    dilated_bluemask = cv2.dilate(blue_mask, kernal)
    blured_bluemask = cv2.GaussianBlur(dilated_bluemask, (5,5), 4/6)
    res_blue = cv2.bitwise_and(frame, frame, mask = blured_bluemask)

    contours_blue, hierarchy = cv2.findContours(blured_bluemask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours_blue):
        area = cv2.contourArea(contour)
        if area > 3000 :
            i+=1
            if i == 2:
                break
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (100,50,40), 4)
            print("Blue found")
            
    #green color l[40,70,40] h [90,255,255]

    low_green = np.array([40, 70, 40])
    high_green = np.array([90, 255, 255])
    green_mask = cv2.inRange(hsv, low_green, high_green)
    dilated_greenmask = cv2.dilate(green_mask, kernal)
    blured_greenmask = cv2.GaussianBlur(dilated_greenmask, (5,5), 4/6)
    res_green = cv2.bitwise_and(frame, frame, mask = blured_greenmask)

    contours_green, hierarchy = cv2.findContours(blured_greenmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours_green):
        area = cv2.contourArea(contour)
        
        if area > 3000 :
            i+=1
            x, y, w, h = cv2.boundingRect(contour)
            if i == 2:
                break
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(100,50,40),4)
            print("Green Found")
            
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1)==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
