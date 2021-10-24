import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0


# 255:白　128:灰色　0:黒    単色画像
img = np.full((750, 1300, 3), 128, dtype=np.uint8)

#for i in range(10):
    #cv2.drawMarker(img, ((i + 1) * 50, 0), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=100)

# cv2.rectangle() 長方形
for i in range(5):
    cv2.rectangle(img, (50, 30 + (i * 140)), (200, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (250, 30 + (i * 140)), (400, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (450, 30 + (i * 140)), (600, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (650, 30 + (i * 140)), (800, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (850, 30 + (i * 140)), (1000, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (1050, 30 + (i * 140)), (1200, 130 + (i * 140)), (255, 0, 0))

# cv2.line() ライン横
for i in range(5):
    cv2.line(img, (200 + (i * 200), 80), (250 + (i * 200), 80), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(5):
    cv2.line(img, (200 + (i * 200), 220), (250 + (i * 200), 220), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(5):
    cv2.line(img, (200 + (i * 200), 360), (250 + (i * 200), 360), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(5):
    cv2.line(img, (200 + (i * 200), 500), (250 + (i * 200), 500), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(5):
    cv2.line(img, (200 + (i * 200), 640), (250 + (i * 200), 640), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.line() ライン縦左
for i in range(2):
    cv2.line(img, (125, 270 + (i * 280)), (125, 310 + (i * 280)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.line() ライン縦右
for i in range(2):
    cv2.line(img, (1125, 130 + (i * 280)), (1125, 170 + (i * 280)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

#img = cv2.imread('app/static/images/kidoyuki2.png')

cv2.imwrite('app/static/images/kidoyuki.png', img)
# True

