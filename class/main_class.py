import hashlib
import getpass


class Member:  # 6번, 8번줄은 id 생성여부 판단하기 위해서 작성, 나머지는 거의 똑같아서 마음대로 적음
    member_list = []

    def __init__(self, name, username, password):
        self.member_list.append(name)
        self.name = name
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"\n이름: {self.name}, ID: {self.username}")


class Post:  # 이건 다들 똑같음
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
    # 터미널에서 비밀번호 입력 시 비밀번호가 보이지 않도록 함. 비밀번호인데 보이면 안될거같아서 사용
    password = getpass.getpass("회원 비밀번호: ")

    # 회원 인스턴스 생성
    members.append(Member(name, username, password))

for member in members:
    member.display()
print("\n")

# post 입력받기
posts = []
while True:
    author = input("\n작성자 (종료하려면 'q' 입력): ")
    if author.lower() == "q":
        break
    elif author not in Member.member_list:
        print("등록된 회원이 아닙니다")
        continue
    content = input("게시물 내용: ")
    title = input("게시물 제목: ")

    # 게시물 인스턴스 생성
    post = Post(title, content, author)
    posts.append(post)

for post in posts:
    post.display()
print("\n\n")

specific_word = input("특정 단어 입력 : ")
print(f'다음은 게시물 내용에 {specific_word}가(이) 포함된 게시글 정보 입니다.\n')
for post in posts:
    if specific_word in post.content:
        print(f"\n'게시물 제목: {post.title}'\t '게시물 내용: {post.content}'\t'작성자: {post.author}'")
