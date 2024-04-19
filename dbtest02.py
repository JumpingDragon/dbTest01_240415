import pymysql  # mysql과 연동 시켜주는 라이브러리

# 파이썬과 mysql 서버 간의 커넥션 생성
# 1) 계정 : root(관리자 계정)
# 2) 비밀번호 : 12345
# 3) 데이터베이스가 설치된 컴퓨터의 IP 주소
#   - 본인 컴퓨터면 localhost, 다른 컴퓨터면 그 컴퓨터의 ip 주소
#   - 192.168.0.--- (컴퓨터 ip 주소)
# 4) 데이터베이스 스키마 이름 (ex: shopdb)

dbConn = pymysql.connect(host='localhost',user='root', password='12345', db='shopdb')
# 파이썬과 mysql 간의 connection 생성

sql = "INSERT INTO membertbl VALUES ('Dog','박개똥','서울시 종로구')"     # DB 에서 실행할 SQL 문 생성
# Primary Key 의 특징을 갖는 memberID 특징 때문에 이미 있으면 오류 뜬다.

cur = dbConn.cursor()
result = cur.execute(sql)  # 연결된 DB에 지정된 SQL 문이 실행됨
print(result)  # insert, update, delete 문이 실행된 후 성공결과를 반환 -> 1 이면 성공!

if result == 1:
    print("회원 가입이 성공하였습니다!")

# records = cur.fetchall()    # insert  into 는 돌려받을 게 없음

# dbConn의 사용이 종료된 후에는 반드시 닫아 줄 것! (close: cur 먼저 닫고 dbConn을 닫아야 한다)
cur.close()

dbConn.commit()  # insert, delete, update 문을 사용한 뒤에는 반드시 commit 함수를 호출해야 한다!
dbConn.close()
