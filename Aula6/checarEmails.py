"""
O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. 
Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário 
tem o @jogajuntoinstituto.org no texto. 
Crie um input para verificar esse texto.
Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. 
Execute os testes, documente e suba os resultados no Bitrix da sua equipe. 
"""
#Lista para armazenar emails com dominio IJJ
dominioIJJ = []
#Lista para armazenar emails sem o dominio IJJ
emails = []

#Entrada de email
email = input("Digite seu email: ")

#Estrutura Condicional para verificar dominio do email
if '@jogajuntoinstituto.org' in email:
    print('Este email possui o domínio IJJ.')
    dominioIJJ.append(email)
else: 
    print('Email não possui o domínio IJJ.')
    emails.append(email)