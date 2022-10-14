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

	cursor = conn.cursor()

	##Parsing dos Dados 
	json_Dict = json.loads(jsonData)
	#Ler apenas os dados que são relevantes
	
	#Dados dependentes do TTN
	idEstacao = json_Dict['end_device_ids']['device_id']

	#Tira o T e o Z + casas decimais da timestamp
	created_at =  json_Dict['received_at']
	created_at = created_at.replace("T"," ")
	created_at = created_at.partition(".")[0]
	ativo = 1

	lat = json_Dict['uplink_message']['locations']['user']['latitude']
	lon = json_Dict['uplink_message']['locations']['user']['longitude']
	altitude = json_Dict['uplink_message']['locations']['user']['altitude']


	agricityData = json_Dict['uplink_message']['decoded_payload']

	#Procura se existem registos da estacao
	cursor.execute("SELECT idEstacao, COUNT(*) FROM estacao WHERE idEstacao = %s GROUP BY idEstacao", (idEstacao,))

	# Esta linha é necessária para o rowcount funcionar
	results = cursor.fetchall()
	# Retorna o numero de vezes que o id dessa estacao especifica aparece na base de dados. 1 ou 0, hopefully. Assim sabemos se ja existe
	row_count = cursor.rowcount

	#testa se existe um registo dessa estação na BD
	if row_count == 0:
    		
		#Estacao nao existe na base de dados entao adiciona à tabela estacao para poder ser ligada às outras tabelas
		insert = """INSERT INTO estacao (idEstacao, lat, lon, altitude, ativo) VALUES (%s,%s,%s,%s,%s) """
		vals = (idEstacao, lat, lon, altitude, ativo)
		cursor.execute(insert, vals)	
		conn.commit()

	#Dados enviados pelo sensor da agricity
	
					
	#nao tentar escrever estas tabelas porque fazem parte da tabela idEstacao ou porque não são de interesse para a BD
	naoLer = ["msgID"]

	
	# inserir na tabelas tabelas respetivas
	def insertIntoBD(created_at, tabela, valor, idEstacao):
		if (tabela not in naoLer):
			insert = """INSERT INTO """+ tabela +""" (created_at, valor, idEstacao) VALUES (%s,%s,%s) """
			vals = (created_at, valor, idEstacao)
			cursor.execute(insert, vals)	
			conn.commit()
		else:
			return

	for entrada in agricityData:
		#valor = json_Dict[entrada]
		valor = agricityData[entrada]
		insertIntoBD(created_at, entrada, valor, idEstacao)

	conn.close()




#===============================================================
# Seleção da BD para introdução dos Dados

def sensor_Data_Handler(Topic, jsonData):
	Data_Handler(jsonData)
	

#===============================================================
