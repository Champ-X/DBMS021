from createConnect import *

def create():
    conn = connectDatabase()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'create table Student (Sno char(8) Primary key, Sname char(10), Ssex char(2), Sage integer, SClass char(6))'
        )
        cursor.execute(
            'create table Course (Cno char(4) Primary key, Cname char(30), Credit float(1) , Chours integer, Tno char(3))'
        )
        cursor.execute(
            'create table SC (Sno char(8), Cno char(4), Score float(1), foreign key (Sno) references Student(Sno), foreign key (Cno) references Course(Cno))'
        )
    finally:
        conn.close()


if __name__ == '__main__':
    create()
    