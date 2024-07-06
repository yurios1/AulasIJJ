from faker import Faker
import pandas as pd
from typing import list, dict

fake = Faker('pt-BR')

###Atividade

def criarPersona() -> dict:
        data = {
            "Nome": fake.name(),
            "Cidade": fake.city(),
            "Idade": fake.random_int(18, 100)
        }
        return data

def gerar_pessoas_em_qtd(number_of_personas: int) -> list:
        #personas_list = []
        #for _ in range(number_of_personas):
        #        personas_list.append(criarPersona())       
        #return personas_list
        #List Comprehension
        return [criarPersona() for _ in range(number_of_personas)]

                

def criar_df(data: dict) -> pd.Dataframe:
        df = pd.DataFrame(data)
        return df


def save_to_csv(filename: str, dataframe: pd):
        return 1