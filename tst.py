#importando módulos para a análise estátistica
import Levenshtein as lv
import numpy as np
import scipy as scip
import statsmodels as stmds
#importando módulos para a plotagem de gráficos
import matplotlib as mplt
import seaborn as seab
import pandas as pd 
import Levenshtein as lv
from urllib.request import urlopen

#Importando o sistema
from sys import argv

#importando nossa biblioteca de funções
import Filtro_Neoplasia as fn

#Criando o dicionario
if len(argv) >= 2:
    filename  = argv[1]
else:
    filename = "exemplopronto.csv"
fid = open(filename , "r") #abrindo o arquivo
contents = fid.read() #lendo o arquivo e salvando em contents
fid.close() #fechando o arquivo
file_information = [] 
contents = contents.split('\n')
for k in range(0, len(contents)):
    L = contents[k].split(';')
    file_information.append(L)

M = np.array(file_information)
M = fn.remove_quotes_each_field(M)
N = M[:, [1, 7]]
D = fn.table2dic(M)

#importando o dataframe
df_exemplopronto = pd.read_csv("exemplopronto.csv", sep = ";")

#testando
filtro = fn.Filtro_Neoplasias(D)
print(type(filtro))

# stats1, p1 = scip.stats.shapiro(x1)

# alpha = 0.05
# cShapiroNormal = 0
# if p1 > alpha:
#     print("Ditribuição normal")
# else:
#     print("distribuiçao nao é normal")
# print(p1)



