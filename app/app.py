import os
from flask import Flask, render_template, request, redirect
from models.models import OnegaiContent
from models.database import db_session
from datetime import datetime
from werkzeug.utils import secure_filename

import imagecr

UPLOAD_FOLDER = './app/static/images/contentsimg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif', 'pdf', 'heic'}

# Flaskオブジェクトの生成
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/form")
def form():
    return render_template("index3.html")


@app.route("/input")
def index():
    all_onegai = OnegaiContent.query.all()
    i = 1
    for onegai in all_onegai:
        onegai.id = i
        i = i + 1
    db_session.commit()
    return render_template("contentsinput.html", all_onegai=all_onegai)


@app.route("/output", methods=["post"])
def t4():
    all_onegai = OnegaiContent.query.all()
    print(imagecr.imagecreate(3, 5, all_onegai))
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
        con3 = con2.id
        con4 = con2.title
        con5 = con2.body
        con2.title = "a"
        print(con5, con4, con3)
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
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイル名をマス番号に変更
            # filename = request.form["file_id"] + filename.rsplit('.', 1)[1].lower()
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return index()


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
