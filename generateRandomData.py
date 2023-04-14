import random
from createConnect import *

# 为Student表产生10,000条以上数据
# 为Course表产生1,000条以上记录
# 为SC表产生10,000*30条以上记录
# 学号按学年管理，每年2500左右的学生，年龄在15-35之间
# 姓名在百家姓中随机选择并结合学号构造，性别分男女，班级按学年分班每班不多于30人
# 课程号分学科，学时在8-192之间且为8的整数倍，学分依据学时换算即每16学时为1学分
# SC表的学号与课程号均应出现于Student表和Course表
# 每个学生学习课程按学年有16、32、48、64门按学年递增分布
# 学生姓名和课程名依学号、课程号构造加随机产生等。注意读者可依据具体情况自主设计各字段编码规律。

# sno:8 sname:10 ssex:2 sage:int sclass:6
student_insert_sql = 'insert into `student` values (%s, %s, %s, %s, %s)'
# cno:4 cname:30 credit:float chours:int tno:3
course_insert_sql = 'insert into `course` values (%s, %s, %s, %s, %s)'
# sno:8 cno:4 score:float
sc_insert_sql = 'insert into `sc` values (%s, %s, %s)'

# 四个年级
years = ['22L', '21L', '20L', '19L']
# 每个年级85个班
classes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54',
           '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
           '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85']
# 每个班30人
orderInClass = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

# 课程数量
courses_numbers = 1500
# 学生人数
students_numbers = 4 * 85 * 30

# 待插入学生数据
student_data = []
# 待插入课程数据
course_data = []
# 待插入学生选课数据
sc_data = []

# 我的sct是在seed=0生成的
random.seed(0)

# 随机设置course表的数据
with open('dataset/courses_zh.txt', 'r') as courseFile:
    coursesName = courseFile.readlines()  # 课程名列表
    coursesName = [course.rstrip() for course in coursesName]
    coursesName = random.sample(coursesName, courses_numbers)
    courseFile.close()
coursesNo = random.sample(range(1, 10000), courses_numbers)  # 不重复课程号列表
coursesNo = [str(cno).zfill(4) for cno in coursesNo]  # 填满四位
for cno_index, cno in enumerate(coursesNo):
    cname = coursesName[cno_index]
    chours = random.randint(1, 24) * 8
    credit = chours / 16
    # 此处设置一门课仅有一位老师 但是一位老师可以教授多门课
    tno = str(random.randint(1, 999)).zfill(3)
    course_data.append((cno, cname, credit, chours, tno))

# 随机取点中文姓名
with open('dataset/Chinese_Names.txt', 'r') as nameFile:
    studentName = nameFile.readlines()  # 中文姓名可选集
    studentName = random.sample(studentName, students_numbers * 3)
    studentName = [name.rstrip() for name in studentName]
    nameFile.close()
# 随机设置student表和sc表的数据
for year_index, year in enumerate(years):
    for class_index, class_ in enumerate(classes):
        for order in orderInClass:
            sno = year + class_ + order
            sname = random.choice(studentName)
            ssex = '男' if random.randint(0, 1) == 0 else '女'
            sage = random.randint(15, 35)
            sclass = year + class_
            student_data.append((sno, sname, ssex, sage, sclass))
            # 为当前student构造在sc中的课程
            courses = random.sample(coursesNo, (year_index + 1) * 16)
            for cno in courses:
                score = round(random.uniform(58.0, 100.0), 2)
                sc_data.append((sno, cno, score))

def getStudent():
    return student_data

def getCourse():
    return course_data

def getSc():
    return sc_data

def initDatabase():
    # 1. 创建连接（Connection）
    conn = connectDatabase()
    conn.select_db('sct')
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句(批处理)
            students_rows = cursor.executemany(student_insert_sql, student_data)
            if students_rows == len(student_data):
                print('生成学生数据成功!!!')
            courses_rows = cursor.executemany(course_insert_sql, course_data)
            if courses_rows == len(course_data):
                print('生成课程数据成功!!!')
            sc_rows = cursor.executemany(sc_insert_sql, sc_data)
            if sc_rows == len(sc_data):
                print('生成学生选课数据成功!!!')
        # 4. 提交事务（transaction）
        conn.commit()
    except pymysql.MySQLError as err:
        # 4. 回滚事务
        conn.rollback()
        print(type(err), err)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    initDatabase()
