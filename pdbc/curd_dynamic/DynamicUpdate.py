import pymysql


def testUpdate():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "update employee set name ='rohan' where id =5"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "update employee set name = %s where id = %s"
    data = ('Ravi', 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')


def testUpdate3(name, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "update employee set name = %s where id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated3 successfully')


def testupdate4(data):
    id = data['id']
    Name = data['Name']
    company = data['company']
    Salary = data['Salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='nitin')
    cursor = connection.cursor()
    sql = "update employee set name= %s, company= %s ,Salary= %s where id = %s"
    data = (id, Name, company, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


testUpdate()
testUpdate2()
testUpdate3('arush', 1)

params = {}
params['id'] = 4
params['Name'] = 'abc'
params['company'] = 'rays'
params['Salary'] = 100000

testupdate4(params)
