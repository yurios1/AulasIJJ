from faker import Faker

dicio = {}

faker = Faker('pt_BR')

idContador = 0
while idContador < 101:
    aluno = faker.name()
    idContador += 1
    dicio[idContador] = aluno

print(dicio)
