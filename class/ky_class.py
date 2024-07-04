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

members = []
member_cnt = int(input("몇 명의 정보를 입력하시겠습니까? : "))
for i in range(member_cnt):
    print(f"{i+1}번째 회원 정보를 입력해주세요.")
    name = input("이름 : ")
    username = input("아이디 : ")
    password = input("비밀번호 : ")
    members.append(Member(name, username, password))
    print("-------------------------------")

for i in members:
    i.display()