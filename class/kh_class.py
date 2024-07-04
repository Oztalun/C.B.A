import hashlib
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.hash_password = hashlib.sha256(self.password.encode()).hexdigest()

    def display(self):
        print(f"회원 이름 : {self.name}")
        print(f"회원 아이디 : {self.username}")
        print(f"회원 비밀번호 : {self.hash_password}")

# members 리스트 생성
members = []

while True:
    print("회원 정보를 입력해주세요.")
    name = input("이름 : ")
    username = input("아이디 : ")
    password = input("비밀번호 : ")
    members.append(Member(name, username, password))
    print("-------------------------------")

    # 한번 정보 입력할 때마다 추가 입력 질문을 출력, 예외처리까지 설정
    while True:
        retry = input("추가로 정보를 입력하시겠습니까? (y/n) : ").lower()
        if retry == 'y' or retry == 'n':
            break
        else:
            print("(y/n)을 입력하세요.")

    if retry == 'n':
        break

# 회원 정보(이름) 출력
for i in members:
    # i.display()
    print(i.name)
