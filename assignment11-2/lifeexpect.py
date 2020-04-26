import pymysql
import matplotlib.pyplot as plt

def getcountrybyname(name):
    worlddb = pymysql.connect("localhost", "root", "bkite123", "world")
    cursor = worlddb.cursor()
    sql = "select LifeExpectancy from country where name=%s"
    command = cursor.execute(sql,name)
    results = cursor.fetchone()
    worlddb.close()
    return results

def graphlifeexp():
    countries=('Algeria','Egypt','Gabon','Liberia','Morocco','Botswana','Madagascar','Namibia')
    lifex=[5,4,3,4,5,6,7,8]
    for i in range(len(countries)):
        lifex[i]=getcountrybyname(countries[i])
        lifex[i]=float(lifex[i][0])
    plt.xlabel('Country')
    plt.ylabel('Life Expectancy')
    plt.title('Life Expectancy by Country')
    plt.xticks(rotation=45)
    plt.bar(countries,lifex)
    plt.show()
graphlifeexp()
