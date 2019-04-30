import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)

'''
警告：
所有的绘图函数的返回值都是 None，所以不能使用 
img =cv2.line(img,(0,0),(511,511),(255,0,0),5)。
'''


'''
- pt1为左上角起始坐标
- pt2为右下角终点坐标
- color：形状的颜色。以RGB为例  需要传入一个元组BGR 例如 255,0,0 
- thickness 线条的粗细。如果给一个闭合图形 置为 -1  那么这个图形就会被填充。 默认值是 1.
'''
cv2.line(img, pt1=(0, 0), pt2=(511, 511), color=(255, 0, 0), thickness=5)
cv2.arrowedLine(img, pt1=(21, 13), pt2=(151, 401),
                color=(255, 0, 0), thickness=5)
cv2.rectangle(img, pt1=(384, 0), pt2=(510, 128),
              color=(0, 255, 0), thickness=3)

'''
- center 圆心中点
- radius 圆的半径
- color 形状颜色
- thickness 线条粗细
- lineType 线条的类型， 8 连接，抗锯齿等。  默认情况是8 连接。cv2.LINE_AA为抗锯齿  这样看起来会非常平滑。
'''
cv2.circle(img, center=(447, 63), radius=63, color=(
    0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

'''
- center 圆心中点
- axes 轴线，分为长轴和短轴
- angle 椭圆沿逆时针方向旋转的角度。
- startAngle 椭圆弧沿顺时方向起始的角度
- endAngle 椭圆弧沿顺时方向结束的角度
- color 形状颜色
- thickness 线条粗细
- lineType 线条的类型， 8 连接，抗锯齿等。  默认情况是8 连接。cv2.LINE_AA为抗锯齿  这样看起来会非常平滑。
'''
cv2.ellipse(img, center=(256, 256), axes=(100, 50), angle=0,
            startAngle=0, endAngle=180, color=(0, 255, 0), thickness=-1)


# cv2.polylines() 可以 用来画很多条线。只需要把想 画的线放在一 个列表中， 将 列表传给函数就可以了。每条线 会被独立绘制。 这会比用 cv2.line() 一条一条的绘制 要快一些。
# cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 30]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, pts, True, (0, 255, 255), 5)

'''
- text 绘制的文字
- org 绘制的位置坐标
- fontFace 字体类型
- fontScale 字体大小
- color 字体颜色
- bottomLeftOrigin=True,文字会上下颠倒
'''
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text="openCV", org=(10, 500), fontFace=font, fontScale=4,
            color=(255, 255, 255), thickness=5, lineType=cv2.LINE_AA)
cv2.putText(img, text='bottomLeftOrigin', org=(10, 400), fontFace=font, fontScale=1, color=(
    255, 255, 255), thickness=1, bottomLeftOrigin=True)  # text, org, fontFace, fontScale, color, thickness=

cv2.imshow('line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
