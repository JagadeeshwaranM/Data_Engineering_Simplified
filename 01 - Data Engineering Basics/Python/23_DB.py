import mysql.connector as mysql
db = mysql.connect(host = "localhost",user = "jaga",passwd="Home@123",database="sql_practise")
query = "SELECT * FROM Orders"
cursor.execute(query)