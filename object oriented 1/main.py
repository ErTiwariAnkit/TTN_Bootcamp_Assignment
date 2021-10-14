import mysql.connector
connec=mysql.connector.connect(user='root',password='password',host='localhost',database='db')
print(connec.is_connected())
