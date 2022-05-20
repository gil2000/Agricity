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
	ativo = json_Dict['ativo']
	lat = json_Dict['lat']
	lon = json_Dict['lon']
	Vegetacao = json_Dict['Vegetacao']
	Altitude = json_Dict['Altitude']
	observacoes = json_Dict['observacoes']

	#nao tentar escrever estas tabelas porque fazem parte da tabela idEstacao
	naoLer = ["ativo","lat","lon","Vegetacao","Altitude","observacoes","created_at","idEstacao"]

	cursor = conn.cursor()
	
	# inserir na tabelas tabelas respetivas
	def insertIntoBD(created_at, tabela, valor, idEstacao):
		
		#Verifica se a estacao
		if (tabela == "idEstacao"):

			tabela = "estacao"
			cursor.execute("SELECT idEstacao, COUNT(*) FROM estacao WHERE idEstacao = %s GROUP BY idEstacao", (valor,))

			# Esta linha é necessária para o rowcount funcionar
			results = cursor.fetchall()
			# Retorna o numero de vezes que o id dessa estacao especifica aparece na base de dados. 1 ou 0, hopefully. Assim sabemos se ja existe
			row_count = cursor.rowcount
			if row_count == 0:

				#Estacao nao existe na base de dados entao adiciona à tabela estacao para poder ser ligada às outras tabelas
				insert = """INSERT INTO """+ tabela +""" (idEstacao, lat, lon, Altitude, Vegetacao, ativo, observacoes) VALUES (%s,%s,%s,%s,%s,%s,%s) """
				vals = (idEstacao, lat, lon, Altitude, Vegetacao, ativo, observacoes)
				cursor.execute(insert, vals)	
				conn.commit()

		elif (tabela not in naoLer):
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




#===============================================================
# Seleção da BD para introdução dos Dados

def sensor_Data_Handler(Topic, jsonData):
	if Topic == data['mqtt']['topic']:
		Data_Handler(jsonData)
	

#===============================================================
