import requests
from faker import Faker
import pandas as pd
from typing import Dict
import random
import json

urlCreateUser = "https://desafiopython.jogajuntoinstituto.org/api/users/"
urlLogin = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

bdUsuarios = []

def gerarUsuario() -> Dict[str, str]:
    faker = Faker('pt-BR')
    ddd = random.randint(11, 97)
    number = faker.numerify(text='9########')
    numberOrg = str(ddd) + number
    usuario = {
        "username": faker.user_name(),
        "email": faker.free_email(),
        "password": faker.password(),
        "phone": numberOrg,
        "address": faker.address(),
        "cpf": faker.cpf()
    }
    return usuario

def criarUsuario():
    usuarioApi = gerarUsuario()
    response = requests.post(urlCreateUser, json=usuarioApi)
    if response.status_code == 201:
        print('Usuário criado com sucesso.')
        bdUsuarios.append(usuarioApi)
        return usuarioApi
    else:
        print('Erro ao criar o usuário')

def logarUsuario(usuarioApi):
    usuarioLogin = {
        "email": usuarioApi["email"],
        "password": usuarioApi["password"]
    }

    responseLogin = requests.post(urlLogin, json=usuarioLogin)
    if responseLogin.status_code == 200:
        print('Login efetuado com sucesso.')
        loginSucedido = responseLogin.json()
        return loginSucedido
    else:
        print('Login negado. Verifique o Usuário ou senha e tente novamente.')
        print(responseLogin.status_code)

def verToken(loginSucedido):
    arquivoToken = open("Token de Acesso", "w")
    json.dump(loginSucedido, arquivoToken, indent=4)
    arquivoToken.close()

def convToCSV(bdUsuarios):
    usuariosCriados = pd.DataFrame(bdUsuarios)
    print(usuariosCriados)
    usuariosCriados.to_csv("Usuários criados",index=False)