"""
Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.
Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.
Solicitação de Entrada:
Implementem a solicitação de entrada de uma palavra (string).
Contagem de Vogais:
Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra.
"""
#Função para receber um entrada do usuário, contar as vogais e retornar a quantidade de vogais e a palavra inserida
def contarVogais() -> tuple:
    palavra = input("Digite a palavra ou frase para contar as vogais: ").lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    quantidadeVogais = 0
    for letra in palavra:
        if letra in vogais:
            quantidadeVogais += 1
    return quantidadeVogais, palavra

#Chamando a função e atribuindo a uma variável
texto = contarVogais()
print(type(texto))
print(f"Existem {texto[0]} vogais na palavra {texto[1]}.")


    