"""
Agora crie um script para com uma lista de frutas, e outra lista com o nome alergias. 
Insira uma fruta da lista de frutas na lista de alergias. 
Depois crie um for para cada item da lista passar por uma verificação em uma estrutura condicional para 
verificar se está essa fruta está contida na lista de alergias. 
Caso a fruta esteja na lista, imprima na tela o nome dela. 
"""
#Lista de Frutas
frutas = ['maçã', 'banana', 'laranja', 'uva']

#Lista de alergias
alergias = []

#Insira uma fruta da lista de frutas na lista de alergias.
alergias.append(frutas[2])

#For para analisar alergias
for i in frutas:
    if i in alergias:
        print(f'Usuário alergico a {i}')

print(alergias)
