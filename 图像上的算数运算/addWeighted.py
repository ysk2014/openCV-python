import numpy as np
import cv2


# 图像混合
img1 = cv2.imread('../data/ml.png')
img2 = cv2.imread('../data/opencv_logo.png')

img1 = cv2.resize(img1, (599, 555))

# dst = α · img1 + β · img2 + γ
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)


cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
