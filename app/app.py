# coding=utf-8
# ライブラリ、モジュールのインポート
import os
from flask import Flask, render_template, request, redirect
import glob
import shutil
# データベース
from models.models import OnegaiContent
from models.database import db_session
from models2.models2 import mapContent
from models2.database2 import db_session2
# ファイル名処理
from werkzeug.utils import secure_filename

# すごろく作成関数
import imagecr
import imagecreate5
import imagecreate3
import imagecreate4

UPLOAD_FOLDER = './app/static/images/contentsimg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif', 'pdf', 'heic'}

# Flaskオブジェクトの生成
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# .があるかどうかのチェックと、拡張子の確認
def allowed_file(filename):
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 練習
@app.route("/")
def de():
    all_onegai = OnegaiContent.query.all()
    for onegai in all_onegai:
        print(onegai.title)
    return render_template("contentsinput.html", all_onegai=all_onegai)

# スタートページ出力
@app.route("/start")
def start():
    return render_template("start.html")

# すごろくデータベースの初期化
@app.route("/mapreset")
def mapreset():
    # database初期化処理
    all_onegai = OnegaiContent.query.all()
    for onegai in all_onegai:
        content = OnegaiContent.query.filter_by(id=onegai.id).first()
        db_session.delete(content)
    db_session.commit()
    # マス画像フォルダの初期化
    shutil.rmtree('app/static/images/contentsimg')
    os.mkdir('app/static/images/contentsimg')
    return render_template("formselect1.html")

# フォーマット選択ページ
@app.route("/form")
def form():
    return render_template("formselect1.html")


# マス目情報入力ページ　ファーマット選択ページから遷移してきた時
@app.route("/input0", methods=["post"])
def index0():
    # フォーマットのマス数をデータベースに格納
    con = mapContent.query.filter_by(id=1).first()
    con.map = request.form["map"]
    db_session2.commit()
    map1 = con.map
    # マス目情報のidを振り直す
    all_onegai = OnegaiContent.query.all()
    i = 1
    for onegai in all_onegai:
        onegai.id = i
        i = i + 1
    db_session.commit()
    # 現在入力されているマス目の数をカウント
    count = len(all_onegai)
    flist = glob.glob('app/static/images/contentsimg/*')
    return render_template("contentsinput2.html", all_onegai=all_onegai, count=count, map=map1, flist=flist)


# マス目情報入力ページ
@app.route("/input", methods=["post"])
def index():
    # フォーマットのマス数を呼び出し
    con = mapContent.query.filter_by(id=1).first()
    map = con.map
    # マス目情報のidを指定
    all_onegai = OnegaiContent.query.all()
    i = 1
    for onegai in all_onegai:
        onegai.id = i
        i = i + 1
    db_session.commit()
    # 現在入力されているマス目の数をカウント
    count = len(all_onegai)
    flist = glob.glob('app/static/images/contentsimg/*')
    return render_template("contentsinput2.html", all_onegai=all_onegai, count=count, map=map, flist=flist)


# 完成すごろく出力ページ
@app.route("/output", methods=["post"])
def t4():
    # フォーマットのマス数を呼び出し
    con = mapContent.query.filter_by(id=1).first()
    map = con.map
    print(map)
    # マス数によってそれぞれのすごろく作成プログラムを実行
    if int(map) == 15:
        print("c")
        imagecreate5.imagecreate()
    elif int(map) == 20:
        print("b")
        imagecreate3.imagecreate()
    else:
        print("ab")
        imagecreate4.imagecreate()
    return render_template('mapoutput.html')


# マス目追加
@app.route("/add", methods=["post"])
def add():
    # titleの情報が他のマスと被っていないか確認
    all_onegai = OnegaiContent.query.all()
    title = request.form["title"]
    for onegai in all_onegai:
        # 被っていたら後ろに"."をつける
        if onegai.title == title:
            title = title+"."
    # bodyを格納
    body = request.form["body"]
    content = OnegaiContent(title, body)
    # 新しいマスを加える
    db_session.add(content)
    db_session.commit()
    return index()


# マス目更新
@app.route("/update", methods=["post"])
def update():
    # 上書きボタンが押されていない時の処理
    if request.form["update"] == "":
        print("a")
        return index()
    # 上書きボタンが押されている時の処理
    else:
        # 選択されているマスを読み込む
        content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
        all_onegai = OnegaiContent.query.all()
        # titleの情報が他のマスと被っていないか確認
        title = request.form["title"]
        for onegai in all_onegai:
            # 被っていたら後ろに"."をつける
            if onegai.title == title:
                title = title + "."
        # titleとbodyを格納
        content.title = title
        content.body = request.form["body"]
        db_session.commit()
        return index()


# 前のマスと入れ替え
@app.route("/up", methods=["post"])
def up():
    # 1番最初のマスではなかった時の処理
    if int(request.form["up"]) > 1:
        # 前のマスの情報を読み込む
        j1 = int(request.form["up"]) - 1
        con2 = OnegaiContent.query.filter_by(id=str(j1)).first()
        con4 = con2.title
        con5 = con2.body
        con2.title = "a"
        # ↑が押されたマスの情報を読み込む
        con1 = OnegaiContent.query.filter_by(id=request.form["up"]).first()
        con6 = con1.title
        con7 = con1.body
        # 前後を入れ替える
        con1.title = con4
        con1.body = con5
        db_session.commit()
        con2.title = con6
        con2.body = con7
        db_session.commit()
        return index()
    # 1番最初のマスであった時の処理
    else:
        return index()


# 後ろのマスと入れ替え
@app.route("/down", methods=["post"])
def down():
    # 1番最後のマスではなかった時の処理
    if int(request.form["down"]) < (OnegaiContent.query.count() - 1):
        # 後ろのマスの情報を読み込む
        j1 = int(request.form["down"]) + 1
        con1 = OnegaiContent.query.filter_by(id=request.form["down"]).first()
        con6 = con1.title
        con7 = con1.body
        con1.title = "e"
        # ↓が押されたマスの情報を読み込む
        con2 = OnegaiContent.query.filter_by(id=str(j1)).first()
        con4 = con2.title
        con5 = con2.body
        # 前後を入れ替える
        con2.title = con6
        con2.body = con7
        db_session.commit()
        con1.title = con4
        con1.body = con5
        db_session.commit()
        return index()
    # 1番最後のマスであった時の処理
    else:
        return index()


# 選択したマスの削除
@app.route("/delete", methods=["post"])
def delete():
    # 削除を選択されたマスのidリストを読み込む
    id_list = request.form.getlist("delete")
    # 読み込んだidにしたがって順に削除する
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
            return index()
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            print('ファイルがありません')
            return index()
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
