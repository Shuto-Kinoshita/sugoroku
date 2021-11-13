def imagecreate():
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    import io
    import sys
    from models.models import OnegaiContent
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print(cv2.__version__)
    # 3.3.0

    #背景に画像を挿入２
    import cv2
    import numpy as np

    back_img = np.full((750, 1050, 3), 77, dtype=np.uint8)
    fore_img = cv2.imread('app/static/images/pumpkin-g0e211d582_1280.jpg')
    h, w = back_img.shape[:2]

    dx = 0
    dy = 0
    M = np.array([[1, 0, dx], [0, 1, dy]], dtype=float)
    img = cv2.warpAffine(fore_img, M, (w, h), back_img, borderMode=cv2.BORDER_TRANSPARENT)


    # 255:白　128:灰色　0:黒    単色画像または画像挿入
    #img = np.full((730, 1050, 3), 77, dtype=np.uint8)


    #for i in range(10):
        #cv2.drawMarker(img, ((i + 1) * 50, 0), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=100)

    # cv2.rectangle() 長方形
    for i in range(5):
        cv2.rectangle(img, (40, 30 + (i * 140)), (200, 130 + (i * 140)), (130, 255, 60), thickness=2, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (201, 30 + (i * 140)), (361, 130 + (i * 140)), (150, 110, 230), thickness=2, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (362, 30 + (i * 140)), (527, 130 + (i * 140)), (220, 220, 70), thickness=2, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (528, 30 + (i * 140)), (688, 130 + (i * 140)), (130, 255, 60), thickness=2, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (689, 30 + (i * 140)), (849, 130 + (i * 140)), (150, 110, 230), thickness=2, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (850, 30 + (i * 140)), (1010, 130 + (i * 140)), (220, 220, 70), thickness=2, lineType=cv2.LINE_AA)

    '''
    # cv2.line() ライン横
    for i in range(2):
        cv2.line(img, (200 + (i * 400), 80), (450 + (i * 400), 80), (240, 255, 255), thickness=5, lineType=cv2.LINE_AA)
    
    for i in range(2):
        cv2.line(img, (200 + (i * 400), 220), (450 + (i * 400), 220), (240, 255, 255), thickness=5, lineType=cv2.LINE_AA)
    
    for i in range(2):
        cv2.line(img, (200 + (i * 400), 360), (450 + (i * 400), 360), (240, 255, 255), thickness=5, lineType=cv2.LINE_AA)
    
    for i in range(2):
        cv2.line(img, (200 + (i * 400), 500), (450 + (i * 400), 500), (240, 255, 255), thickness=5, lineType=cv2.LINE_AA)
    
    for i in range(2):
        cv2.line(img, (200 + (i * 400), 640), (450 + (i * 400), 640), (240, 255, 255), thickness=5, lineType=cv2.LINE_AA)
    '''

    # cv2.line() ライン縦左
    for i in range(2):
        cv2.line(img, (125, 270 + (i * 280)), (125, 310 + (i * 280)), (240, 255, 255), thickness=2, lineType=cv2.LINE_AA)

    # cv2.line() ライン縦右
    for i in range(2):
        cv2.line(img, (925, 130 + (i * 280)), (925, 170 + (i * 280)), (240, 255, 255), thickness=2, lineType=cv2.LINE_AA)


    base = Image.fromarray(img)
    draw = ImageDraw.Draw(base)
    font_path = 'C:\Windows\Fonts\BIZ-UDMinchoM.ttc'
    font_size = 10
    font = ImageFont.truetype(font_path, font_size)
    #　入力された文字を枠に入れる
    k = 1
    a = 0
    for i in range(5):
        for j in range(6):
            #con = OnegaiContent.query.filter_by(id=k).first()
            if a % 2 == 0:
                draw.text(xy=(44+j*162, 32+i*140), text="aaaaa", font=font, fill=(255, 255, 255, 10))
                draw.text(xy=(44+j*162, 52+i*140), text="body", font=font, fill=(255, 255, 255, 10))
            else:
                draw.text(xy=(854-j*162, 32+i*140), text="con", font=font, fill=(255, 255, 255, 10))
                draw.text(xy=(854-j*162, 52+i*140), text="con", font=font, fill=(255, 255, 255, 10))
            k = k+1
        a = a+1


    base = np.array(base)  # 画像をOpencv形式(ndarray)に変更

    cv2.imwrite('kidoyuki4.png', base)
    # True
