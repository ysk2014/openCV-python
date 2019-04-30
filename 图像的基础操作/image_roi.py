import numpy as np
import cv2


img = cv2.imread('../data/messi5.jpg')

ball = img[280:340, 330:390]

img[100:160, 200:260] = ball

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
