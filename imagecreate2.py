import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(cv2.__version__)
# 3.3.0


# 255:白　128:灰色　0:黒    単色画像
img = np.full((730, 1250, 3), 128, dtype=np.uint8)


#for i in range(10):
    #cv2.drawMarker(img, ((i + 1) * 50, 0), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=100)

# cv2.rectangle() 長方形
for i in range(5):
    cv2.rectangle(img, (50, 30 + (i * 140)), (200, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (450, 30 + (i * 140)), (600, 130 + (i * 140)), (255, 0, 0))

for i in range(5):
    cv2.rectangle(img, (850, 30 + (i * 140)), (1000, 130 + (i * 140)), (255, 0, 0))

j=50
k=200
for j in range(3):
    for i in range(5):
        cv2.rectangle(img, (j, 30 + (i * 140)), (k, 130 + (i * 140)), (255, 0, 0))
    j=j+400
    k=k+400



# cv2.line() ライン横
for i in range(2):
    cv2.line(img, (200 + (i * 400), 80), (450 + (i * 400), 80), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(2):
    cv2.line(img, (200 + (i * 400), 220), (450 + (i * 400), 220), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(2):
    cv2.line(img, (200 + (i * 400), 360), (450 + (i * 400), 360), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(2):
    cv2.line(img, (200 + (i * 400), 500), (450 + (i * 400), 500), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(2):
    cv2.line(img, (200 + (i * 400), 640), (450 + (i * 400), 640), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.line() ライン横右
for i in range(4):
    cv2.line(img, (1000, 80 + (i * 140)), (1120, 80 + (i * 140)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.line() ライン縦左
for i in range(2):
    cv2.line(img, (125, 270 + (i * 280)), (125, 310 + (i * 280)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.line() ライン縦右
for i in range(2):
    cv2.line(img, (1125, 80 + (i * 280)), (1125, 220 + (i * 280)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

cv2.circle(img, (200, 200), 5, (255, 255, 255), thickness=-1)
cv2.circle(img, (100, 100), 5, (255, 255, 255), thickness=-1)
cv2.circle(img, (100, 200), 5, (255, 255, 255), thickness=-1)

base = Image.fromarray(img)
draw = ImageDraw.Draw(base)
font_path = '/download/SatsukiGendaiMincho-M.ttf'
font_size = 10
font = ImageFont.truetype(font_path, font_size)
draw.text(xy=(100, 200), text='3マス進む', font=font, fill=(255, 255, 255, 10))

base = np.array(base)  # 画像をOpencv形式(ndarray)に変更

cv2.imwrite('app/static/images/kidoyuki3.png', base)
# True