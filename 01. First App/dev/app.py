from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    days = ['월요일', '화요일', '수요일', '목요일', '금요일']
    menu = ['오코토 제육', '나이스샤워 텐동', '뤠벤 돈가스', '타코벨', '맘스터치', '이어곰탕', '반계탕', '한산주 순대국', 'Johnson 샌드위치']

    # print(f"오늘은 {days[datetime.datetime.today().weekday()]} 입니다")
    # print(f"오늘의 메뉴는 {menu[random.randint(0, len(menu)-1)]}입니다")

    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/menu')
def menu():
    menu = ['오코토 제육', '나이스샤워 텐동', '뤠벤 돈가스', '타코벨', '맘스터치', '이어곰탕', '반계탕', '한산주 순대국', 'Johnson 샌드위치']

    return f"오늘의 메뉴를 알려줄게! 오늘은 바로 {menu[random.randint(0, len(menu)-1)]} 먹는 날이야!"