from faker import Faker
import pandas as pd

fake = Faker('pt-BR')

persona = {
    "Nome": fake.name(),
    "Cidade": fake.city(),
    "Idade": fake.random_int(18, 100)
}

print(persona)

###Atividade

def criarPersona(number_of_personas: int) -> list:
    list_Personas = []
    
    for i in range(number_of_personas):
        data = {
            "Nome": fake.name(),
            "Cidade": fake.city(),
            "Idade": fake.random_int(18, 100)
        }
        list_Personas.append(data)

    return list_Personas

"""
persona_criada = criarPersona(1)
print(persona_criada)
for i in range(10):
    criarPersona()
"""

listaPersonas = criarPersona(20)

df_lista_de_personas = pd.DataFrame(listaPersonas)

#df_lista_de_personas.to_csv('Personas_para_Test', index=False)
