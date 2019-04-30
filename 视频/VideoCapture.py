import numpy as np
import cv2

cap = cv2.VideoCapture(0)

print(cv2.CAP_PROP_FRAME_WIDTH)
print(cv2.CAP_PROP_FRAME_HEIGHT)

print(cap.get(3))
print(cap.get(4))

cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():

    ret, frame = cap.read()

    frame = cv2.flip(frame, -1)  # 左右翻转,使用笔记本电脑摄像头才有用。
    # flipCode：翻转方向：1：水平翻转；0：垂直翻转；-1：水平垂直翻转

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('im', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
