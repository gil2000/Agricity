import json


with open("jsonteste.json") as ficheiro:
    dados = json.load(ficheiro)

#Dados dependentes do TTN
idEstacao = dados['end_device_ids']['device_id']
created_at = dados['received_at']
ativo = 1

lat = dados['uplink_message']['locations']['user']['latitude']
lon = dados['uplink_message']['locations']['user']['longitude']
altitude = dados['uplink_message']['locations']['user']['altitude']
agricityData = dados["uplink_message"]["decoded_payload"]

print(f"Valor {idEstacao} ")
print(f"Valor {created_at} ")
print(f"Valor {lat} ")
print(f"Valor {lon} ")
print(f"Valor {altitude} ")
print(f"Valor {agricityData} ")
    # valor = dados["uplink_message"]["decoded_payload"][entrada]
    # if type(valor) == float:
    #     valor = round(valor, 2)
    # print(f'Para a entrada {entrada} temos os valor {valor}')
    # # print(entrada)
    # # print(valor)