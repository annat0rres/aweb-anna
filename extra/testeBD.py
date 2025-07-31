from mysql.connector import (connection)

cnx = connection.MySQLConnection(
    user='root', password='labinfo',
    host='127.0.0.1',
    database='cliente'
    )

cursor = cnx.cursor()

sql = "INSERT INTO pessoa(nome, cidade, nascimento) VALUES (%s, %s, %s)"
dados = ('João Pedro', 'Extremoz', '2024-12-13')

cursor.execute(sql, dados)
cnx.commit()

cnx.close()