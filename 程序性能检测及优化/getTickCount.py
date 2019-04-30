import cv2
import numpy as np


img1 = cv2.imread('../data/ml.jpg')

# getTickCount 返回从参考点到这个函数被执行的时钟数
e1 = cv2.getTickCount()


for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()

# getTickFrequency 返回时频率，或者说每秒钟的时钟数。
time = (e2 - e1) / cv2.getTickFrequency()

print(time)
