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

	#Conexão à BD
	conn = mysql.connector.connect(
		host= data['mysql']['host'],
		database=data['mysql']['db'],
		user=data['mysql']['user'],
		password=data['mysql']['passwd']
		)

	#Parsing dos Dados 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	logTopic = "Temperature"
	
	#Inserção dos Dados na BD
	cursor = conn.cursor()
	if not isinstance(Temperature, float):
		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Temperature, logTopic)
		cursor.execute(dbinsertlog, vals)	
		conn.commit()
		cursor.close()

	elif Temperature < data['validacoes']['temp_min'] or Temperature > data['validacoes']['temp_max']:
		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Temperature, logTopic)
		cursor.execute(dbinsertlog, vals)	
		conn.commit()
		cursor.close()

	else:
		
		dbinsert = """INSERT INTO dht22_temperature_data (SensorID, Date_n_Time, Temperature) VALUES (%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Temperature)
		cursor.execute(dbinsert, vals)	
		conn.commit()

		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Temperature, logTopic)
		cursor.execute(dbinsertlog, vals)
		conn.commit()
		print ("Inserida Informação da Temperatura na Base de Dados.")
		print ("")
		cursor.close()

# Função para guardar a Humidade na BD
def DHT22_Humidity_Data_Handler(jsonData):

	#Conexão à BD
	conn = mysql.connector.connect(
		host= data['mysql']['host'],
		database=data['mysql']['db'],
		user=data['mysql']['user'],
		password=data['mysql']['passwd']
		)
	
	#Parsing dos Dados
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Humidity = json_Dict['Humidity']
	logTopic = "Humidity"
	cursor = conn.cursor()
	if not isinstance(Humidity, float):
		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Humidity, logTopic)
		cursor.execute(dbinsertlog, vals)	
		conn.commit()
		cursor.close()
	elif Humidity < data['validacoes']['hum_min'] or Humidity > data['validacoes']['hum_max']:
		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Humidity, logTopic)
		cursor.execute(dbinsertlog, vals)	
		conn.commit()
		cursor.close()
	else:
		#Inserção dos Dados na BD
	
		dbinsert = """INSERT INTO dht22_humidity_data (SensorID, Date_n_Time, Humidity) VALUES (%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Humidity)
		cursor.execute(dbinsert, vals)
		conn.commit()

		dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
		vals = (SensorID, Data_and_Time, Humidity, logTopic)
		cursor.execute(dbinsertlog, vals)
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
