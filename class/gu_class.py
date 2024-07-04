import hashlib

# ----- 코드 정의 ------

# 회원 정보 정의
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원이름: {self.name}, 회원 아이디: {self.username}")
        # print(f"비번: {self.password}")


# 게시판 정보 정의
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def display(self):
        print(f"게시물 제목: {self.title}")
        print(f"게시물 내용: {self.content}")
        print(f"작성자: {self.author}")
        

# ----- 코드 실행 ------
members = []
posts = []

for i in range(3):
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    HashPass = hashlib.sha256(password.encode())
    hex_dig = HashPass.hexdigest()

    members.append(Member(name, username, hex_dig))

    for i in range(3):
        title = input("게시물 제목을 입력하세요: ")
        content = input("게시물 내용을 입력하세요: ")
        author = username

        posts.append(Post(title, content, username))


for member in members:
    member.display()

for post in posts:
    post.display()