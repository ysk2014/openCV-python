import numpy as np
import cv2

cap = cv2.VideoCapture(0)

width = 640
ret = cap.set(3, width)
height = 480
ret = cap.set(4, height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame, 0)

        out.write(frame)
        cv2.imshow('im', frame)

    else:
        break

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
