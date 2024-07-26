def matriculas(numeroMAt: int, nome: str) -> str:
    if numeroMAt % 2 == 0:
        print(f'{nome}, você pertence ao time Azul.')
    else:
        print(f'{nome}, você pertence ao time Amarelo.')

matriculaAluno = int(input('Digite sua matricula: '))
nomeAluno = input('Digite seu nome: ')
matriculas(matriculaAluno, nomeAluno)