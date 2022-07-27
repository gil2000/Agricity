# Importar a biblioteca paho e chamar a funçao sensor_Data_handler do ficheiro store
import json
import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler

with open("ficheiros\config.json") as json_data_file:
    data = json.load(json_data_file)
#print(data)

# Definições MQTT 
MQTT_Broker = data['mqtt']['broker']
MQTT_Port = data['mqtt']['port']
Keep_Alive_Interval = data['mqtt']['alive_interval']
MQTT_Topic = data['mqtt']['topic']
MQTT_User = data['mqtt']['user']
MQTT_Passwd = data['mqtt']['passwd']


# Conectar e Subscrever ao Tópico 
def on_connect(mosq, obj, flag, rc):
    #importante manter o QoS como 0
	mqttc.subscribe(MQTT_Topic, 0)


# Guardar a mensagem na base de dados recorrendo ao ficheiro store
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# Função "sensor_Data_Handler" está no script "sensor_data_to_db.py"
	print ("Dados MQTT recebidos...")
	print ("MQTT Tópico: " + msg.topic)  
	print ("Dados: " + str(msg.payload))
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Atribuir ações a chamadas
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

#Definição de utilizador e password
mqttc.username_pw_set(MQTT_User, password=MQTT_Passwd)

# Conexão
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Repetir Processo
mqttc.loop_forever()
