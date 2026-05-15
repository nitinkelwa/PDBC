import pymysql



def testDelete1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "delete from employee where id = 17"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("data Delete with testdelete1 Successfully")


def testdelete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "delete from employee where id= %s"
    data=(18,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete with testdelete2 Successfully")

def testdelete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "delete from employee  where id= %s"
    data=(id,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete with testdelete3 Successfully")


testDelete1()
testdelete2()
testdelete3(19)