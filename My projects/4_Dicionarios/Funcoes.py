def perguntar():
    return input("O que deseja realizar?\n" +
          "<I> - Inserir\n" +
          "<P> - Pesquisar\n" +
          "<E> - Excluir\n" +
          "<L> - Listar\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o login:").upper()]=[input("Informe o nome: ").upper(),
                                                    input("Informe o ultimo acesso: "),
                                                    input("Informe a última estação de acesso: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt","a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
