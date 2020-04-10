import pymysql


def insertstud():

    db = pymysql.connect("localhost", "root", "bkite123", "tstudent")
    dbcursor = db.cursor()

    stuid = input("please  input a student id:")
    stuname = input("please  input the student's name:")
    major = input("please input the student's major:")
    stuyear = input("please  input the student's year:")
    tuition = input("please  input how much tuition is owed:")
    favcolor = input("please  input their favorite color:")

    sql = "insert into student(stuid,stuname,major,stuyear,tuition,favcolor) value(%s,%s,%s,%s,%s,%s)"
    values = (stuid,stuname,major,stuyear,tuition,favcolor)
    dbcursor.execute(sql, values)
    db.commit()
    dbcursor.close()
    db.close()

def delstud():

    db = pymysql.connect("localhost", "root", "bkite123", "tstudent")
    dbcursor = db.cursor()
    values = input("please input the id of the student you wish to delete:")

    sql = "delete from student where stuid=%s"

    dbcursor.execute(sql, values)
    db.commit()
    dbcursor.close()
    db.close()

def chgstudname():

    db = pymysql.connect("localhost", "root", "bkite123", "tstudent")
    dbcursor = db.cursor()
    stuid = input("please input the student id:")
    newname = input("please input the new name:")

    values = (newname,stuid)

    sql = "update student set stuname=%s where stuid=%s"

    dbcursor.execute(sql, values)
    db.commit()
    dbcursor.close()
    db.close()


def majcount():
    db = pymysql.connect("localhost", "root", "bkite123", "tstudent")
    dbcursor = db.cursor()
    sql = "select major, count(*) from student where major=%s "
    values = input("please input the major to be counted:")
    dbcursor.execute(sql,values)
    results = dbcursor.fetchall()
    print(results)

    dbcursor.close()
    db.close()
    results = ""



#insertstud()
#delstud()
#chgstudname()
#majcount()
