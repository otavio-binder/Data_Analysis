import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Criando um DataFrame de exemplo com três fatores
data= {
    'grupo': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'tratamento': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'tempo': ['T1', 'T1', 'T2', 'T2', 'T2', 'T1', 'T1', 'T2', 'T1'],
    'resultado': [10, 12, 15, 8, 7, 10, 16, 18, 20]
}
moore = sm.datasets.get_rdataset("Moore", "carData", cache = True) 
data = moore.data
data = data.rename(columns ={"grupo" : "grupo", "tratamento" : "tratamento", "tempo" : "tempo"})

# Cria um modelo de ANOVA de três vias
model = ols('conformity ~ C(grupo, Sum) * C(tratamento, Sum) * C(tempo, Sum)', data = data).fit()

# Imprime a tabela ANOVA
tabela_anova = sm.stats.anova_lm(model, typ=2)
print(tabela_anova)
