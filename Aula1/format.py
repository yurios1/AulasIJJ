nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
valor = 80.122355 

mensagem = 'Olá {0}, seja bem vindo!'.format(nome)

print(mensagem)
print(f'Olá {nome}, bem vindo! Vimos que tem {idade} anos.')
mensagemPromo = 'Você ganhou um saldo para compras de R${:.2f}, parabéns!!'.format(valor)
print(mensagemPromo)

typeNam = type(nome)
typeAge = type(idade)
typeVal = type(valor)

print(f"""
      Dados de Usuário
      Nome: {typeNam} 
      Idade: {typeAge}
      Valor: {typeVal}
      """)