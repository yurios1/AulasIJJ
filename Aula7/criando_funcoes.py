#Criar função para imprimir uma mensagem de boas vindas para nomes específicos
def saudacaoGame(nome):
    print(f"Olá {nome}, bem vindo a Terra Nova")

saudacaoGame("Yuri")

#Criar função para somar 2 valores
def soma(numbA, numbB):
    resultado = numbA + numbB
    return resultado

resultado_soma = soma(5,4)

if resultado_soma == 8:
    print(f'Resultado: {resultado_soma}')
else:
    print(f'O resultado não é 8. Resultado: {resultado_soma}')

#Criar função para calcular preço total de uma compra com descontos
def precoLiquido(valorCompra, desconto):
    porcentDesconto = valorCompra * (desconto / 100)
    valorFinal = valorCompra - porcentDesconto
    return valorFinal 

valorDaCompra = int(input('Digite o valor da compra: '))
descontoAplicado = int(input('Digite a porcetagem de desconto aplicado: '))
pagamento = precoLiquido(valorDaCompra, descontoAplicado)
print(f'O valor a ser pago é: {pagamento}')
