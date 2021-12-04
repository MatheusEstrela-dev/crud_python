import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="usuariobancodados",
  password ="senhausuario",
  database="bancodados",
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute (sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)