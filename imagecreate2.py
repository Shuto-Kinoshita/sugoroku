import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
import sys
import os
import re
import glob
from models.models import OnegaiContent
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

# 画像入れ
def add(f1, f2, top, left):
    img = Image.open(f1)
    img_resize = img.resize((100, 100))
    img_resize.save(f1)

    img1 = cv2.imread(f1)
    img2 = cv2.imread(f2)

    height, width = img1.shape[:2]
    img2[top:height + top, left:width + left] = img1

    cv2.imwrite('app/static/images/kidoyuki3.png', img2)


flist = glob.glob('app/static/images/contentsimg/*')
b_path = 'app/static/images/kidoyuki3.png'
for fname in flist:
    print(fname.split('.')[0])
a = 1
b = 0
for i in range(5):
    for j in range(3):
        for fname in flist:
            if fname.split('.')[0] == "app/static/images/contentsimg/"+str(a) and b == 0:
                add(fname, b_path, 50+150*i, 50+500*j)
                b = 1
                print(j)
        a = a+1
        b = 0


# 文字入れ
base = Image.fromarray(img)
draw = ImageDraw.Draw(base)
font_path = '/download/SatsukiGendaiMincho-M.ttf'
font_size = 20
font = ImageFont.truetype(font_path, font_size)
k = 1
a = 0
for i in range(5):
    for j in range(3):
        con = OnegaiContent.query.filter_by(id=k).first()
        if a % 2 == 0:
            draw.text(xy=(50+j*400, 30+i*140), text=con.title, font=font, fill=(255, 255, 255, 10))
            draw.text(xy=(50+j*400, 50+i*140), text=con.body, font=font, fill=(255, 255, 255, 10))
        else:
            draw.text(xy=(850-j*400, 30+i*140), text=con.title, font=font, fill=(255, 255, 255, 10))
            draw.text(xy=(850-j*400, 50+i*140), text=con.body, font=font, fill=(255, 255, 255, 10))
        k = k+1
    a = a+1

base = np.array(base)  # 画像をOpencv形式(ndarray)に変更

#cv2.imwrite('app/static/images/kidoyuki3.png', base)
# True