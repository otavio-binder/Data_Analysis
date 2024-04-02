from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.stats.weightstats import ttest_ind

#Estudando algumas funções do teste do T student com a amostra aleatoria
N = 1000
m1 = 10
m2 = 8

#histograma

x1 = np.random.randn(N) + m1 #randn gerador pseudo-aleatório de distribuição normal padrão (ANTESS)
x2 = np.random.randn(N) + m2 #randn gerador pseudo-aleatório de distribuição normal padrão (DEPOISS)
h1 = plt.hist(x1, bins = 1000)  # O argumento "bins" define o número de intervalos no histograma
h2 = plt.hist(x2, bins = 1000)  # O argumento "bins" define o número de intervalos no histograma

#teste de normalidade
 
stats1, p1 = scipy.stats.shapiro(x1)
stats2, p2 = scipy.stats.shapiro(x2)
print("valor de p1", p1)
print()
print("valor de p2", p2)

#teste t para uma amostra

if p1 > 0.05 and p2 > 0.05:

    #teste t para duas amostras
    
    t_stats2, p_value2 =  scipy.stats.ttest_rel(x1, x2)  # Teste se a média da amostra é igual a m2(o REL significa pareado, e o IND é não pareado)
    print("Estatística t para duas amostra:", t_stats2)
    print()
    print("Valor de p para duas amostra:", p_value2)
    
else:
    print("A normalidade foi rejeitada :thumbs up:")