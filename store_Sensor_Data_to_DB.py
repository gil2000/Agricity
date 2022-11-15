# Importar bibliotecas json MySQL
from datetime import datetime
import json
import mysql.connector

with open("ficheiros/config.json") as json_data_file:
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

	cursor = conn.cursor()

	##Parsing dos Dados 
	json_Dict = json.loads(jsonData)
	#Ler apenas os dados que são relevantes
	
	#Dados dependentes do TTN
	nomeEstacao = json_Dict['end_device_ids']['device_id']


	#Tira o T e o Z + casas decimais da timestamp
	created_at =  json_Dict['received_at']
	created_at = created_at.replace("T"," ")
	created_at = created_at.partition(".")[0]
	ativo = 1

	lat = json_Dict['uplink_message']['locations']['user']['latitude']
	lon = json_Dict['uplink_message']['locations']['user']['longitude']
	altitude = json_Dict['uplink_message']['locations']['user']['altitude']


	agricityData = json_Dict['uplink_message']['decoded_payload']

	logf = open("error.log", "a")
 
	#validação mt fast
	try:
		if int(agricityData['msgID']) == 2:
			if float(agricityData['barometricPressure']) > 10000 or float(agricityData['barometricPressure']) < 0:
				agricityData['barometricPressure'] = 0

			if float(agricityData['soilTemperature']) > 1000:
				agricityData['soilTemperature'] = 0
	except Exception as e:
		logf.write("Failed to use {0}: {1}\n".format(str(agricityData), str(e)))
		logf.write("\n")
		logf.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		logf.write("\n")
		logf.flush()
  
      
	try:
		#Procura se existem registos da estacao
		cursor.execute("SELECT nomeEstacao, COUNT(*) FROM estacao WHERE nomeEstacao = %s;", (nomeEstacao,))

		# Esta linha é necessária para o rowcount funcionar
		results = cursor.fetchall()
		# Retorna o numero de vezes que o id dessa estacao especifica aparece na base de dados. 1 ou 0, hopefully. Assim sabemos se ja existe
		row_count = results[0][1]

		#testa se existe um registo dessa estação na BD
		if row_count == 0:
				
			#Estacao nao existe na base de dados entao adiciona à tabela estacao para poder ser ligada às outras tabelas
			insert = """INSERT INTO estacao (nomeEstacao, lat, lon, altitude, ativo) VALUES (%s,%s,%s,%s,%s) """
			vals = (nomeEstacao, lat, lon, altitude, ativo)
			cursor.execute(insert, vals)	
			conn.commit()

		#Encontra o id da estação a inserir
		cursor.execute("SELECT id FROM estacao WHERE nomeEstacao = %s;", (nomeEstacao,))
		selectid = cursor.fetchall()
		idEstacao = selectid[0][0]

	except Exception as e:
		logf.write("Failed to query database for {0}: {1}\n".format(str(nomeEstacao), str(e)))
		logf.write("\n")
		logf.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		logf.write("\n")
		logf.flush()

	#Dados enviados pelo sensor da agricity
	
					
	#nao tentar escrever estas tabelas porque fazem parte da tabela nomeEstacao ou porque não são de interesse para a BD
	naoLer = ["msgID"]

	
	# inserir na tabelas tabelas respetivas
	def insertIntoBD(created_at, tabela, valor, idEstacao):
		try:
     
			insert = """INSERT INTO """+ tabela +""" (created_at, valor, idEstacao) VALUES (%s,%s,%s) """
			vals = (created_at, valor, idEstacao)
			cursor.execute(insert, vals)	
			conn.commit()
   
		except Exception as e:
			logf.write("Failed to insert to database {0} with valor {1}: {2}\n".format(str(tabela),valor, str(e)))
			logf.write("\n")
			logf.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			logf.write("\n")
			logf.flush()


	for entrada in agricityData:
		#valor = json_Dict[entrada]
		valor = agricityData[entrada]
		if (entrada not in naoLer):
			entrada = entrada.lower()
			insertIntoBD(created_at, entrada, valor, idEstacao)
   
	logf.close()
	conn.close()




#===============================================================
# Seleção da BD para introdução dos Dados

def sensor_Data_Handler(Topic, jsonData):
	Data_Handler(jsonData)
	

#===============================================================
