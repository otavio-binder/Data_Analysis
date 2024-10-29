from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import statsmodels.api as sm
import numpy as np
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
import pandas as pd

N = 40

#gerando dados dos grupos
grupo1 = np.random.randn(N)
grupo2 = np.random.randn(N)
grupo3 = np.random.randn(N)

#deixando os dados mais espalhados e mais aleatorios
grupo2 = (grupo2 + grupo1)*2
grupo3 = (grupo3 * grupo1)*4

print("grupo 1: ", grupo1)
print()
print("grupo 2: ", grupo2)
print()
print("grupo 3: ", grupo3)

# Aplicar o teste ANOVA
resultado_anova = f_oneway(grupo1, grupo2, grupo3)

# Exibir o valor de p
print("Valor de p:", resultado_anova.pvalue)

# Interpretar o resultado
if resultado_anova.pvalue < 0.05:
    print("Há evidências de que há diferença significativa entre os grupos.")
    print()
else:
    print("Não há evidências de diferença significativa entre os grupos.")
    print()

#Utilizando diferentes dados    
A = np.random.rand(N)
B = np.random.rand(N)
C = np.random.rand(N)

# Concatenando os dados em uma lista
valores = list(A) + list(B) + list(C)

# Criando uma lista para identificar os grupos
grupos = ['A'] * N + ['B'] * N + ['C'] * N
print("\n", grupos, "\n")
# Criando o DataFrame
dados = pd.DataFrame({'grupo': grupos, 'valor': valores})

# Ajustar o modelo ANOVA
modelo = ols('valor ~ grupo', data=dados).fit()

# Realizar a análise de variância
anova_resultado = sm.stats.anova_lm(modelo, typ=2)

# Exibir o resultado
print("Resultado com StatsModel", anova_resultado)
print()
print("Resultado do PR(>F)", anova_resultado.loc['grupo', 'PR(>F)'] )
#resultado legivel

if anova_resultado.loc['grupo', 'PR(>F)'] < 0.05:
    print("Há evidências de que há diferença significativa entre os grupos. TESTE PANDAS")
else:
    print("Não há evidências de diferença significativa entre os grupos. TESTE PANDAS")

