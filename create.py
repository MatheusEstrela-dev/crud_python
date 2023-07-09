import mysql.connector
import datetime

from mysql.connector.dbapi import DATETIME

connection = mysql.connector.connect( 
    host="locahost",
    user="usuariobancodados",
    password="senhausuario",
    database="bancodados"
)

cursor = connection.cursor()

sql =  "INSERT INTO users (nome, email, created)  VALUES (%s, %s, %s)"
data = (
  "primeiro usuario",
  "primeirousuario@teste.com.br",
  DATETIME.datatime.today()
)

cursor.exexute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("foi cadastrado o novo usuario de ID:", userid)

# https://github.com/MatheusEstrela-dev/crud_python