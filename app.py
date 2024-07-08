# import random
import json
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
from flask_sqlalchemy import SQLAlchemy


# DB 코드
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)

db = SQLAlchemy(app)


class RPSGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), primary_key=False)
    computer = db.Column(db.String(100), primary_key=False)
    result = db.Column(db.String(100), primary_key=False)
    win = db.Column(db.Integer, primary_key=False)
    lose = db.Column(db.Integer, primary_key=False)
    draw = db.Column(db.Integer, primary_key=False)
    GameDay = db.Column(db.String(100), primary_key=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), primary_key=False)
    password = db.Column(db.String(100), primary_key=False)


with app.app_context():
    db.create_all()

rsplist = ["가위", "바위", "보"]  # 가위바위보 양식 맞는지 비교용
regame = "y"
check = [
    "n",
    "N",
    "아니요",
    "아니",
    "y",
    "Y",
    "네",
]  # 다시 할지 안할지 물어볼때 양식 맞는지 비교용
reports = {"win": 0, "lose": 0, "draw": 0}  # 전역 변수 선언
finish = ""


@app.route("/")
def view():
    return 'mainpage<a href="/signin">로그인</a><br><a href="/signup">회원가입</a>'


# 로그인 폼
@app.route("/signin")
def signin():
    return render_template("signin.html")


# 회원가입 폼
@app.route("/signup")
def signupweb():
    return render_template("signup.html")


# 로그인 하면 처리하러 오는곳
@app.route("/signin_data", methods=["POST"])
def signin_data():
    username = request.form["username"]
    password = request.form["password"]

    # 아이디 비번 짝 맞으면 로그인 성공
    id = User.query.filter_by(username=username).first()
    if id:
        print("id exist")
        if id.password == password:
            print("로그인 성공")
            return redirect(
                url_for("home")
            )  # 로그인 성공하면 메인 주소로 보내기(home바꾸기)
        else:
            print("incorrect")
            return redirect(url_for("signin"))
    else:
        print("id not exist")
        return redirect(url_for("signin"))


# 회원가입 하면 처리하러 오는곳
@app.route("/signup_data", methods=["POST"])
def signup_data():
    username = request.form["username"]
    password = request.form["password"]

    # 이미 아이디가 있는 경우
    if User.query.filter_by(username=username).first():
        print("already exist")
        return redirect(url_for("signin"))  # 아이디가 있으니 로그인 화면으로

    # 아이디가 없으면 생성
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    print("회원가입 완료")
    return redirect(url_for("signin"))  # 회원가입 후 로그인하러home으로


@app.route("/game")  # 가위바위보 고르는 페이지, 모달에서 처리 했던것 처럼 값을 보냄
def home():
    global reports  # 20240704: 전역 변수 수정 시 global를 선언해줘야한다.
    record = RPSGame.query.all()
    record.reverse()  # DB 최근 등록 순으로 불러오기
    # 1번부터 출력할지 마지막부터 출력할지 회의

    if bool(record):
        reports = {"win": record[0].win, "lose": record[0].lose, "draw": record[0].draw}

    # 전역 변수 reports 읽기 및 참조
    return render_template("index.html", record=record, reports=reports)


# @app.route('/receive/data/', methods=['POST'])
@app.route(
    "/top_users/"
)  # 상위 10명의 사용자를 표시하는 모달. (버튼 눌러서 모달을 띄우고 다시 닫을 수 있는 방식으로 구현)
def top_users():
    # 많이 승리한 사용자 순으로 정렬하며 동점자의 경우 적게 패배한 사용자가 높이 랭킹.
    top_users = (
        RPSGame.query.order_by(RPSGame.win.desc(), RPSGame.lose.asc()).limit(10).all()
    )
    return render_template("top_users.html", top_users=top_users)


@app.route("/receive/data/", methods=["POST"])
def get_data():

    today = datetime.now()
    user = request.form.get("user")
    computer = request.form.get("ComputerVal")
    result = ""

    if computer == user:
        result = "무"
        reports["draw"] += 1
    elif rsplist[rsplist.index(user) - 1] == computer:
        result = "승"
        reports["win"] += 1
    elif rsplist[rsplist.index(user) - 2] == computer:
        result = "패"
        reports["lose"] += 1

    game = RPSGame(
        user=user,
        computer=computer,
        result=result,
        win=reports["win"],
        lose=reports["lose"],
        draw=reports["draw"],
        GameDay=today.strftime("%Y-%m-%d"),
    )
    db.session.add(game)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
