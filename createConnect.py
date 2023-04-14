import pymysql
# 创建连接（Connection）
def connectDatabase():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        charset='utf8mb4',
        autocommit=True
    )
