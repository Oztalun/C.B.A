import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.encoded_password = password.encode('utf-8')
        self.hash_password = hashlib.sha256(self.encoded_password).hexdigest()

    def display(self):
        print(f"화원 이름: {self.name}")
        print(f"회원 아이디: {self.username}")
        print(f"회원 비밀번호: {self.hash_password}")


members = []

# 회원 정보 등록
while True:
    print("회원 정보를 등록합니다.")
    name = input("이름 : ")
    username = input("아이디 : ")
    password = input("비밀번호 : ")
    members.append(Member(name, username, password))
    print(f"{name} 님 등록 완료\n")

    # 회원 등록 추가 여부
    while True:
        add_other = input("다른 정보를 추가하시겠습니까? (y/n): ").lower()
        if add_other == "y":
            break
        elif add_other == "n":
            print("\n회원 등록을 종료합니다.")
            break
        else:
            print("유효한 입력이 아닙니다.")
            continue

    # 입력값이 "n"일 경우 외부 while문까지 종료
    if add_other == "n":
        break

# while문이 모두 종료되면 회원 명단 출력
print("\n- 회원 명단 -")
for member in members:
    print(f"\n{member.name} 님")
