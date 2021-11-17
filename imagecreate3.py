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

    #背景に画像を挿入１
    def cvpaste(img, imgback, x, y, angle, scale):
        # x and y are the distance from the center of the background image

        r = img.shape[0]
        c = img.shape[1]
        rb = imgback.shape[0]
        cb = imgback.shape[1]
        hrb = round(rb/2)
        hcb = round(cb/2)
        hr = round(r/2)
        hc = round(c/2)

        # Copy the forward image and move to the center of the background image
        imgrot = np.zeros((rb,cb,3),np.uint8)
        imgrot[hrb-hr:hrb+hr,hcb-hc:hcb+hc,:] = img[:hr*2,:hc*2,:]

        # Rotation and scaling
        M = cv2.getRotationMatrix2D((hcb,hrb),angle,scale)
        imgrot = cv2.warpAffine(imgrot,M,(cb,rb))
        # Translation
        M = np.float32([[1,0,x],[0,1,y]])
        imgrot = cv2.warpAffine(imgrot,M,(cb,rb))

        # Makeing mask
        imggray = cv2.cvtColor(imgrot,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(imggray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        # Now black-out the area of the forward image in the background image
        img1_bg = cv2.bitwise_and(imgback,imgback,mask = mask_inv)

        # Take only region of the forward image.
        img2_fg = cv2.bitwise_and(imgrot,imgrot,mask = mask)

        # Paste the forward image on the background image
        imgpaste = cv2.add(img1_bg,img2_fg)

        return imgpaste

    imgback = np.full((750, 1050, 3), (150, 180, 200), dtype=np.uint8)
    imge = cv2.imread('app/static/images/contentsimg/img8.jpg')

    x = -60
    y = 70
    angle = 20
    scale = 0.7

    #img = cvpaste(imge, imgback, x, y, angle, scale)




    # 255:白　128:灰色　0:黒    単色画像または画像挿入
    img = np.full((730, 1050, 3), 77, dtype=np.uint8)
    #img = cv2.imread('app/static/images/party_cracker_kamifubuki.png')

    #for i in range(10):
        #cv2.drawMarker(img, ((i + 1) * 50, 0), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=100)

    # cv2.rectangle() 長方形
    for i in range(5):
        cv2.rectangle(img, (50, 30 + (i * 140)), (200, 130 + (i * 140)), (130, 255, 60), thickness=3, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (450, 30 + (i * 140)), (600, 130 + (i * 140)), (220, 220, 70), thickness=3, lineType=cv2.LINE_AA)

    for i in range(5):
        cv2.rectangle(img, (850, 30 + (i * 140)), (1000, 130 + (i * 140)), (150, 110, 230), thickness=3, lineType=cv2.LINE_AA)

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

    # cv2.line() ライン縦左
    for i in range(2):
        cv2.line(img, (125, 270 + (i * 280)), (125, 310 + (i * 280)), (240, 255, 255), thickness=7, lineType=cv2.LINE_AA)

    # cv2.line() ライン縦右
    for i in range(2):
        cv2.line(img, (925, 130 + (i * 280)), (925, 170 + (i * 280)), (240, 255, 255), thickness=7, lineType=cv2.LINE_AA)

    base = Image.fromarray(img)
    draw = ImageDraw.Draw(base)
    font_path = '/download/SatsukiGendaiMincho-M.ttf'
    font_size = 15
    font = ImageFont.truetype(font_path, font_size)
    #　入力された文字を枠に入れる
    k = 1
    a = 0
    all_onegai = OnegaiContent.query.all()
    b = len(all_onegai)
    for i in range(5):
        for j in range(3):
            con = OnegaiContent.query.filter_by(id=k).first()
            if a % 2 == 0:
                draw.text(xy=(55+j*400, 35+i*140), text=con.title, font=font, fill=(200, 200, 200, 10))
                draw.text(xy=(55+j*400, 55+i*140), text=con.body, font=font, fill=(200, 200, 200, 10))
            else:
                draw.text(xy=(855-j*400, 35+i*140), text=con.title, font=font, fill=(200, 200, 200, 10))
                draw.text(xy=(855-j*400, 55+i*140), text=con.body, font=font, fill=(200, 200, 200, 10))
            k = k+1
            if k == b+1:
                break
        else:
            a = a + 1
            continue
        break

    base = np.array(base)  # 画像をOpencv形式(ndarray)に変更


    cv2.imwrite('app/static/images/kidoyuki3.png', base)
    # True
