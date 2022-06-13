#####NOVO ARQUIVO#####
#1_arquivo = open("primeiro_arquivo.txt","w")
#r - read
#w - write
#a - append
#x - exclusive

#1_arquivo.write("Meu primeiro arquivo! Ai que absurdo!")

#1_arquivo.close()

#####Inserir dados no arquivo#####
#with open("primeiro_arquivo.txt","r") as arquivo:
#    arquivo.write("\nOs seus problemas.  Voce deve esquecer")

#####Ler Arquivo Inteiro#####
#with open("primeiro_arquivo.txt","r") as arquivo:
#   conteudo = arquivo.read()
#    print(conteudo)

#####Ler Arquivo - Linha#####
#with open("primeiro_arquivo.txt","r") as arquivo:
#    conteudo = arquivo.readline()
#    print(conteudo)

#####Ler Arquivo - Linha#####
with open("primeiro_arquivo.txt","r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
