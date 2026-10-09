import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DRAGON",
    database="aqua_alert"
)

if mydb.is_connected():
    print("MySQL connection successful!")