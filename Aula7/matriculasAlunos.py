#Criar um script para inserir matricula de 5 digitos, e verificar se é par ou impar

idsMatriculados = []

while len(idsMatriculados: list) < 5:
    matriculaAluno = int(input('Digite sua matricula: '))
    idsMatriculados.append(matriculaAluno)

for id in idsMatriculados:
    if id % 2 == 0:
        print(f'A matricula {id} é par.')
    else:
        print(f'A matricula {id} é impar.')