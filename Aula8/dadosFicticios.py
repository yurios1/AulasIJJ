import pandas as pd

dados = pd.read_csv('./dados_Ficticios.csv')

df = pd.DataFrame(data=dados)

filtroIdade = df[df["idade"] > 40]
filtroRendaMaior5 = df[df["renda"] < 5000]
filtroRendaMaior15 = df[df["renda"] < 15000]

print(filtroIdade)
print(filtroRendaMaior5)
print(filtroRendaMaior15)
