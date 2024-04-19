import pymysql

dbConn = pymysql.connect(user="root", password="12345", host="localhost", db = 'shopdb')

while True:
    print("************* 회원관리 프로그램 *************")
    print("1 : 회원 가입")
    print("2 : 회원 정보 수정")
    print("3 : 회원 탈퇴")
    print("4 : 전체 회원목록 조회")
    print("5 : 프로그램 종료")
    print("******************************************")

    menuNum = input("메뉴 중 한 가지를 선택하세요(1~4)")

    if menuNum == "1":
        print("회원정보 입력:")
        ID = input("1) 회원 아이디 입력: ")
        Name = input("2) 회원 이름 입력: ")
        Address = input("3) 회원 주소 입력: ")

        sql = f"INSERT INTO membertbl VALUES('{ID}','{Name}','{mAddress}')"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("축하. 회원가입 성공.")
        else:
            print("회원가입 실패")
        cur.close()
        dbConn.commit()

    elif menuNum == "2":
        ID = input("정보 수정할 회원 아이디 입력:")
        Name = input("수정할 회원 이름 입력:")
        Address = input("수정할 회원 주소 입력:")

        sql = f"UPDATE membertbl SET memberName='{Name}', memberAddress='{Address}' WHERE memberID = '{ID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("축하. 수정 성공.")
        else:
            print("수정 실패.")

    elif menuNum == "3":
        ID = input("탈퇴할 회원 아이디 입력:")

        sql = f"DELETE * FROM membertbl WHERE memberID = '{ID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("탈퇴 성공.")
        else:
            print("탈퇴 실패.")

    elif menuNum == "4":
        ID = input("탈퇴할 회원 아이디 입력:")

        sql = f"SELECT * FROM membertbl"
        cur = dbConn.cursor()
        result = cur.execute(sql)


    elif menuNum == "5":
        print("프로그램을 종료합니다. 안녕히가세요.")
        dbConn.close()
        break
    else:
        print("잘못입력. 다시 입력 바람.")

