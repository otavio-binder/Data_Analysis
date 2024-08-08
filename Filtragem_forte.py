from matplotlib import pyplot as plt
import numpy as np
from sys import argv
from Levenshtein import distance as lv 
import pandas as pd

#Essa função pega uma string e corta o primeiro e o ultimo caractere
def tablefield2int(s: str):  
    s = s[1 : len(s) - 1]
    i = int(s)
    return i

#Essa função pega um dataframe e o transforma em um dicionário
def table2dic(M: np.ndarray):
    D = {}
    keys = M[0, :]
    for k in range(0, len(keys)):
        D[keys[k]] = [''] * (M.shape[0] - 1)
    for n in range(1, M.shape[0]):
        L = M[n, :]
        for k in range(0, len(keys)):
            D[keys[k]][n - 1] = L[k]
    return D

def remove_quotes_each_field(M: np.ndarray):
    N = M
    for i in range(0, M.shape[0]):
        for j in range(0, M.shape[1]):
            L = N[i, j]
            N[i, j] = L[1 : len(L) - 1]
    return N

def Filtro_Neoplasias(D:list):
    listaprocura = []
    cont = 0
    dic_Neoplasia= {"Neoplasia de colon": "C18", "Melanoma Maligno" : "C43", "Outras Neoplasias de pele" : "C44",
                    "Neoplasia de Pulmao": "C32" "C33" "C34"}
    lista_armazena_posi = []
    #coluna = str(input("Digite a coluna: "))
    #lista = D[coluna]
    procurado = str(input("Digite o que quer procurar na coluna: "))
    for i in range(len(D)):
        if (D[i] == procurado) :
            listaprocura.append(D[i])
            cont = cont + 1
            lista_armazena_posi.append(i)
    print(listaprocura)
    print("achou", cont, "elementos")
    return cont, lista_armazena_posi

#Essa função recebe o nome de um estado e retorna a chave dele
def Filtro_Estado(D: dict):
    listabuscadigitos = []
    contador = 0
    lista_armazena_posi = []
    procuradic = input("Digite o que deseja procurar(ex: CODMUNRES): ").upper()
    listadic = D[procuradic]
    dic_Mun = {12 : "ACRE" , 27 : "ALAGOAS", 16 : "AMAPÁ", 13 : "AMAZONAS", 29 : "BAHIA",
            	23 : "CEARÁ", 53 : "DF", 32 : "ESPÍRITO SANTO", 52 : "GOIÁS",
            	21 : "MARANHÃO", 51 : "MATO GROSSO", 50 : "MATO GROSSO DO SUL", 
            	31 : "MINAS GERAIS" , 15 : "PARÁ" , 25 : "PARAÍBA" , 41 : "PARANÁ" , 26 : "PERNAMBUCO",
            	22 : "PIAUÍ" , 33 : "RIO DE JANEIRO" , 24 : "RIO GRANDE DO NORTE" , 43 : "RIO GRANDE DO SUL" , 
            	11 : "RONDONIA" , 14 : "RORAIMA" , 42 : "SANTA CATARINA" , 35 : "SÃO PAULO" ,
            	28 : "SEGIPE" , 17 : "TOCANTINS"}
    endereco = input('Digite o nome do estado: ').upper()
    dic_orden = dict()
    for key, value in dic_Mun.items():
        distancia = lv(endereco, value)
        if	distancia <=2:
            print(f"{key} e {value}")
            dic_orden[key] = value
    for chv in range(len(listadic)):
        if listadic[chv] == '':
            listabuscadigitos.append(100) #apenas um número para poder salvar a posição do lugar nulo
        else:
            listabuscadigitos.append(int(listadic[chv])) #convertendo para inteiro
    for cnt in range(len(listabuscadigitos)):
        (listabuscadigitos[cnt]) = int(listabuscadigitos[cnt]/10000) #pegando somente os dois primeiros digitos
    for chave in dic_orden.keys():
        for cnt in range(len(listabuscadigitos)):
            if listabuscadigitos[cnt] == chave:
                contador += 1
                lista_armazena_posi.append(cnt) #armazenando as posicoes
    print("existem", contador ,"em", endereco)
    print("posicoes armazenadas: ", lista_armazena_posi)
    return lista_armazena_posi # retornando as variaveis

#Um funcao que tem baseado em pegar o valor retonardo pelo filtro estado para achar as posições de uma outra key do dicionário
def usaPosicao_Fitro_Estado(D: dict):
    teste = []
    cnt = 0
    listStoragePos = Filtro_Estado(D)
    key = input("Digite onde você quer usar a lista de posições: ")
    keyEscolhida = D[key]
    for i in listStoragePos:
        teste.append(keyEscolhida[i])
        cnt += 1
    print(teste)
    print("Contou ",cnt," elementos")
    return teste

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
    df_exemplopronto = pd.read_csv("exemplopronto.csv", sep = ";")
    M = np.array(file_information)
    M = remove_quotes_each_field(M)
    N = M[:, [1, 7]]
    D = table2dic(M)
    lista_neo=usaPosicao_Fitro_Estado(df_exemplopronto)
    Filtro_Neoplasias(lista_neo)