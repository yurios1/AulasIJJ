# If/Else/Elif - Match/Case
"""
USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, imprima na tela 
"Indivíduo possui idade mínima para dirigir"
USANDO ELSE: Complemente o script feito, imprimindo na tela 
"Indivíduo NÃO possui idade mínima para dirigir"
USANDO ELIF: Complemente o script feito, imprimindo na tela 
"Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir"
"""

# Entrada de idade do usuário
userAGe = int(input("Digite sua idade: "))

#Estrutura condicional para analisar idade do usuário
if userAGe > 18:
    print("Indivíduo possui idade mínima para dirigir.")
elif userAGe == 18 or userAGe == 17:
    "Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir"
else:
    print("Indivíduo NÃO possui idade mínima para dirigir")
