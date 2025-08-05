#arquivo para funções utéis

from dotenv import load_dotenv

load_dotenv()

#env é uma variavel q funciona por toda aplicação flask
#precisamos do os, pq estamos usando funções do sistema op


from mysql.connector import (connection)


def conectarBD():
    cnx = connection.MySQLConnection(
        user='root', #vamos substituir o root para USERDB --> CONFIGURAMOS NO ENV, usamos o comando os.getenv
        password='labinfo', #substit. labinfo por  PASSDB
        host='127.0.0.1',
        database='cliente' #substit. cliente por NAMEDB
        #fica da seguinte forma: password= os.getenv('PASSDB')
    )
     

    return cnx