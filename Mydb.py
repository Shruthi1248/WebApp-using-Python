import mysql.connector
dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345'
)
cursorObject =dataBase.cursor()
cursorObject.execute("CREATE DATABASE websitedb")
print("All done")