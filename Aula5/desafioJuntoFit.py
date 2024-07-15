'''
Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas
para presentear um acompanhante. Caso contrário, ele não se qualifica para o benefício.
Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer 
a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"
Quando ele completar 21 identificações seguidas, deve aparecer a mensagem 
"UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".
Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer 
"QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.
'''

clienteCodigo = input("Código do cliente: ")
contagem = 0
reset = 0
amigoPresente = 0
if amigoPresente == 0:
     while contagem < 21:
            dias = input("Registrar novo dia? [y/n]".lower())
            if (reset == 1 and dias == "y"):
                    contagem += 1
                    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
                    reset = 0
            else:
                if (dias == "y" and contagem == 20):
                    print(f"UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ \nDIAs: {contagem}")
                    amigoPresente = 1
                    break
                elif (dias == "y" and contagem > 0):
                    contagem += 1
                    print(f"VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO \nSALDO DE DIAS: {contagem}")
                elif (dias == "n" and contagem > 0):
                    contagem = 0
                    reset = 1
                elif (dias == "y" and contagem == 0):
                    print("""
                      BEM VINDO A PROMO JUNTOFIT 21 DIAS
                      FREQUENTE DURANTE 21 DIAS SEGUIDOS PARA GANHAR 1 MÊS GRÁTIS PARA UM ACOMPANHANTE.
                      """)
                    contagem += 1
                else:
                    print("COMECE HOJE A CONTAGEM DA SUA PROMOCAO, SEU PREMIO TE AGUARDA!")
else: 
    print("VOCê JÁ PARTICIPOU DA PROMOÇÃO JUNTOFIT.")
