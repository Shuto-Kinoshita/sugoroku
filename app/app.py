from flask import Flask, render_template, request
from models.models import OnegaiContent
from models.database import db_session
from datetime import datetime

import imagecr

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/form")
def form():
    return render_template("formselect.html")

@app.route("/input")
def index():
    all_onegai = OnegaiContent.query.all()
    return render_template("contentsinput.html", all_onegai=all_onegai)


@app.route("/output", methods=["post"])
def t4():
    all_onegai = OnegaiContent.query.all()
    imagecr.imagecreate(3, 5, all_onegai)
    return render_template('mapoutput.html')

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