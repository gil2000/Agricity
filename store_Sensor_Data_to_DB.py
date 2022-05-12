# Importar bibliotecas json MySQL
import json
import mysql.connector

with open("ficheiros\config.json") as json_data_file:
    data = json.load(json_data_file)
#print(data)


#===============================================================
# Funções para passar os dados para a Base de Dados

# Função para guardar a Temperatura na BD
def Data_Handler(jsonData):

	#Ligação à BD
	conn = mysql.connector.connect(
		host= data['mysql']['host'],
		database=data['mysql']['db'],
		user=data['mysql']['user'],
		password=data['mysql']['passwd']
		)

	#Parsing dos Dados 
	json_Dict = json.loads(jsonData)

	idEstacao = json_Dict['idEstacao']
	created_at = json_Dict['created_at']

	cursor = conn.cursor()
	
	# inserir na tabela outdoor temp
	def insertIntoBD(created_at, tabela,valor, idEstacao):
		if (tabela != "created_at" and tabela != "idEstacao"):
			insert = """INSERT INTO """+ tabela +""" (created_at, valor, idEstacao) VALUES (%s,%s,%s) """
			vals = (created_at, valor, idEstacao)
			cursor.execute(insert, vals)	
			conn.commit()
		else:
			return

	for entrada in json_Dict:
		valor = json_Dict[entrada]
		insertIntoBD(created_at, entrada, valor, idEstacao)

	conn.close()

		
	#Validação se o valor pertence ao domínio Min a Max, caso falso é enviado para a tabela logs
	# elif Temperature < data['validacoes']['temp_min'] or Temperature > data['validacoes']['temp_max']:
	# 	dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
	# 	vals = (SensorID, Data_and_Time, Temperature, logTopic)
	# 	cursor.execute(dbinsertlog, vals)	
	# 	conn.commit()
	# 	cursor.close()

	#Inserção dos Dados na BD ao ter passado todos os testes de validação
	# else:
	# 	dbinsert = """INSERT INTO dht22_temperature_data (SensorID, Date_n_Time, Temperature) VALUES (%s,%s,%s) """
	# 	vals = (SensorID, Data_and_Time, Temperature)
	# 	cursor.execute(dbinsert, vals)	
	# 	conn.commit()

	# 	dbinsertlog = """INSERT INTO logs (SensorID, Date_n_Time, Value, Topic) VALUES (%s,%s,%s,%s) """
	# 	vals = (SensorID, Data_and_Time, Temperature, logTopic)
	# 	cursor.execute(dbinsertlog, vals)
	# 	conn.commit()
	# 	print ("Inserida Informação da Temperatura na Base de Dados.")
	# 	print ("")
	# 	cursor.close()



#===============================================================
# Seleção da BD para introdução dos Dados

def sensor_Data_Handler(Topic, jsonData):
	if Topic == data['mqtt']['topic']:
		Data_Handler(jsonData)
	

#===============================================================
