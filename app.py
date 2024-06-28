import random
from flask import Flask, render_template, request

rsplist = ['가위', '바위', '보']  # 가위바위보 양식 맞는지 비교용
regame = 'y'
check = ['n', "N", "아니요", "아니", "y", "Y", "네"]  # 다시 할지 안할지 물어볼때 양식 맞는지 비교용
reports = {'win': 0, 'lose': 0, 'draw': 0}
finish = ''

app = Flask(__name__)


@app.route("/")  # 가위바위보 고르는 페이지, 모달에서 처리 했던것 처럼 값을 보냄
def home():
    return render_template('index.html')


@app.route("/rock/")  # 값 받고 계산해서 출력
def rock():
    button = request.args.get("button")
    print(f'User selected: {button}')
    return f'You selected: {button}'

@app.route("/sissor/")  # 값 받고 계산해서 출력
def sissor():
    button = request.args.get("button")
    print(f'User selected: {button}')
    return f'You selected: {button}'

@app.route("/paper/")  # 값 받고 계산해서 출력
def paper():
    button = request.args.get("button")
    print(f'User selected: {button}')
    return f'You selected: {button}'


if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/music/create/")#모달에서 처리하던 코드
# def music_create():
#     username_receive = request.args.get("username")
#     title_receive = request.args.get("title")
#     artist_receive = request.args.get("artist")
#     image_receive = request.args.get("image_url")
#     return redirect(url_for('Introduce'))

# rsplist = ['가위', '바위', '보']  # 가위바위보 양식 맞는지 비교용
# regame = 'y'
# check = ['n', "N", "아니요", "아니", "y", "Y", "네"]  # 다시 할지 안할지 물어볼때 양식 맞는지 비교용
# reports = {'win': 0, 'lose': 0, 'draw': 0}
# finish = ''
# while regame not in check[0:4]:
#     computer = rsplist[random.randint(0, 2)]
#     user = input('가위, 바위, 보 중 하나를 선택하세요 : ')
#     user = user.replace(" ", "")  # 빈 공간 제거
#     while user not in rsplist:
#         print('유효한 입력이 아닙니다. 제대로 입력 해 주세요!!!')
#         user = input('가위, 바위, 보 중 하나를 선택하세요 : ')
#     print(f'user: {user}, computer: {computer}')

#     # 평가에서 원하는것 같은 코드
#     # if computer=="가위":
#     #     if user=="가위":
#     #         print('무승부 입니다')
#     #         reports['draw']+=1
#     #     elif user=="바위":
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     #     else:
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1
#     # elif computer=='바위':
#     #     if user=="가위":
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1
#     #     elif user=="바위":
#     #         print('무승부 입니다')
#     #         reports['draw']+=1
#     #     else:
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     # else:
#     #     if user=="가위":
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     #     elif user=="바위":
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1
#     #     else:
#     #         print('무승부 입니다')
#     #         reports['draw']+=1

#     # 다중 if문
#     # if computer==user:
#     #     print('무승부 입니다')
#     #     reports['draw']+=1
#     # elif computer=="가위":
#     #     if user=="바위":
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     #     elif user=="보":
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1
#     # elif computer=='바위':
#     #     if user=="가위":
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1
#     #     elif user=="보":
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     # else:
#     #     if user=="가위":
#     #         print('사용자 승리!')
#     #         reports['win']+=1
#     #     elif user=="바위":
#     #         print('컴퓨터 승리!')
#     #         reports['lose']+=1

#     # 내맘대로
#     # rsplist[i]와 rsplist[i-1]을 비교하면
#     if computer == user:
#         print('무승부 입니다')
#         reports['draw'] += 1
#     elif rsplist[rsplist.index(user)-1] == computer:
#         print('사용자 승리!')
#         reports['win'] += 1
#     elif rsplist[rsplist.index(user)-2] == computer:
#         print('컴퓨터 승리!')
#         reports['lose'] += 1

#     regame = input('다시 하시겠습니까? (y/n) : ')
#     while regame not in check:
#         print('양식에 맞게 입력 해 주세요')
#         regame = input('다시 하시겠습니까? (y/n) : ')


# # 결과 출력
# print(reports)  # 딕셔너리로 깔끔하지 않아도 되면
# for reportStatus, reportNum in reports.items():  # 깔끔하게 결과값만 나와야 할 떄
#     finish += f'{reportStatus} {reportNum} '
# print(finish)
