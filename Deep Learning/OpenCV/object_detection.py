import os
import cv2

img = cv2.imread(os.path.join('.','images','obj_detection.jpg'))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
# inverse binary because we need the objects to be white while detecting them.

contours , hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 1. contours: A Python list of all the detected contours. 
# Each individual contour is a NumPy array containing the (x, y) coordinates of the boundary points.
# 2. hierarchy: A matrix containing information about image topology. 
# It tells you which contour is a "parent" (contains something) and which is a "child" (is inside something).

for cnt in contours:
    # print(cv2.contourArea(cnt)) # we can see so much noise 

    # removing noise
    if cv2.contourArea(cnt) > 200:
        # Draw ALL contours (-1) in green (0, 255, 0) with a line thickness of 2 pixels
        cv2.drawContours(img, cnt, -1, (0,255,0), 1)

        x1, y1, w,h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x1,y1), (x1+w, y1+h), (0,255,0), 2)

cv2.imshow("orginial image", img)
cv2.imshow("thresholded image", thresh)
# cv2.imshow("contours", contours)
cv2.waitKey(0)
cv2.destroyAllWindows()