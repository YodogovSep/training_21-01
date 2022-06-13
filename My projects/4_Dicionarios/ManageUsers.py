from Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
     if opcao=="I":
        inserir(usuarios)
        opcao = perguntar()
 #   if opcao=="I":
 #       chave=input("Informe o Login: ").upper()
 #       nome=input("Informe o Nome: ").upper()
 #       data=input("Informe o acesso mais recente: ")
 #       estacao=input("Informe a Estação: ").upper()
 #       usuarios [chave]=[nome, data, estacao]
 #   opcao = perguntar()