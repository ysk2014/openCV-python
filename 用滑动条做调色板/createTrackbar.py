import numpy as np
import cv2


def nothing(x):
    pass


drawing = False
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

    color = (r, g, b)

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            cv2.circle(img, (x, y), 5, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

cv2.setMouseCallback('image', draw_circle)


while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
