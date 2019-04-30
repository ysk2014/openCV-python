import numpy as np
import cv2


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('im')
cv2.setMouseCallback('im', draw_circle)

while True:
    cv2.imshow('im', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
