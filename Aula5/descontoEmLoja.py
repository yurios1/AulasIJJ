"""
Na "FashionStyle", para um cliente obter 10% de desconto em suas compras, a compra deve ser de pelo menos R$250,00 e 
para obter 30%, a compra deve ser acima de R$500,00. Caso contrário, nenhum desconto é aplicado.
No caixa, haverá uma tela voltada para o cliente. Ao passar o produto, caso cumpra o requisito da promoção, 
aparecerá a mensagem:
Caso o cliente não cumpra o requisito, deve aparecer 'POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.'
Caso o cliente faça uma compra acima de R$250,00 'PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00'
Caso o cliente faça uma compra acima de R$500,00 'PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%'
"""

valorDaCompra = int(input("Valor do produto: "))
desconto = 0
if valorDaCompra >= 500:
    desconto = 30
    pagamento = valorDaCompra - (valorDaCompra * (desconto / 100))
    print(f"PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%! \nValor para pagamento: {pagamento}")
elif valorDaCompra >= 250:
    desconto = 10
    pagamento = valorDaCompra - (valorDaCompra * (desconto / 100))
    print(f"PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00. \nValor para pagamento: {pagamento}")
else:
    desconto = 0
    print(f"POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA. \nValor para pagamento: {valorDaCompra}")
