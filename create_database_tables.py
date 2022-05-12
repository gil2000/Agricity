from __future__ import print_function
import json
import mysql.connector
from mysql.connector import errorcode




def main():

    with open("ficheiros\config.json") as json_data_file:
        data = json.load(json_data_file)

    DB_NAME = data['mysql']['db']

    TABLES = {}
    TABLES[data['mysql']['tables']] = (
        " CREATE TABLE `" + data['mysql']['tables'] +"` ("
        " `id` INT(11) NOT NULL AUTO_INCREMENT,"
        " `UTCTime` TIMESTAMP NOT NULL,"
        " `IdEstacao` VARCHAR(20) NOT NULL COLLATE 'utf8_bin',"
        " `OutdoorTemperature` FLOAT NULL DEFAULT NULL,"
        " `OutdoorHumidity` FLOAT NULL DEFAULT NULL,"
        " `Rain60Minutes` FLOAT UNSIGNED NULL DEFAULT NULL,"
        " `Rain24Hours` FLOAT UNSIGNED NULL DEFAULT NULL,"
        " `SunlightVisible` INT(10) NULL DEFAULT NULL,"
        " `SunlightUVIndex` FLOAT NULL DEFAULT NULL,"
        " `WindSpeed` FLOAT NULL DEFAULT NULL,"
        " `WindDirection` VARCHAR(5) NULL DEFAULT NULL COLLATE 'utf8_bin',"
        " `BarometricPressure` FLOAT UNSIGNED NULL DEFAULT NULL,"
        " `batteryPower` INT(3) UNSIGNED NULL DEFAULT NULL,"
        " `solarPower` INT(10) UNSIGNED NULL DEFAULT NULL,"
        " `soilTemperature` INT(5) NULL DEFAULT NULL,"
        " `soilHumidity` INT(5) UNSIGNED NULL DEFAULT NULL,"
        " `metal` INT(10) UNSIGNED NULL DEFAULT NULL,"
        " `lat` FLOAT NULL DEFAULT NULL,"
        " `lon` FLOAT NULL DEFAULT NULL,"
        " `Altitude` INT(10) NULL DEFAULT NULL,"
        " `Vegetacao` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_bin',"
        "PRIMARY KEY (`id`) USING BTREE"
        ") ENGINE=InnoDB")

    
    cnx = mysql.connector.connect(user=data['mysql']['user'])
    cursor = cnx.cursor()

    database_test(DB_NAME,cnx,cursor)
    create_tables(TABLES,cursor)
    close_connections(cursor,cnx)


    

def create_database(DB_NAME,cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def database_test(DB_NAME,cnx,cursor):
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(DB_NAME,cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

def create_tables(TABLES,cursor):
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def close_connections(cursor,cnx):
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()