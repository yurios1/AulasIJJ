def saudacaoGame(nome):
    print(f"Olá {nome}, bem vindo a Terra Nova")

saudacaoGame("Yuri")

def soma(numbA, numbB):
    resultado = numbA + numbB
    return resultado

resultado_soma = soma(5,4)

if resultado_soma == 8:
    print(f'Resultado: {resultado_soma}')
else:
    print(f'O resultado não é 8. Resultado: {resultado_soma}')