from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import statsmodels
import numpy as np
import scipy.stats

N = 15
#Testes de normalidade a serem estudados

# Gerar dados aleatórios usando numpy
#x1= np.random.randn(N)  # Gera 500 números aleatórios de uma distribuição normal padrão
#x3 = x1*0.5  #O mesmos dados porém bem mais concentrados

# Criar um histograma
#h1 = plt.hist(x1, bins = 1000)  # O argumento "bins" define o número de intervalos no histograma

'''
#Descomentar tudo para ver histograma
plt.title('Histograma de Dados Aleatórios')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()

h2 = plt.hist(x3, bins = 1000)

#Descomentar tudo para ver histograma
plt.title('Histograma de Dados Aleatórios mais concentrados')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()
plt.show()
'''
alpha = 0.05

cShapiro = 0
cSmirnov = 0
cJaquera = 0 
cShapiroNormal = 0
cSmirnovNormal = 0
cJaqueraNormal = 0
cShapiroNaoNormal = 0
cSmirnovNaoNormal = 0
cJaqueraNaoNormal = 0

for i in range(100):
    # Gerar dados aleatórios usando numpy
    x3= np.random.randn(N)  # Gera 50 números aleatórios de uma distribuição normal padrão
    x1 = x3  #O mesmos dados porém bem mais concentrados

    # Criar um histograma
    h1 = plt.hist(x1, bins = 100)  # O argumento "bins" define o número de intervalos no histograma

    
    #Descomentar tudo para ver histograma
    ''''
    plt.title('Histograma de Dados Aleatórios')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.show()
    '''
    
    h2 = plt.hist(x3, bins = 100)
    
    #Descomentar tudo para ver histograma

    """"
    plt.title('Histograma de Dados Aleatórios mais concentrados')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.show()
    plt.show()
    """
    #Teste shapiro-wilk

    stats1, p1 = scipy.stats.shapiro(x1)

    if p1 > alpha:
        print("Ditribuição normal")
        cShapiroNormal = cShapiroNormal + 1
    else:
        print("distribuiçao nao é normal")
        cShapiroNaoNormal = cShapiroNaoNormal + 1
    print(p1)


    #Teste de Kolmogrov-smirnov (Só funciona se for teste de normalidade PADRÃO)
    from scipy.stats import kstest 

    stats2, p2 = kstest(x1, "norm")

    if p2 > alpha:
        print("Ditribuição normal")
        cSmirnovNormal = cSmirnovNormal +1
    else:
        print("distribuiçao nao é normal")
        cSmirnovNaoNormal = cSmirnovNaoNormal +1
    print(p2)

    #Teste de Jarquera-Barquera
    from scipy.stats import jarque_bera

    stats3, p3 = jarque_bera(x1)

    if p3 > alpha:
        print("Ditribuição normal")
        cJaqueraNormal = cJaqueraNormal +1
    else:
        print("distribuiçao nao é normal")
        cJaqueraNaoNormal = cJaqueraNaoNormal +1
    print(p3)

    #comparação dos testes

    if p1>p2 and p1>p3:
        print("O teste do shapiro tende a sair o numero maior")
        cShapiro = cShapiro + 1
        print()
    elif p2>p3 and p2>p1:
        print("O teste do smirnov tende a ser maior")
        cSmirnov = cSmirnov +1
        print()
    elif p3>p1 and p3>p2:
        print("O teste do jarque tende a ser maior")
        cJaquera = cJaquera +1
        print()
    else: 
        print("ERRO!")
    
print("Shapiro foi maior em", cShapiro, "teve seu número de distribuição normal de", cShapiroNormal, "e não normal de", cShapiroNaoNormal)
print()
print("Smirnov foi maior em", cSmirnov, "teve seu número de distribuição normal de", cSmirnovNormal, "e não normal de", cSmirnovNaoNormal )
print()
print("Jaquera foi maior em", cJaquera, "teve seu número de distribuição normal de", cJaqueraNormal, "e não normal de", cJaqueraNaoNormal )
