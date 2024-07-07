nome = input('Nome do aluno: ')
notaAV1 = int(input('Digite a nota da AV1: '))
notaAV2 = int(input('Digite a nota da AV2: '))
notaAV3 = int(input('Digite a nota da AV3: '))
notaAV4 = int(input('Digite a nota da AV4: '))

media = (notaAV1 + notaAV2 + notaAV3 + notaAV4) /4

print(f'Olá, {nome}! Sua média é: {media} pontos.')