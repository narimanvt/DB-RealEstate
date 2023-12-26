import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    username = "root",
    password = "Mina@modir2003"
    )

mycusor = mydb.cursor()

print(mydb)
#mycursor.execute("CREATE TABLE CITY")

