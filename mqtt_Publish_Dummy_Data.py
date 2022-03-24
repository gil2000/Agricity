# Importar a bibliteca paho, random, threading, json e datetime
import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data)

#====================================================
# Definições MQTT 
MQTT_Broker = data['mqtt']['broker']
MQTT_Port = data['mqtt']['port']
Keep_Alive_Interval = data['mqtt']['alive_interval']
MQTT_Topic_Humidity = data['mqtt']['topic_humidade']
MQTT_Topic_Temperature = data['mqtt']['topic_temperatura']
#====================================================

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ("Falha a conexão ao broker MQTT...")
	else:
		print ("Conectado ao MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Publicado: " + str(message) + " " + "no MQTT Topic: " + str(topic))
	print ("")


#====================================================
# Sensor Fake 
# Codigo usado para criar valores Fake 

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(3, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(-40, 200)))

		Humidity_Data = {}
		Humidity_Data['Sensor_ID'] = "Sensor02"
		Humidity_Data['Date'] = (datetime.today()).strftime("%Y-%m-%d %H:%M:%S")
		Humidity_Data['Humidity'] = Humidity_Fake_Value
		humidity_json_data = json.dumps(Humidity_Data)

		print ("Valor fake de humidade: " + str(Humidity_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_Humidity, humidity_json_data)
		toggle = toggle + 1

	else:
		Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(0, 50)))

		Temperature_Data = {}
		Temperature_Data['Sensor_ID'] = "Sensor01"
		Temperature_Data['Date'] = (datetime.today()).strftime("%Y-%m-%d %H:%M:%S")
		Temperature_Data['Temperature'] = Temperature_Fake_Value
		temperature_json_data = json.dumps(Temperature_Data)

		print ("Valor fake de temperatura: " + str(Temperature_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_Temperature, temperature_json_data)
		toggle = 0


publish_Fake_Sensor_Values_to_MQTT()

#====================================================
