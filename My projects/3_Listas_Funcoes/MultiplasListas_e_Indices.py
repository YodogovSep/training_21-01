equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("\nNome.........: ", equipamentos[indice])
    print("\nValor........: ", valores[indice])
    print("\nSerial.......: ", seriais[indice])
    print("\nDepartamento.: ", departamentos[indice])