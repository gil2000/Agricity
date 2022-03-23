import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
          host='localhost',
          database='agricity',
          user='root',
          password=''
          )
    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        curs = conn.cursor()
        curs.execute("select database();")
        record = curs.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if conn.is_connected():
        curs.close()
        conn.close()
        print("MySQL connection is closed")


# Nome da Base de Dados
#DB_Name =  "agr"


# Conexão à Base de Dados
#conn = sqlite3.connect(DB_Name)
#curs = conn.cursor()

# Criar Tabelas
#sqlite3.complete_statement(TableSchema)
#curs.executescript(TableSchema)

# Fechar Base de Dados
#curs.close()
#conn.close()