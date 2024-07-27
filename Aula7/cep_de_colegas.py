import requests

cepsAmigos = [42738320, 66815295, 14600971]

def descobrirCidade(cep:int) -> str:
    endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    #print(f'Status code: {endereco.status_code}')

    if endereco.status_code == 200:
        resultado = endereco.json()
        #print(resultado)
        cidade = resultado["localidade"]
    else:
        return {}
    return cidade

for cpEsc in cepsAmigos:
    nomeCidade = descobrirCidade(cpEsc)
    print(nomeCidade)