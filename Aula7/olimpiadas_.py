from faker import Faker

dicio = {}

faker = Faker('pt_BR')

idContador = 0
while idContador < 101:
    aluno = faker.name()
    idContador += 1
    dicio[idContador] = aluno

def matriculas(dicionario: dict) -> (list):
    timeAzul = []
    timeAmarelo = []
    for chave, valor in dicionario.items():
        if chave % 2 == 0:
            #print(f'{valor}, você pertence ao time Azul.')
            timeAzul.append(valor)
        else:
            #print(f'{valor}, você pertence ao time Amarelo.')
            timeAmarelo.append(valor)
    return timeAzul, timeAmarelo

result = matriculas(dicio)
print(f"""
        Time Azul: {result[0]}
        Time Amarelo: {result[1]}
    """)

'''
matriculaAluno = int(input('Digite sua matricula: '))
nomeAluno = input('Digite seu nome: ')
matriculas(matriculaAluno, nomeAluno)
'''
