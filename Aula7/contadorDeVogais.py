mensagem = input("Insira uma palavra ou frase: ").lower()

def contarVogais():
    letraA = 0
    letraE = 0
    letraI = 0
    letraO = 0
    letraU = 0
    vogais = "aeiouáéíóúãõàèìòùâêô"
    for letra in mensagem:
        if letra in vogais:
           match letra:
               case 'a'|'á'|'ã'|'à'|'â'|'ã':
                   letraA += 1
               case 'e'|'é'|'è'|'ê':
                   letraE += 1
               case 'i'|'í'|'ì':
                   letraI += 1
               case 'o'|'ó'|'õ'|'ò'|'ô':
                   letraO += 1
               case 'u'|'ú'|'ù':
                   letraU += 1
    contador = letraA + letraE + letraI + letraO
    return contador, letraA, letraE, letraI, letraO, letraU


resultado = contarVogais()
print(f"""
      O texto inserido tem {resultado[0]} vogais.
      Qtd. 'a': {resultado[1]}
      Qtd. 'e': {resultado[2]}
      Qtd. 'i': {resultado[3]}
      Qtd. 'o': {resultado[4]}
      Qtd. 'u': {resultado[5]}
      """)