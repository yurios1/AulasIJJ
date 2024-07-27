import requests

def pegarEndereco(cep:int) -> dict:
    endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    print(f'Status code: {endereco.status_code}')

    if endereco.status_code == 200:
        resultado = endereco.json()
        print(resultado)
    else:
        return {}
    return resultado

def verificarFrete(resultado: dict) -> str:
        estadosNordeste = ["BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
        if resultado["uf"] in estadosNordeste:
            frete = "O CEP informado possui frete grátis."
        else:
             frete = "O CEP informado não possui frete grátis."
        return frete
    

mensagem = int(input("Digite o CEP desejado: "))

enderecoDoCEP = pegarEndereco(mensagem)
freteDoCEP = verificarFrete(enderecoDoCEP)
print(freteDoCEP)