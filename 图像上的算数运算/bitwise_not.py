"""
bitwise_not—图像非运算

函数原型：bitwise_not(src1, src2, dst=None, mask=None)

src1：图像矩阵1

src1：图像矩阵2

dst：默认选项

mask：默认选项
"""

import numpy as np
import cv2


# 画圆形
Circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(Circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", Circle)
cv2.waitKey(0)


# 圆形的非运算
bitwiseNot = cv2.bitwise_not(Circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
