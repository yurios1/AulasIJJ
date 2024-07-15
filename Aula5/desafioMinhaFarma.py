'''
Na "Farmácia MINHA FARMA", clientes que comprarem produtos no valor total de R$ 100 ou mais ganham um vale-compras 
de R$ 10 para a próxima compra. Compras de valores menores não se qualificam para o vale.
Ao conseguir atingir o limite mínimo da compra estabelecido na promoção, deve aparecer na nota fiscal 
"SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.".
Caso o cliente não cumpra o requisito, deve aparecer 
"OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE 
R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?"
'''
empresa = {
    'nome fantasia': 'FARMÁCIA MINHA FARMA',
    'CNPJ': '13.245.324/0001-89'
}
cliente = {
    'nome': '',
    'cpf': '',
    'saldo': 0,
}

produtos = {
    "contonetes": 7.99,
    "dipirona": 2.99,
    "xarope": 8.99,
    "creme corporal": 9.99,
    'paracetamol': 4.99,
}

listaDeCompras = {}

def criarCliente():
    cliente['nome'] = input('Nome do cliente: ')
    cliente['cpf'] = input('CPF do cliente: ')

def comprar() -> dict:
    finalizar = False
    compras = {}
    while finalizar == False:
        produto = input(f'Escolha seus produtos:\n{produtos}').lower()
        quantidade = int(input('Quantidade: '))
        if produto in produtos:
            compras[produto] = quantidade
            print('Produto adicionado.')
        else:
             print('Produto não encontrado.')
        adicionar = input('Adicionar novo produto? [y/n]').lower()
        if adicionar == 'n':
            finalizar = True
    return compras

criarCliente()

carrinho = comprar()

for i in carrinho:
    valor = carrinho[i] * produtos[i]
    listaDeCompras[i] = valor


valorCompras = sum(listaDeCompras.values())
if valorCompras >= 100:
    cliente['saldo'] = 10
    mensagem = "SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO."
else:
    mensagem = '''
    OBRIGADO POR ESCOLHER A MINHA FARMA.
    VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS 
    GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO 
    PARA A PRÓXIMA COMPRA?
    '''


print(f"""
    NOTA FISCAL 
    {empresa['nome fantasia']}
    CNPJ: {empresa['CNPJ']}

    Cliente: {cliente['nome']}
    CPF: {cliente['cpf']}

    Compras:
    {listaDeCompras}
    Total: R${valorCompras},00

    {mensagem}
      """)

        
    