# Importar bibliotecas json MySQL
import json
import mysql.connector

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data)


#===============================================================
# Funções para passar os dados para a Base de Dados

# Função para guardar a Temperatura na BD
def DHT22_Temp_Data_Handler(jsonData):
	#Parsing dos Dados 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	
	#Introdução na BD
	conn = mysql.connector.connect(
		host= data['mysql']['host'],
		database=data['mysql']['db'],
		user=data['mysql']['user'],
		password=data['mysql']['passwd']
		)

	cursor = conn.cursor()
	dbinsert = """INSERT INTO dht22_temperature_data (SensorID, Date_n_Time, Temperature) VALUES (%s,%s,%s) """
	vals = (SensorID, Data_and_Time, Temperature)
	
	cursor.execute(dbinsert, vals)	
	conn.commit()
	print ("Inserida Informação da Temperatura na Base de Dados.")
	print ("")

	cursor.close()

# Função para guardar a Humidade na BD
def DHT22_Humidity_Data_Handler(jsonData):
	#Parsing dos Dados
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Humidity = json_Dict['Humidity']
	
	#Introdução na BD
	conn = mysql.connector.connect(
		host= data['mysql']['host'],
		database=data['mysql']['db'],
		user=data['mysql']['user'],
		password=data['mysql']['passwd']
		)
	
	
	cursor = conn.cursor()
	dbinsert = """INSERT INTO dht22_humidity_data (SensorID, Date_n_Time, Humidity) VALUES (%s,%s,%s) """
	vals = (SensorID, Data_and_Time, Humidity)
	
	cursor.execute(dbinsert, vals)	
	conn.commit()
    
	print ("Inserida Informação da Humidade na Base de Dados.")
	print ("")
	cursor.close()

#===============================================================
# Seleção da BD para introdução dos Dados

def sensor_Data_Handler(Topic, jsonData):
	if Topic == data['mqtt']['topic_temperatura']:
		DHT22_Temp_Data_Handler(jsonData)
	elif Topic == data['mqtt']['topic_humidade']:
		DHT22_Humidity_Data_Handler(jsonData)	

#===============================================================
