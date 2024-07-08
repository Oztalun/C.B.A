<<<<<<< HEAD
=======
# 예시
# class ClassName:
#     # 클래스 변수 (모든 인스턴스가 공유하는 변수)
#     class_variable = 0
    
#     # 초기화 메서드 (인스턴스 생성 시 호출되는 메서드)
#     def __init__(self, arg1, arg2):
#         self.instance_variable1 = arg1
#         self.instance_variable2 = arg2
        
#     # 인스턴스 메서드 (인스턴스에 의해 호출되는 메서드)
#     def instance_method(self):
#         # 메서드 내용
#         return self.instance_variable1 + self.instance_variable2
    
#     # 클래스 메서드 (클래스에 의해 호출되는 메서드)
#     @classmethod
#     def class_method(cls, arg):
#         # 클래스 변수에 접근할 때는 cls.class_variable 사용
#         cls.class_variable += arg
    
#     # 정적 메서드 (클래스나 인스턴스와 무관하게 호출되는 메서드)
#     @staticmethod
#     def static_method():
#         # 정적 메서드 내용
#         return "This is a static method"
# # 클래스 인스턴스 생성
# obj = ClassName(10, 20)
# # 인스턴스 변수 읽기
# print(obj.class_variable)
# print(obj.instance_variable1)  # 출력: 10
# print(obj.instance_variable2)  # 출력: 20

# # 인스턴스 변수 수정
# obj.instance_variable1 = 30
# print(obj.instance_variable1)  # 출력: 30

# # 인스턴스 메서드 호출
# result = obj.instance_method()
# print(result)  # 출력: 50 (10 + 30)

# # 클래스 메서드 호출
# ClassName.class_method(5)
# print(ClassName.class_variable)  # 출력: 5

# # 정적 메서드 호출
# message = ClassName.static_method()
# print(message)  # 출력: "This is a static method"
#----------------------------------------------------------------------------------


# ----- 코드 정의 ------
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc
import hashlib

check = ['n', "N", "아니요", "아니", "y", "Y", "네"]

class Member:
    member_list = []
    def __init__(self, name, username, password):
        self.member_list.append(name)
        self.name = name
        self.username = username
<<<<<<< HEAD
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def display(self):
        print(f"name : {self.name}")
        print(f"username : {self.username}\n")
        # print(f'password : {self.password}')
=======
        self.encodedpw = password.encode('utf-8')
        self.password = hashlib.sha256(self.encodedpw).hexdigest()

    def display(self):
        print(f"name : {self.name}")
        print(f"username : {self.username}")
        print(f'password : {self.password}')
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc
        pass


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def display(self):
        print(f"title : {self.title}")
        print(f"content : {self.content}")
<<<<<<< HEAD
        print(f'author : {self.author}\n')
=======
        print(f'author : {self.author}')
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc
        pass

members = []
posts = []

readd = "Y"
while readd not in check[0:4] and readd in check:
    members.append(Member(input("name : "), input("username : "), input("password : ")))
<<<<<<< HEAD
    readd = input("\n더 추가 하시겠습니까?\n")
    print("")
    while readd not in check:
        readd = input("\n더 추가 하시겠습니까?\n")
        print("")
=======
    readd = input("더 추가 하시겠습니까?")
    while readd not in check:
        readd = input("더 추가 하시겠습니까?")
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc

for i in members:
    i.display()

readd = "Y"
while readd not in check[0:4] and readd in check:
    name = input("who is author? : ")
    while name not in Member.member_list:
        print("해당 이름이 존재하지 않습니다.")
        name = input("who is author? : ")
    posts.append(Post(input("제목을 입력하세요 : "), input("내용을 입력하세요 : "), name))
<<<<<<< HEAD
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
=======
    readd = input("더 추가 하시겠습니까?")
    while readd not in check:
        readd = input("더 추가 하시겠습니까?")
    
for i in posts:
    i.display()
"""
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc
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
<<<<<<< HEAD

=======
 
>>>>>>> a5a0919b63b8453a8c7ca252edc4a24c166359bc
"""