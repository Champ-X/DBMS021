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
    cols_name = ()
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
            cols_name = cursor.description
            victory = True
    except pymysql.MySQLError as err:
        errInfo = 'ERROR' + str(err)
        cols_name = ()
        victory = False
    finally:
        # 5. 关闭连接释放资源
        conn.close()
        if victory:
            return victory, cols_name, query_res
        else:
            return victory, cols_name, errInfo


if __name__ == '__main__':
    # _, cols1, res1 = query(query1, 'sct')
    # print(cols1)
    # print(res1)
    # _, cols2, res2 = query(query2, 'sct')
    # print(cols2)
    # print(res2)
    _, cols3, res3 = query('show tables', 'sct')
    print(cols3)
    print(res3)


