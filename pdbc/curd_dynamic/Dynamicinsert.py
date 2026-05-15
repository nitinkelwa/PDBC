import pymysql

def testinsert1():

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "insert into employee values  (17, 'tony', 'origin', 70000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data inserted with testinsert1 Successfully")


def testinsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "insert into employee values (%s, %s, %s, %s)"
    data=(18,'aditya','mahendra',80000)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data inserted with testinsert 2 Successfully")


def testinsert3(id, Name, company, Salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "insert into employee values(%s, %s, %s, %s)"
    data = (id, Name, company, Salary)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print('Data  inserted with testinsert3 successfully')


# def testinsert4(data={}):
#     id = data['id']
#     name = data['Name']
#     company = data['company']
#     Salary = data['Salary']
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
#     cursor = connection.cursor()
#     sql = "insert into employee values(%s, %s, %s, %s)"
#     data = (id, name, company, Salary)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('Data inserted with  testinsert4 successfully')




testinsert1()
testinsert2()
testinsert3(19,'Aman','Microsoft',800000)
# testinsert4({'id':20,
#              'Name':'ARUN',
#              'company':'Ncs',
#              'Salary':500000})
