# C:/Users/rlagk/PycharmProjects/Contact/contact.py

# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, name, phone_number, e_mail, addr): # __init__쓰는 이유가 뭐였더라??
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact(): # 왜 클래스 밖에서 def를 할까??
    name = input("Name: ") # input은 값을 넣도록 지정 하는 함수
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info() # 문제는 입력해 놓았던 모든 리스트를 반환한다는 문제가 있다.

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 연락처 저장
def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def run():
    contact_list = [] # contact_list라는 빈 리스트를 생성한다.
    while 1: # 무한 루프를 생성한다. # while 1은 무한 루프함수이다.
        menu = print_menu() # menu 인스턴스를 생성한다.
        if menu == 1: # 1이 아니면 설정되지 않은 경우이기 때문에 무한 재실행.
            contact = set_contact() # set_contact()를 부르는 contact 인스턴스를 부른다.
            contact_list.append(contact) # 위의 contact_list에 추가한다.
        elif menu == 2:
            print_contact(contact_list) # 현재까지 contact_list에 저장한 contact들의 목록을 전부 불러온다.
        elif menu == 3:
            name = input("Name: ") # 지울 연락처의 이름을 지정하고 삭제한다.
            delete_contact(contact_list, name)
        elif menu == 4: # 4가 되면 멈춰라
            store_contact(contact_list) # contact_list를 contact_db.txt에 저장한다.
            break # 강제로 print_menu 함수 내부에 int를 설정하는 함수를 만들어서 break 조건을 걸어준다.

if __name__ == "__main__":
    run()

# 위의 모듈을 실행하는 방법은 아래와 같다.
# 1.인터프리터에서 직접 실행
# 직접실행 = __main__
# 2. 다른 모듈에 임포트해서 실행

# __name__: 인터프리터가 실행 전에 만들어 둔 글로벌 변수
# __main__: 인터프리터에서 직접 실행하는 것.

