from flask import Flask,render_template,request
from data import data
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():

    warpid = request.form.get("warpid")
    id = request.form.get("id")
    password = request.form.get("password")
    print('warpid=',warpid)
    print('id=',id)
    print('password=',warpid)

    if id == "admin" and password == "admin":
        datas = data()
        datas.final(warpid)
        return render_template("sucess.html")
    else:
        return render_template("failure.html")

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=random.randint(2000,9000))