from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.stats.weightstats import ttest_ind

#Estudando algumas funções do teste do T student com a amostra aleatoria
N = 1000
m1 = 0
m2 = 0

#histograma
x1 = np.random.randn(N) #randn gerador pseudo-aleatório de distribuição normal padrão
x2 = np.random.randn(N) #randn gerador pseudo-aleatório de distribuição normal padrão
h1 = plt.hist(x1, bins = 1000)  # O argumento "bins" define o número de intervalos no histograma
h2 = plt.hist(x2, bins = 1000)  # O argumento "bins" define o número de intervalos no histograma

estimatedmean1 = np.mean(x1)
estimatedmean2 = np.mean(x2)

for i in range (N):
    m1 = x1[i] + m1
    m2 = x2[i] + m2

m1 = m1/N
m2 = m2/N

print("valor de m1", m1, "valor de m2", m2)
print()
print("valor de estimated1", estimatedmean1, "valor de estimated2", estimatedmean2)
print()
#teste de normalidade
 
stats1, p1 = scipy.stats.shapiro(x1)
stats2, p2 = scipy.stats.shapiro(x2)
print(p1)

#teste t para uma amostra

if p1 > 0.05:
    t_stats1, p_value1 =  scipy.stats.ttest_1samp(x1, m1)  # Teste se a média da amostra é igual a m1
    print("Estatística t para uma amostra:", t_stats1)
    print()
    print("Valor de p para uma amostra:", p_value1)
    print()

    #teste t para duas amostras
    '''
    t_stats2, p_value2 =  scipy.stats.ttest_ind(m1, m2)  # Teste se a média da amostra é igual a m2
    print("Estatística t para duas amostra:", t_stats2)
    print()
    print("Valor de p para duas amostra:", p_value2)
    '''
else:
    print("A normalidade foi rejeitada :thumbs up:")