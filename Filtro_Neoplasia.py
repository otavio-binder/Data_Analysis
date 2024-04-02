# map <leader><leader> :wall<cr>:!python %<cr>

from matplotlib import pyplot as plt
import numpy as np
from sys import argv

def tablefield2int(s):
    s = s[1 : len(s) - 1]
    i = int(s)
    return i

def table2dic(M):
    D = {}
    keys = M[0, :]
    for k in range(0, len(keys)):
        D[keys[k]] = [''] * (M.shape[0] - 1)
    for n in range(1, M.shape[0]):
        L = M[n, :]
        for k in range(0, len(keys)):
            D[keys[k]][n - 1] = L[k]
    return D

def Pegar_digito_especifico(D):
    digitos_chave = []
    aux = int(input("digite quantos digitos deseja pegar: "))
    aux2 = input("Digite a coluna que deseja pegar: ")
    cont = 0
    for i in D[aux2]:
        i = D[aux2]

def remove_quotes_each_field(M):
    N = M
    for i in range(0, M.shape[0]):
        for j in range(0, M.shape[1]):
            L = N[i, j]
            N[i, j] = L[1 : len(L) - 1]
    return N

def Filtro_Neoplasia(D):
    listaprocura = []
    cont = 0
    coluna = str(input("Digite a coluna: "))
    procurado = str(input("Digite o que quer procurar na coluna: "))
    for i in D[coluna]:
        if i == procurado:
            listaprocura.append(i)
            cont = cont + 1
    print(listaprocura)
    print("achou", cont, "elementos")

def Filtro_Idade(D):
    listaprocura = []
    cont = 0
    idade1 = int(input("Digite a idade menor: " ))
    idade2 = int(input("Digite a idade maior: " ))
    idade1 = idade1 + 400
    idade2 = idade2 + 400
    for i in D["IDADE"]:
        b = int(i)
        if (b > idade1) and (b < idade2) :
            b = b - 400
            listaprocura.append(b)
            cont = cont + 1
    print(listaprocura)
    print("achou", cont, "elementos")


def Filtro_Assit_Med(D):
    listaprocura = []
    cont = 0
    for i in D["ASSISTMED"]:
        if  i == '1':
            listaprocura.append(i)
            cont = cont + 1
    print("antes da morte houveram", cont, "asstências medicas")
    return listaprocura

def Filtro_Cirurgia(D):
    listaprocura0 = []
    cont = 0
    aux = input("digite 1 se quer saber se passou por cirurgia, ou 2 se não passou por cirurgia ")
    for i in D["CIRURGIA"]:
        if  i == aux:
            listaprocura0.append(i)
            cont = cont + 1
    print("resultado obtido", i)


def Filtro_Estado(D):
    listaprocura = []
    cont = 0
    Pegar_digito_especifico(D)


if __name__ == '__main__':
    #Verificando o arquivo
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
    M = remove_quotes_each_field(M)
    N = M[:, [1, 7]]
    D = table2dic(M)
    #print(D["IDADE"])
    #Filtro_Neoplasia(D)
    #Filtro_Idade(D)
    #print(D["ASSISTMED"])
    #Filtro_Idade(D)
    #Filtro_Cirurgia (D)
    Pegar_digito_especifico(D)