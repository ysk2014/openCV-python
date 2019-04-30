"""
bitwise_and—图像与运算， 是取两个图像的交集

函数原型：cv2.bitwise_and(src1, src2, dst=None, mask=None)

src1：图像矩阵1

src1：图像矩阵2

dst：默认选项

mask：默认选项
"""

import numpy as np
import cv2

# 画矩形
rectangle = np.zeros((300, 300), np.uint8)
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)


# 画圆形
Circle = np.zeros((300, 300), np.uint8)
cv2.circle(Circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", Circle)
cv2.waitKey(0)


# 画图像的交

biwiseAnd = cv2.bitwise_and(rectangle, Circle)
cv2.imshow('and', biwiseAnd)
cv2.waitKey(0)

cv2.destroyAllWindows()
