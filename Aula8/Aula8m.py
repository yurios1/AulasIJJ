import pandas as pd

dados = {
    "Nome": ["João", "Maria"],
    "Idade": [18, 25, 23, 45, 33]
}

df = pd.DataFrame(data=dados)

print(df)