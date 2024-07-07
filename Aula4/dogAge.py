# ChronoDog

pet = input('Nome do pet: ')
idadeCanina = int(input('Idade do pet (em anos): '.upper()))
sexo = input('Sexo (M/F): ')
quantidadeDeBanhos = int(input('Quantos banhos por ano: '))
porte = input('''
              Até 10kg = P
              De 10kg a 20 kg = M
              Acima de 20kg = G
              Porte (P/M/G): 
              '''.upper())

# Função para definir artigos/pronomes sexuais
if sexo == 'M':
    artigo = 'um'
    sx = 'Ele'
elif sexo == 'F':
    artigo = 'uma'
    sx = 'Ela'
else: 
    print('Sexo indefinido.')

# Função para definir Idade humana, porte impresso, valor e custo do banho com base no porte
if porte == 'P':
    idadeHumana = idadeCanina * 7
    porteImpresso = 'pequeno'
    valorBanho = 50
    custoBanho = 5
    lucro = (quantidadeDeBanhos * valorBanho) - (quantidadeDeBanhos * custoBanho)
elif porte == 'M':
    idadeHumana = idadeCanina * 8
    porteImpresso = 'médio'
    valorBanho = 60
    custoBanho = 15
    lucro = (quantidadeDeBanhos * valorBanho) - (quantidadeDeBanhos * custoBanho)
elif porte == 'G':
    idadeHumana = idadeCanina * 9
    porteImpresso = 'grande'
    valorBanho = 75
    custoBanho = 20
    lucro = (quantidadeDeBanhos * valorBanho) - (quantidadeDeBanhos * custoBanho)
else:
    print('Porte não identificado')

# Função para definir tempo de vida canino
if idadeHumana <= 18:
    tempoCanino = 'ainda é uma criança'
elif idadeHumana > 18 and idadeHumana <= 45:
    tempoCanino = 'é {} adolescente'.format(artigo)
elif idadeHumana > 45 and idadeHumana <= 72:
    tempoCanino = 'é {} adulto'.format(artigo)
elif idadeHumana > 72:
    tempoCanino = 'já é {} vovô'.format(artigo)

print(f'O pet {pet} de porte {porteImpresso} já possui {idadeHumana} anos, em idade humana. {sx} {tempoCanino} e nos últimos 12 meses o lucro com ele foi de R${lucro},00.')

