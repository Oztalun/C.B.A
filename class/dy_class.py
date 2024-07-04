import hashlib
import getpass


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"\n이름: {self.name}, ID: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"\n게시물 제목: {self.title}")
        print(f"게시물 내용: {self.content}")
        print(f"작성자: {self.author}")


# member 입력받기
members = []
while True:
    name = input("\n회원 이름 (종료하려면 'q' 입력): ")
    if name.lower() == "q":
        break
    username = input("회원 아이디: ")
    password = getpass.getpass("회원 비밀번호: ")
    password_hash = []
    password_hash.append(hashlib.sha256(password.encode()).hexdigest())

    # 회원 인스턴스 생성
    member = Member(name, username, password)
    members.append(member)

for member in members:
    member.display()

# post 입력받기
posts = []
while True:
    title = input("\n게시물 제목 (종료하려면 'q' 입력): ")
    if title.lower() == "q":
        break
    content = input("게시물 내용: ")
    author = input("작성자: ")

    # 게시물 인스턴스 생성
    post = Post(title, content, author)
    posts.append(post)

for post in posts:
    post.display()

specific_word = "기록"
for post in posts:
    if specific_word in post.content:
        print(f"\n'{specific_word}'이 포함된 게시글 제목: {post.title}")
