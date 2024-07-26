###Criar uma lista de dados e, usando a biblioteca OS, 
# interagir com o seu sistema operacional. 
# Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.

import os

myData = ["Yuri", "Matheus", "Marcus"]

diretorio = "Desafio_OS"

if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    print(f'Diretório "{diretorio}" criado.')
else:
    print(f'Diretório "{diretorio}" já existe.')


caminhoDeArquivo = os.path.join(diretorio, "dados.txt")

with open(caminhoDeArquivo, "w") as arquivo:
    for dados in myData:
        arquivo.write(dados + "\n")

print(f'Dados salvos no arquivo "{caminhoDeArquivo}".')