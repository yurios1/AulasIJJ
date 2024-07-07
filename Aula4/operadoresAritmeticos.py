valorA = int(input('Digite o valor: '))
valorB = int(input('Digite o próximo valor: '))

print(f'SOMA (+): {valorA + valorB}')
print(f'SUBTRAÇÃO (-): {valorA - valorB}')
print(f'MULTIPLICAÇÃO (*): {valorA * valorB}')
print(f'DIVISÃO (/): {valorA / valorB}')
print(f'DIVISÃO INTEIRA (//): {valorA // valorB}')
print(f'ELEVAÇÃO (**): {valorA ** valorB}')
print(f'RAIZ QUADRADA (**(1/2): ) {valorA**(1/2)} e {valorB**(1/2)}')

print('\nORDEM DE PRECEDENCIA')

print(f'Parênteses (): {valorA + (valorB - 4)}')
print(f'Elevação (**): {valorA + (valorB ** 2)}')
print('Demais operações')
