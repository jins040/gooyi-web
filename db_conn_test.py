import pymysql
import sys

print(sys.stdin.encoding)

# Maria DB Connection 연결
conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='0409',
                                 db='test', charset ='utf8')

# Connection으로부터 Cursor 생성
cur = conn.cursor()

# SQL문 실행
cur.execute("SELECT * FROM test_conn")

# 데이터 Fetch
rows = cur.fetchall()
print(rows)

# Connection 닫기
conn.close()