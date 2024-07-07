valor = int(input('Digite um valor: '))
contador = 2
while contador < 7:
    match contador:
        case 2:
            resultado = valor * 2
            print(f'Dobro do valor inserido: {resultado}')
        case 3:
            resultado = valor * 3
            print(f'Triplo do valor inserido: {resultado}')
        case 4:
            resultado = valor ** 2
            print(f'Valor inserido ao quadrado: {resultado}')
        case 5:
            resultado = valor **(1/2)
            print(f'Raiz quadrada do valor inserido: {resultado}')
        case 6:
            resultado = valor **(1/3)
            print(f'Raiz cúbica do valor inserido: {resultado}')
    contador += 1