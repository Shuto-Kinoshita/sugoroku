import os
from flask import Flask, render_template, request, redirect, session
from models.models import OnegaiContent
from models.database import db_session
from models2.models2 import mapContent
from models2.database2 import db_session2
from datetime import datetime
from werkzeug.utils import secure_filename

import imagecr
import imagecreate3
import imagecreate4

UPLOAD_FOLDER = './app/static/images/contentsimg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif', 'pdf', 'heic'}

# Flaskオブジェクトの生成
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def de():
    all_onegai = OnegaiContent.query.all()
    for onegai in all_onegai:
        print(onegai.title)
    return render_template("index3.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/mapreset")
def mapreset():
    #database初期化処理

    return render_template("formselect.html")

@app.route("/form")
def form():
    return render_template("formselect.html")

@app.route("/input0", methods=["post"])
def index0():
    con = mapContent.query.filter_by(id=1).first()
    con.map = request.form["map"]
    db_session2.commit()
    map1 = con.map
    all_onegai = OnegaiContent.query.all()
    i = 1
    for onegai in all_onegai:
        onegai.id = i
        i = i + 1
    db_session.commit()
    count = len(all_onegai)
    return render_template("contentsinput.html", all_onegai=all_onegai, count=count, map=map1)


@app.route("/input", methods=["post"])
def index():
    con = mapContent.query.filter_by(id=1).first()
    map = con.map
    all_onegai = OnegaiContent.query.all()
    i = 1
    for onegai in all_onegai:
        onegai.id = i
        i = i + 1
    db_session.commit()
    count = len(all_onegai)
    return render_template("contentsinput.html", all_onegai=all_onegai, count=count, map=map)


@app.route("/output", methods=["post"])
def t4():
    con = mapContent.query.filter_by(id=1).first()
    map = con.map
    if map == 15:
        print(map)
        imagecr.imagecreate()
    elif map == 25:
        print("b")
        imagecreate3.imagecreate()
    else:
        print("a")
        imagecreate3.imagecreate()
    return render_template('mapoutput.html')


@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title, body, datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()


@app.route("/update", methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    print(request.form["update"])
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()


@app.route("/up", methods=["post"])
def up():
    if int(request.form["up"]) > 1:
        j1 = int(request.form["up"]) - 1
        con2 = OnegaiContent.query.filter_by(id=str(j1)).first()
        con4 = con2.title
        con5 = con2.body
        con2.title = "a"
        con1 = OnegaiContent.query.filter_by(id=request.form["up"]).first()
        con6 = con1.title
        con7 = con1.body
        con1.title = con4
        con1.body = con5
        db_session.commit()
        con2.title = con6
        con2.body = con7
        db_session.commit()
        return index()
    else:
        return index()


@app.route("/down", methods=["post"])
def down():
    if int(request.form["down"]) < (OnegaiContent.query.count() - 1):
        j1 = int(request.form["down"]) + 1
        con1 = OnegaiContent.query.filter_by(id=request.form["down"]).first()
        con6 = con1.title
        con7 = con1.body
        con1.title = "e"
        con2 = OnegaiContent.query.filter_by(id=str(j1)).first()
        con4 = con2.title
        con5 = con2.body
        con2.title = con6
        con2.body = con7
        db_session.commit()
        con1.title = con4
        con1.body = con5
        db_session.commit()
        return index()
    else:
        return index()


@app.route("/delete", methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()


# ファイルを受け取る方法の指定
@app.route('/getimg', methods=['GET', 'POST'])
def uploads_file():
    print(request.form["file_id"])
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            print('ファイルがありません')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            print('ファイルがありません')
            return redirect(request.url)
        # ファイルのチェック
        if file and allowed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイル名をマス番号に変更
            filename = request.form["file_id"] + '.' +filename.rsplit('.', 1)[1].lower()
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return index()


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
