#Importando biblioteca random para criar um numero aleatorio
import random

#Variável de finalização
terminar = False
reiniciar = True

#Estrutura de repetição para reiniciar o jogo
while reiniciar != False:
    #Criando o número secreto
    numeroSecreto = int(random.randint(1, 100))
    
    #Estrutura de repetição para receber chutes até o correto
    while terminar == False:
        #Variável para coletar chute
        chute = int(input("Digite o número que deseja chutar entre 1 e 100: "))
        #Estrutura condicional se o número é correto, menor ou maior que o chute
        if chute == numeroSecreto:
            print('Parabéns! Você acertou.')
            terminar = True
        #Menor que chute
        elif chute < numeroSecreto:
            print(f'O numero secreto e maior que {chute}')
        #Maior que chute
        elif chute > numeroSecreto:
            print(f'O numero secreto e menor que {chute}')
        #Valores incorretos
        else: 
            print('Valor incorreto inserido.')
    
    #Estrutura condicional para reiniciar o jogo
    reinicio = input('Deseja jogar denovo? [y/n]: ').lower()
    if reinicio == 'y':
        reiniciar = True
        terminar = False
    elif reinicio == 'n':
        reiniciar = False
    else:
        print('Valor inserido incorreto.')

