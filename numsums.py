import pymysql
import csv
import pandas as pd


def sqlit(): #reads csv and inputs data to datenumber.sql
    filename = "assign11-1-ch02-data.csv"

    with open(filename) as f:
        reader = csv.reader(f)
        data=reader
        db = pymysql.connect("localhost", "root", "bkite123", "datenumber")
        dbcursor = db.cursor()

        sql = "insert into numbydate(dates,num) value(%s,%s)"
        for row in data:
            if data.line_num>1:
                values = (row[0],row[1])
                dbcursor.execute(sql,values)

        db.commit()
        db.close()

def sumbydate(): #sums the numbers by date then outputs them to excel file
    db = pymysql.connect("localhost", "root", "bkite123", "datenumber")
    dbcursor = db.cursor()

    sql = "select dates,sum(num) as counts from numbydate group by dates"

    dbcursor.execute(sql)
    results = dbcursor.fetchall()
    dates = ()
    nums = ()
    for row in results:
        dates = dates + (row[0],)
        nums = nums + (int(row[1]),)

    dit = {'date': dates, 'num': nums}

    file_path = 'outputh.xlsx'
    writer = pd.ExcelWriter(file_path)

    df = pd.DataFrame(dit)
    df.to_excel(writer, columns=['date', 'num'], index=False, encoding='utf-8', sheet_name='Sums')
    writer.save()
    dbcursor.close()
    db.close()
    results = ""


