# Crie uma tupla com 5 dados
frutas = ("melancia", "laranja", "abacaxi", "banana", "maçã")
print(frutas)

#Altere a tupla para uma lista
bancaDeFrutas = list(frutas)
print(bancaDeFrutas)

#Insira 2 dados extras a essa lista
bancaDeFrutas.append("melão")
bancaDeFrutas.append("romã")
print(bancaDeFrutas)

#Remova o primeiro dado da lista
bancaDeFrutas.pop(0)
print(bancaDeFrutas)

#Remova o último dado da lista
bancaDeFrutas.pop()
print(bancaDeFrutas)

#Faça um print com o primeiro dado da lista
print(f"O primeiro item: {bancaDeFrutas[0]}")

#Faça um print com a quantidade de dados da lista
print(f"Existem {len(bancaDeFrutas)} itens na lista.")

#Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
pessoa = {
    "Nome": "Yuri",
    "Idade": 25,
    "Profissão": "QA"          
}

#Imprima somente o valor contido na chave Nome do dicionário
print(f"Usuário: {pessoa["Nome"]}")
