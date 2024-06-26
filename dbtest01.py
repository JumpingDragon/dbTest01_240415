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

sql = "SELECT * FROM membertbl"     # DB 에서 실행할 SQL 문 생성

cur = dbConn.cursor()
cur.execute(sql)  # 연결된 DB의 스키마에 지정된 SQL 문이 실행됨

records = cur.fetchall()    # sql 문에서 실행된 select문의 결과를 records 라는 이름으로 받음

print(records)  # tuple 형식으로 나옴. tuple의 특징은 수정 불가.
print(records[0])  # 특정 레코드
print(records[0][1])  # 특정 레코드

for member in records:
    print(member)       # 레코드 단위로 출력
    print(member[1])    #

# dbConn의 사용이 종료된 후에는 반드시 닫아 줄 것! (close: cur 먼저 닫고 dbConn을 닫아야 한다)
cur.close()
dbConn.close()
