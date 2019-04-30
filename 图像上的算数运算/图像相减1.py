"""
subtract—图像矩阵相减

函数原型：cv2.subtract(src1, src2, dst=None, mask=None, dtype=None)

src1：图像矩阵1

src1：图像矩阵2

dst：默认选项

mask：默认选项

dtype：默认选项
"""

import numpy as np
import cv2


img1 = cv2.imread('./subtract1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./subtract2.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('1', img1)
cv2.imshow('2', img2)

st = img2 - img1

cv2.imshow('after', st)


cv2.waitKey(0)
cv2.destroyAllWindows()
