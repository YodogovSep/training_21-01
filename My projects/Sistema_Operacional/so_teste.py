#import platform
import getpass
#from datetime import datetime

# print("Nome maquina:........", platform.node())
# print("Arquitetura:.........", platform.architecture())
# print("Sistema Operacional:.", platform.system())
# print("Versao do SO:........", platform.release())
# print("Processador:.........", platform.processor())
# print("Versao do python:....", platform.python_version())

#print(datetime.now().month)

###Solicitacao de senha
# print(getpass.getuser())
# print(getpass.getpass("Digite sua Senha:..."))

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == 'usertricaster' and senha == 'Hello':
    print('Bem vinda Adele')
else:
    print('Voc~e não tem acesso!')