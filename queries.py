from createConnect import *

# 查询选修了编译技术这门课的学生的学号 姓名 性别 成绩
query1 = 'select sno, sname, ssex, score ' \
         'from student natural join sc natural join course ' \
         'where cname=\'编译技术\''

# select sno, sname, ssex, score from student natural join sc natural join course where cname='编译技术'
# 查询选修人数排在前11的课程名称 课程号 选课人数 排名
query2 = 'select cname, cno, cnt, row_number() over (order by cnt desc) as `rank` ' \
         'from (select cname, cno, count(*) as cnt from sc natural join course group by cno) as tmp ' \
         'limit 11'

# select cname, cno, cnt, row_number() over (order by cnt desc) as `rank` from (select cname, cno, count(*) as cnt from sc natural join course group by cno) as tmp limit 11
def query(query_sql: str, db=''):
    # 1. 创建连接（Connection）
    conn = connectDatabase()
    if db:
        conn.select_db(db)
    victory = True
    query_res = []
    errInfo = ''
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            cursor.execute(query_sql)
            # 4.1 通过游标对象抓取数据(一个一个)
            # row = cursor.fetchone()
            # while row:
            #     query_res.append(row)
            #     row = cursor.fetchone()
            # 4.2 通过游标对象抓取数据(一次性)
            query_res = cursor.fetchall()
            victory = True
    except pymysql.MySQLError as err:
        # print(str(err))
        errInfo = 'ERROR' + str(err)
        victory = False
    finally:
        # 5. 关闭连接释放资源
        conn.close()
        if victory:
            return victory, query_res
        else:
            return victory, errInfo


if __name__ == '__main__':
    res1 = query(query1)
    [print(line) for line in res1]
    res2 = query(query2)
    [print(line) for line in res2]

