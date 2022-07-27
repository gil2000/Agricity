import json


with open("jsonteste.json") as ficheiro:
    dados = json.load(ficheiro)

for entrada in dados["uplink_message"]["decoded_payload"]:
    valor = dados["uplink_message"]["decoded_payload"][entrada]
    if type(valor) == float:
        valor = round(valor, 2)
    print(f'Para a entrada {entrada} temos os valor {valor}')
    # print(entrada)
    # print(valor)