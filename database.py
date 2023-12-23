import mysql.connector
#example
#commit()- method which ensures the changes made to the database 
# roolback()-used to revert the changes that are done to the database
#
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "gowtham#7278",
    database='employes'
    )

print(mydb)
cursor=mydb.cursor()
print(cursor)

#show database

# myconn=mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='gowtham#7278'
#     )
# mycur=myconn.cursor()

# try:
#    dbs=mycur.execute("show databases")
# except:
#    myconn.rollback()
# for x in mycur:  
#     print(x) 
# myconn.close()

#crate database

# myconn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='gowtham#7278',
#     )
# cur=myconn.cursor()

# try:
#     cur.execute("CREATE DATABASE GROCERYSTORE")
#     dbs=cur.execute("SHOW DATABASES")
# except:
#     myconn.rollback()
# for x in cur:
#     print(x)
# myconn.close()


# #creating table

# myconn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='gowtham#7278',
#     database='Grocerystore'
#     )
# cur=myconn.cursor()
# try:
#     dbs=cur.execute("create table products(productname varchar(20) not null, id int(20) not null primary key, MRP float not null)")
# except:
#     myconn.rollback()
# myconn.close()

#alter table

# myconn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='gowtham#7278',
#     database='Grocerystore'
#     )
# cur=myconn.cursor()
# try:
#    cur.execute("alter table products add product_count int(20) not null")
# except:
#     myconn.rollback()
# myconn.close()

#insert operation

# myconn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='gowtham#7278',
#     database='Grocerystore'
#     )
# cur=myconn.cursor()
# sql = "insert into products(productname, id, MRP,product_count) values (%s, %s, %s, %s)"

# value=("Rice",1,1500,10)
# try:
#    cur.execute(sql,value)
#    myconn.commit()  
# except:
#     myconn.rollback()
# print(cur.rowcount,"record inserted!")  
# myconn.close()

#Insert multiple rows

# myconn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='gowtham#7278',
#     database='Grocerystore'
#     )
# cur=myconn.cursor()
# sql = "insert into products(productname, id, MRP,product_count) values (%s, %s, %s, %s)"

# value=[("soap",2,15,10),("Toothpaste",3,25,20),("Biscuit",4,10,40)]
# try:
#    cur.executemany(sql,value)
#    myconn.commit()  
# except:
#     myconn.rollback()
# print(cur.rowcount,"record inserted!")  
# myconn.close()

# read operation

# myconn=mysql.connector.connect(host='localhost',user='root',password='gowtham#7278',database='Grocerystore')
# cur=myconn.cursor()
# try:
#     cur.execute('select * from products')
#     result=cur.fetchall()

#     for x in result:
#         print(x);

# except:
#     myconn.rollback()
# myconn.close()

