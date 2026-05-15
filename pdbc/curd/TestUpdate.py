# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
# cursor = connection.cursor()
# sql = "update user set name = 'abhi' where id =2"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("data Update Successfully")
#
# ##############################################################################################################

#
# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='indore')
# cursor = connection.cursor()
# sql = "update marksheet set name = 'pravin' where id =2"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("data Update Successfully")

################################################################################################################

import pymysql


connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='demo')
cursor=connection.cursor()
sql="update claim set status ='Approved' where claimid=10"
cursor.execute(sql)
connection.commit()
connection.close()
print("data updated in table claim ")