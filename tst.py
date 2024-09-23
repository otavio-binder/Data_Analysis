import pandas as pd
import Filtro_Neoplasia as Fn
import scipy
# Exemplo de uso
# D = ["*C180", "*C43A", "*C440", "*C341", "*C342", "*C183", "*C18X"]
# Fn.Filtro_Neoplasias(D)


csv = pd.read_csv("/home/andre/Documentos/Testes_Estatisticos/M2020_1.csv", sep = ";")

csv_cancerpulmao1 = csv.loc[csv['LINHAA'] ==  "*C341"]
csv_cancerpulmao2 = csv.loc[csv['LINHAA'] ==  "*C342"]

# Puxando coluna de idades
idades1 = csv_cancerpulmao1['IDADE']
idades2 = csv_cancerpulmao2['IDADE']

# Subtraindo 400 de todos os itens devido à nomenclatura do CID
idades1 = [idade - 400 for idade in idades1]
idades2 = [idade - 400 for idade in idades2]

print(f'Idades 1: {idades1}')
print(f'Idades 2: {idades2}')

# Valor do alpha
alpha = 0.05

stat, p_value = scipy.stats.shapiro(idades1)

print(f'Estatística do teste: {stat}')
print(f'Valor-p: {p_value}')

if p_value > alpha:
    print("Distribuição aparentemente normal (falha ao rejeitar H0)")
else:
    print("Distribuição não é normal (rejeita-se H0)")