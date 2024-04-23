# map <leader><leader> :wall<cr>:!python %<cr>

from matplotlib import pyplot as plt
import numpy as np
from sys import argv
from Levenshtein import distance as lv 

#Essa função pega uma string e corta o primeiro e o ultimo caractere
def tablefield2int(s):  
    s = s[1 : len(s) - 1]
    i = int(s)
    return i

#Essa função pega um dataframe e o transforma em um dicionário
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

#
def Digitos_Especifico(D):
    dig = int(input("Digite quantos digitos deseja pegar: "))
    va = str(input("Digite o codigo do municipio: "))
    va2 = (D[va])
    lista_resultado = []
    #print(lista["12"])
    for valores in va2:
        for valor in valores:
            lista_resultado.append(valor[:dig + 1])
        cd = "".join(lista_resultado)  
    #print(va2)    
    print(cd)

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

#Essa função recebe o nome de um estado e retorna a chave dele
def Filtro_Estado(D):
    listabuscadigitos = []
    contador = 0
    listadic = D["CODMUNRES"]
    dic_Mun = {12 : "ACRE" , 27 : "ALAGOAS", 16 : "AMAPÁ", 13 : "AMAZONAS", 29 : "BAHIA",
            	23 : "CEARÁ", 53 : "DF", 32 : "ESPÍRITO SANTO", 52 : "GOIÁS",
            	21 : "MARANHÃO", 51 : "MATO GROSSO", 50 : "MATO GROSSO DO SUL", 
            	31 : "MINAS GERAIS" , 15 : "PARÁ" , 25 : "PARAÍBA" , 41 : "PARANÁ" , 26 : "PERNAMBUCO",
            	22 : "PIAUÍ" , 33 : "RIO DE JANEIRO" , 24 : "RIO GRANDE DO NORTE" , 43 : "RIO GRANDE DO SUL" , 
            	11 : "RONDONIA" , 14 : "RORAIMA" , 42 : "SANTA CATARINA" , 35 : "SÃO PAULO" ,
            	28 : "SEGIPE" , 17 : "TOCANTINS"}
    endereco = input('Digite o nome do estado: ').upper()
    dic_orden = dict()
    for i,j in dic_Mun.items():
        distancia = lv(endereco, j)
        if	distancia <=2:
            print(f"{i} e {j}")
            dic_orden[i] = j
    for chv in range(len(listadic)):
        listabuscadigitos.append(int(listadic[chv])) # pegando os dois primeiro digittos
    for cnt in range(len(listabuscadigitos)):
        (listabuscadigitos[cnt]) = int(listabuscadigitos[cnt]/10000)
    for chave in dic_orden.keys():
        for cnt in range(len(listabuscadigitos)):
            if listabuscadigitos[cnt] == chave:
                contador = contador + 1
    print("existem", contador ,"em", endereco)
    return contador


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
    #Pegar_digito_especifico(D)
    #Digitos_Especifico(D)
    Filtro_Estado(D)
   # print(D["CODMUNRES"])