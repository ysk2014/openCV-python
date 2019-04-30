import numpy as np
import cv2


def nothing(x):
    pass


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)


'''
创建滑动条

- trackbarName 滑动条的名字
- windowName 放置窗口的名字
- value 默认位置
- count 滑动条的最大值
- onChange 改变触发事件
'''
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    print(r, g, b)
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
