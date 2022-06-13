#Forma não muito convencional de desenvolver ferramenta de gestão de dados!
usuarios = {}
opcao = input("O que deseja realizar?\n" +
            "<I> - Inserir\n" +
            "<P> - Pesquisar\n" +
            "<E> - Excluir\n" +
            "<L> - Listar\n").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Informe o Login: ").upper()
        nome=input("Informe o Nome: ").upper()
        data=input("Informe o acesso mais recente: ")
        estação=input("Informe a Estação: ").upper()
        usuarios [chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?\n")
            "<I> - Inserir\n" +
            "<P> - Pesquisar\n" +
            "<E> - Excluir\n" +
            "<L> - Listar\n").upper()