import pymysql


def getcountrydata():
    worlddb=pymysql.connect("localhost","root","bkite123","world")
    cursor=worlddb.cursor()
    sql="select * from country"
    command=cursor.execute(sql)
    results=cursor.fetchall()
    worlddb.close()

def getcountrybyname(name):
    worlddb = pymysql.connect("localhost", "root", "bkite123", "world")
    cursor = worlddb.cursor()
    sql = "select * from country where name=%s"
    command = cursor.execute(sql,name)
    results = cursor.fetchone()
    worlddb.close()

getcountrydata()

getcountrybyname("aruba")