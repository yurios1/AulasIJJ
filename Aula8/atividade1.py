import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Mateus", "Lucas", "Ruan", "Silvia", "Lupita"],
    "Idade": [18, 25, 23, 45, 33, 50, 32],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(data=dados)

df_recife = df[df["Cidade"] == "Recife"]

print(df_recife)