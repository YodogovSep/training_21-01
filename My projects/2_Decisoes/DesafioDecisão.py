nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu genero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
           print("Olá Administradora")
        else:
            print("Olá Administrador")

    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("olá usuário")
elif nivel=="GUEST":
     print("Olá Visitante")
else:
     print("Olá Desconhecido(a)")