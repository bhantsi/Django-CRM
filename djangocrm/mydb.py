import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@$$word32",

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE djangocrm")

print("Please wait while we create the database...")
print("..........................")
print("Database created successfully!")
