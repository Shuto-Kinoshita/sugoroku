from flask import Flask, render_template, request
from models.models import OnegaiContent
from models.database import db_session
from datetime import datetime

import imagecr

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    name = request.args.get("name")
    all_onegai = OnegaiContent.query.all()
    okyo = ["色不異空","空不異色","色即是空","空即是色"]
    return render_template("index.html", name=name, okyo=okyo, all_onegai=all_onegai)


@app.route("/t4", methods=["post"])
def t4():
    name = request.form["name"]
    return render_template('index3.html', name=name)

@app.route("/cr", methods=["post"])
def callimage():
    all_onegai = OnegaiContent.query.all()
    print(imagecr.imagecreate(3, 5, all_onegai))
    return render_template('index3.html')

@app.route("/index",methods=["post", "get"])
def post():
    name = request.form["name"]
    all_onegai = OnegaiContent.query.all()
    okyo = ["色不異空", "空不異色", "色即是空", "空即是色"]
    return render_template("index.html", name=name, okyo=okyo, all_onegai=all_onegai)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()

@app.route("/update",methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

#おまじない
if __name__ == "__main__":
    app.run(debug=True)