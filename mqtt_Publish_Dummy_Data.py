# Importar a bibliteca paho, random, threading, json e datetime
import re
from time import sleep
import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

with open("ficheiros\config.json") as json_data_file:
    data = json.load(json_data_file)
#print(data)

#====================================================
# Definições MQTT 
MQTT_Broker = data['mqtt']['broker']
MQTT_Port = data['mqtt']['port']
Keep_Alive_Interval = data['mqtt']['alive_interval']
MQTT_Topic = data['mqtt']['topic']
#====================================================

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ("Falha na ligação ao broker MQTT...")
	else:
		print ("Ligado ao MQTT Broker: " + str(MQTT_Broker))

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

def createFakeFloatValue():
	valor =  float("{0:.2f}".format(random.uniform(0, 200)))
	return valor

def createFakeIntValue(minimum=0 ,maximum= 150):
	valor =  int("{0}".format(random.randint(minimum, maximum)))
	return valor

def createFakeStrValue():
	valor = float("{0:.2f}".format(random.uniform(0, 200)))
	if (valor > 100 and valor < 150):
		valor = "NNW"
	elif (valor > 150):
		valor = "N"
	elif (valor < 100 and valor > 50):
		valor = "S"
	else:
		valor = "SEE"
	return valor


def publish_Fake_Sensor_Values_to_MQTT():
	while(1):
		OutdoorTempreratureFake = createFakeFloatValue()
		OutdoorHumidityFake = createFakeFloatValue()
		Rain60MinutesFake = createFakeFloatValue()
		Rain24HoursFake = createFakeFloatValue()
		SunlightVisibleFake = createFakeIntValue()
		SunlightUVIndexFake = createFakeFloatValue()
		WindSpeedFake = createFakeFloatValue()
		BarometricPressureFake = createFakeFloatValue()
		bateryPowerFake = createFakeIntValue()
		SolarPowerFake = createFakeIntValue()
		SoilTemperatureFake = createFakeIntValue()
		SoilHumidityFake = createFakeIntValue()
		WindDirectionFake = createFakeStrValue()
		metalFake = createFakeIntValue()


		#Criar e definir valores globais aqui
		Valores = {}
		Valores['created_at'] = (datetime.today()).strftime("%Y-%m-%d %H:%M:%S")
		Valores['idEstacao'] = "Estacao_" + str(createFakeIntValue(1,20))

		#valores a separar para cada tabela individual

		Valores["OutdoorTemperature"] = OutdoorTempreratureFake
		Valores['OutdoorHumidity'] = OutdoorHumidityFake
		Valores['Rain60Minutes'] = Rain60MinutesFake
		Valores['Rain24Hours'] = Rain24HoursFake
		Valores['SunlightVisible'] = SunlightVisibleFake
		Valores['SunlightUVIndex'] = SunlightUVIndexFake
		Valores['WindSpeed'] = WindSpeedFake
		Valores['WindDirection'] = WindDirectionFake
		Valores['BarometricPressure'] = BarometricPressureFake
		Valores['batteryPower'] = bateryPowerFake
		Valores['SolarPower'] = SolarPowerFake
		Valores['SoilTemperature'] = SoilTemperatureFake
		Valores['SoilHumidity'] = SoilHumidityFake
		Valores['metal'] = metalFake
		Valores["lat"] = createFakeFloatValue()
		Valores["lon"] = createFakeFloatValue()
		Valores["Vegetacao"] = createFakeStrValue()
		Valores["observacoes"] = createFakeStrValue()
		Valores["Altitude"] = createFakeIntValue()
		toggle = 1
		if(toggle):
			Valores["ativo"] = toggle
			toggle = toggle - 1
		else:
			Valores["ativo"] = toggle
			toggle = toggle + 1



		json_valores = json.dumps(Valores)

		print ("Valores: " + json_valores)
		sleep(10)
		publish_To_Topic (MQTT_Topic, json_valores)


publish_Fake_Sensor_Values_to_MQTT()

#====================================================
