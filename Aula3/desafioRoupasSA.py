# A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:
# Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% 
# em sua próxima compra. Use o cupom PAULAÉ10.

nome = "Julio"
sobrenome = "Silva"
mesDaCompra = "Fevereiro"
valorDaCompra = 1008.15
desconto = 10
cupomPromocional = '{nome.upper}É{desconto}'

print(f'Olá, {nome + ' ' + sobrenome}, ')