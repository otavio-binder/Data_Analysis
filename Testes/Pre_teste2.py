from urllib.request import urlopen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
import scipy.stats

np.set_printoptions(precision = 10, suppress= True) # precisão do grafico
pd.set_option("display.width", 100) #tamanho do gráfico

try:
    salario = pd.read_csv("tabela.de.salario") #tentativa de importar a tabela
except:
    url = "http://stats191.stanford.edu/data/salary.table" #importando os dados
    fh = urlopen(url)
    salario = pd.read_table(fh) #lendo a tabela importada
    salario.to_csv("table.de.salario") #convertendo para csv

E = salario.E
M = salario.M
X = salario.X
S = salario.S
print(salario)

#plotando o gráfico
plt.figure(figsize=(6 ,6))
symbols = ["^", "D"]
colors = ["r", "g", "blue"]
factor_groups = salario.groupby(["E", "M"])
for values, group in factor_groups:
    i, j = values
    plt.scatter(group["X"], group["S"], marker=symbols[j], color=colors[i - 1], s=144)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

#Teste de normalidade
s1, p1 = scipy.stats.shapiro(salario.S)
print(p1)
