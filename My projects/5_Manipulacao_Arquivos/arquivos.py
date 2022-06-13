import json

## Leitura arquivo Jason
#with open("bd.json", "r") as arq_json:
#    dicionario = json.load(arq_json)
#    for chave, dados in dicionario.items():
#        print(chave + " | " + str(dados))

dicionario = {
    "endereco": ["Lins de Vasconcelos", "1222", "Sao Paulo", "SP"]
}

with open("../6_Wazayes/entrada.json", "w") as json_file:
    json.dump(dicionario,json_file)


##Leitura da base de dados considerando o separador interno
#basedados = []
#with open("iris.data", "r") as arquivo:
#    for registro in arquivo.readlines():
#        basedados.append(registro.split(","))


##Leitura total dos dados
#print(basedados)

##somando campos para apresentação de resultados após leitura dos dados
#print(float(basedados[0][0]) + float(basedados[0][1]))
