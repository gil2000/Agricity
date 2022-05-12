import mysql.connector
from mysql.connector import Error
import create_database_tables as createTablespy
import json

with open("ficheiros\config.json") as json_data_file:
    data = json.load(json_data_file)

try:

    cnx = mysql.connector.connect(user=data['mysql']['user'])
    cursor = cnx.cursor()
    createTablespy.database_test(data['mysql']['db'],cnx,cursor)
    

    conn = mysql.connector.connect(
          host=data['mysql']['host'],
          database=data['mysql']['db'],
          user=data['mysql']['user'],
          password=data['mysql']['passwd'],
          )

    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        curs = conn.cursor()
        curs.execute("select database();")
        record = curs.fetchone()
        print("You're connected to database: ", record)

        curs.execute("SHOW TABLES")
        all_tables_in_db = []
        for x in curs:
            all_tables_in_db.append(x)
        # se a tabela inserida no json existir então deixa passar
        if (all_tables_in_db.count((data['mysql']['tables'],)) >= 1 ):
            print("Table: "+ data['mysql']['tables'] +" exists")
        # se não existir vai ao novo script e cria a tabela
        else:
            createTablespy.main()


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