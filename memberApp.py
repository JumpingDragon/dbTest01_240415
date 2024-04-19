import sys
import pymysql

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/appui.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원 관리 프로그램")

        self.join_btn.clicked.connect(self.member_join)   # 회원가입 버튼 클릭 시 가입함수 호출
        self.joinreset_btn.clicked.connect(self.join_reset)   # 초기화
        self.idcheck_btn.clicked.connect(self.idcheck)      #


    def member_join(self):   # 회원 가입 이벤트 처리 함수
        memberid = self.joinid_edit.text() # 유저가 입력한 회원 아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()  # 유저가 입력한 회원 아이디 텍스트 가져오기
        membername = self.joinname_edit.text()  # 유저가 입력한 회원 아이디 텍스트 가져오기
        memberemail = self.joinemail_edit.text()  # 유저가 입력한 회원 아이디 텍스트 가져오기
        memberage = self.joinage_edit.text()  # 유저가 입력한 회원 아이디 텍스트 가져오기

        if memberid == "" or memberpw =="" or membername == "" or memberemail== "" or memberage =="":
            QMessageBox.warning(self, "입력 오류", "빈칸이 있습니다. 빈칸을 채워주세요.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 14자 이하이어야 합니다. 다시 입력바람.")
        elif len(memberpw) < 4 or len(memberpw) >= 15:
            QMessageBox.warning(self, "비밀번호길이오류", "비밀번호는 4자 이상 14자 이하이어야 합니다. 다시 입력바람.")
        else:
            dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

            sql = (f"INSERT INTO appmember VALUES('{memberid}','{memberpw}','{membername}',"
                   f"'{memberemail}','{memberage}')")

            cur = dbConn.cursor()
            result = cur.execute(sql)  # 회원가입하는 sql 문 성공 시 1 반환

            if result == 1:
                QMessageBox.warning(self, "회원가입성공", "축하합니다.\n 회원가입이 성공함.")
                self.join_reset()  # 회원가입 성공 ok 클릭 후 입력내용 초기화
            else:
                QMessageBox.warning(self, "회원가입실패", "회원가입 실패.")
            cur.close()
            dbConn.commit()
            dbConn.close()

    def join_reset(self):  # 회원가입정보 입력내용 초기화
        self.joinid_edit.clear()
        self.joinpw_edit.clear()
        self.joinname_edit.clear()
        self.joinemail_edit.clear()
        self.joinage_edit.clear()

    def idcheck(self):  # 기존 아이디 회원가입 여부 체크 함수
        memberid = self.joinid_edit.text()
        if memberid == "":
            QMessageBox.warning(self, "아이디입력오류", "아이디는 필수 입력사항입니다.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 14자 이하이어야 합니다. 다시 입력바람.")
        else:
            dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

            sql = f"SELECT count(*) FROM appmember WHERE memberid='{memberid}"
            # SQL문 실행 시 1 또는 0이 반환 (기존에 가입된 아이디면 1, 아니면 0)

            cur = dbConn.cursor()
            cur.execute(sql)  # 회원가입하는 sql 문 성공 시 1 반환

            result = cur.fetchall()

            if result[0][0] == 1:
                QMessageBox.warning(self, "회원가입불가", "존재하는 아이디입니다.")
            else:
                QMessageBox.warning(self, "회원가입가능", "가입 가능한 아이디입니다.")

            cur.close()
            dbConn.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
