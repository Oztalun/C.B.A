import hashlib

check = ['n', "N", "아니요", "아니", "y", "Y", "네"]


class Member:
    member_list = []

    def __init__(self, name, username, password):
        self.member_list.append(name)
        self.name = name
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def display(self):
        print(f"name : {self.name}")
        print(f"username : {self.username}\n")
        # print(f'password : {self.password}')
        pass


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"title : {self.title}")
        print(f"content : {self.content}")
        print(f'author : {self.author}\n')
        pass


members = []
posts = []

readd = "Y"
while readd not in check[0:4] and readd in check:
    members.append(Member(input("name : "), input(
        "username : "), input("password : ")))
    readd = input("\n더 추가 하시겠습니까?\n")
    print("")
    while readd not in check:
        readd = input("\n더 추가 하시겠습니까?\n")
        print("")

for i in members:
    i.display()

readd = "Y"
while readd not in check[0:4] and readd in check:
    name = input("who is author? : ")
    while name not in Member.member_list:
        print("해당 이름이 존재하지 않습니다.")
        name = input("who is author? : ")
    posts.append(Post(input("제목을 입력하세요 : "), input("내용을 입력하세요 : "), name))
    readd = input("\n더 추가 하시겠습니까?\n")
    print("")
    while readd not in check:
        readd = input("\n더 추가 하시겠습니까?\n")
        print("")

for i in posts:
    i.display()

word = input("특정 단어 입력 : ")
for i in posts:
    if word in i.content:
        i.display()

"""일일이 입력하기 귀찮아서 주석으로 달아둠(예시)
파이리
파이
vkdlfl
네
꼬부기
꼬북
Rhqnrl
네
버터플
버터플라이
butterfl
네
야도란
야도
diehfks
아니
"""
