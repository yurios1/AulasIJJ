"""
Faça um for e imprima na tela todos os numeros de 1 até 1000. 
Depois, crie uma estrutura condicional para descobrir e printar apenas os números que forem par.  
"""

# Input do valor para gerar a tabuada
valor = int(input('Digite o valor que deseja criar a tabuada: '))

# estrutura de repeticao para imprimir tabuada
for i in range(1,11):
    print(f'{valor}x{i}:{valor*i}')