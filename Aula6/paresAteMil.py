"""
Crie a estrutura de uma tabuada para um valor inserido. O resultado deverá ser printado do valor multiplicado de 1 a 10. 
"""

# Estrutura de repetiçao para repetir até 1000
for i in range(1,1001):
    # Estrutura condicional para identificar e printar os números pares
    if i % 2 == 0:
        print(f'Par: {i}')