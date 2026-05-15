import pymysql


def testread1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "select * from employee"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    connection.commit()
    connection.close()
 

print("Data read successfully")

testread1()


def testread2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "select * from employee"
    cursor.execute(sql)
    data = cursor.fetchall()
    columnName = ('id', 'name', 'company', 'Salary')
    for x in data:
        print(x)
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


print("data read 2 successfully ")

testread2()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()

    sql = "select * from employee"
     # sql = "select * from employee where id = 1"
     # sql = "select * from employee where LastName = 'Kumar'"
     # sql = "select * from employee where name like 'a%'"
     # sql = "select * from employee where Salary = 50000"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
    connection.commit()
    connection.close()

print("Data read 3 successfully")

testRead3()

