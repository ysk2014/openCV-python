import numpy as np
import cv2

img = cv2.imread('../data/messi5.jpg')

cv2.imshow('original', img)

cv2.waitKey(0)


"""
add—图像矩阵相加

函数原型：cv2.add(src1, src2, dst=None, mask=None, dtype=None)

src1：图像矩阵1

src1：图像矩阵2

dst：默认选项

mask：默认选项

dtype：默认选项
"""

M = np.ones(img.shape, np.uint8) * 100
added = cv2.add(img, M)
cv2.imshow("Added", added)
cv2.waitKey(0)
