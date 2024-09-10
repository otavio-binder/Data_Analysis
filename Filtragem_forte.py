from matplotlib import pyplot as plt #plotar os graficos
import numpy as np #
from sys import argv # importar os arquivos que serao lidos
import Levenshtein as lv #auxilio nas filtragens
import pandas as pd #criacao de data frame
import re

#Essa função pega uma string e corta o primeiro e o ultimo caractere
def tablefield2int(s: str):  
    s = s[1 : len(s) - 1] 
    i = int(s)
    return i

#Essa função pega um dataframe e o transforma em um dicionário
def table2dic(M: np.ndarray):
    D = {} #dicionario vazio
    keys = M[0, :]  #definindo as chaves como a primeira linha da matriz
    #para cada chave, cria uma lista vazia no dicionario, onde cada lista tera um tamanho correspondente ao número de linhas restantes na matriz
    for k in range(0, len(keys)): 
        D[keys[k]] = [''] * (M.shape[0] - 1)
    #itera no restantes das linhas da matriz, comecando da segunda
    for n in range(1, M.shape[0]):
        L = M[n, :] #armazena a linha atual da matriz
        for k in range(0, len(keys)):
            D[keys[k]][n - 1] = L[k] #liga as chaves aos seus respectivos valores
    return D #retorna o dicionario

def remove_quotes_each_field(M: np.ndarray):
    N = M
    for i in range(0, M.shape[0]): #percorre todas as linhas da matriz
        for j in range(0, M.shape[1]): #percorre todas as colunas da matriz
            L = N[i, j] #armazena o valor de cada posição em L
            N[i, j] = L[1 : len(L) - 1] #remove o primeiro e o ultimo valor, que sao as aspas
    return N

def Filtro_Idade(D: dict):
    listaprocura = [] #criando lista vazia para armazenar os valores desejados
    cont = 0 # contador
    lista_armazena_posi = [] #lista para armazerna a posicao
    #idade1 = int(input("Digite a idade menor:(bota qualquer numero)" )) #input da menor idade que deseja buscar
    #idade2 = int(input("Digite a idade maior:(ta indo de 40 a 90 agr pq eu mexi no code) " )) #input da maior idade que deseja buscar
    idade1 = 40 + 400
    idade2 = 90 + 400 # soma 400 em ambas pois nos dados o 4 representa a idade em anos
    for i in range(len(D["IDADE"])): #percorrendo a coluna da IDADE
        b = int(D["IDADE"][i]) # transformando para inteiro para poder comparar
        if (b >= idade1) and (b <= idade2) : # se a idade estiver entre os dois valores, armazena tal
            b = b -400
            listaprocura.append(b) #armazenando a idade
            cont = cont + 1 #incrementando o contador
            lista_armazena_posi.append(i) #armazenando a posicao
    print(listaprocura) #imprime a lista das idades encontradas
    print("achou", cont, "elementos") # quantos elementos foram encontrados
    return lista_armazena_posi # retorna a lista de posicoes

def Filtro_Neoplasias(D:list, i):
    listaprocura = []
    cont = 0
    lista_armazena_posi = []
    procurado = ["*C34X" , "*C18X" , "*C43X"]
   # procurado = str(input("Digite o que quer procurar na coluna(*C34X, *C18X ou *C43X ): "))
    procuradopi = re.escape(procurado[i])
    procurado_regex = procuradopi.replace('X', r'[0-9X]')
    try:
        # Tentando compilar a expressão regular
        print(procurado)
        pattern = re.compile(procurado_regex)
    except re.error as e:
        print(f"Erro ao compilar a expressão regular: {e}")
        return 0

    for i in range(len(D)):
        value = str(D[i])
        if pattern.search(value):
            listaprocura.append(value)
            cont += 1
            lista_armazena_posi.append(i)
    #print(listaprocura)
    print("achou", cont, "elementos")
    return cont


#Essa função recebe o nome de um estado e retorna a chave dele
def Filtro_Estado(D: dict):
    listabuscadigitos = [] #criando lista vazia para armazenar os valores desejados
    contador = 0 # contador
    lista_armazena_posi = [] #lista que armazena a posicao
    procuradic = input("Digite o que deseja procurar(ex: CODMUNRES): ").upper() #selecionando a coluna onde vai procurar
    listadic = D[procuradic]
    dic_Mun = {12 : "ACRE" , 27 : "ALAGOAS", 16 : "AMAPÁ", 13 : "AMAZONAS", 29 : "BAHIA",
            	23 : "CEARÁ", 53 : "DF", 32 : "ESPÍRITO SANTO", 52 : "GOIÁS",
            	21 : "MARANHÃO", 51 : "MATO GROSSO", 50 : "MATO GROSSO DO SUL", 
            	31 : "MINAS GERAIS" , 15 : "PARÁ" , 25 : "PARAÍBA" , 41 : "PARANÁ" , 26 : "PERNAMBUCO",
            	22 : "PIAUÍ" , 33 : "RIO DE JANEIRO" , 24 : "RIO GRANDE DO NORTE" , 43 : "RIO GRANDE DO SUL" , 
            	11 : "RONDONIA" , 14 : "RORAIMA" , 42 : "SANTA CATARINA" , 35 : "SAO PAULO" ,
            	28 : "SERGIPE" , 17 : "TOCANTINS"} #dicionario com todos os estados
    endereco = input('Digite o nome do estado: ').upper() #digitar o nome do estado
    dic_orden = dict() #criacao de um novo dicionario
    for key, value in dic_Mun.items():
        distancia = lv.distance(endereco, value) #se digitar errado existe um parametro que verifica o que o usuario tentou digitar
        if	distancia <=2:
            print(f"{key} e {value}") #printa os valores
            dic_orden[key] = value #armazena na chave do novo dic no o valor do div_Mun
    for chv in range(len(listadic)):
        if listadic[chv] == '': #verifica se o valor nao esta vazio
            listabuscadigitos.append(100) #apenas um número para poder salvar a posição do lugar nulo 
        else:
            listabuscadigitos.append(int(listadic[chv])) #convertendo para inteiro
    for cnt in range(len(listabuscadigitos)):
        (listabuscadigitos[cnt]) = int(listabuscadigitos[cnt]/10000) #pegando somente os dois primeiros digitos
    for chave in dic_orden.keys():
        for cnt in range(len(listabuscadigitos)):
            if listabuscadigitos[cnt] == chave: #se for igual ao valor procurado, armazena na lista
                contador += 1 #incrementa o contador
                lista_armazena_posi.append(cnt) #armazenando as posicoes
    print("existem", contador ,"em", endereco) #fala aonde o estado e quanto encontrou
    print("posicoes armazenadas: ", lista_armazena_posi)
    return lista_armazena_posi # retornando as variaveis

#Um funcao que tem baseado em pegar o valor retonardo pelo filtro estado para achar as posições de uma outra key do dicionário
def usaPosicao(D: dict, function):
    teste = []
    cnt = 0
    listStoragePos = function
    key = print("Digite onde você quer usar a lista de posições: LINHAA")
    keyEscolhida = D["LINHAA"]
    for i in listStoragePos:
        teste.append(keyEscolhida[i])
        cnt += 1
    #print(teste)
    print("Contou ",cnt," elementos")
    return teste, cnt


#Funçao para plotar grafico:
def plot_graph(cancer_pulmao, cancer_colon, cancer_pele, labels):
    width = 0.25  # Largura das barras
    
    # Definir a posição das barras para cada grupo
    x_pulmao = np.arange(len(labels))
    x_colon = np.arange(len(labels)) + width
    x_pele = np.arange(len(labels)) + 2 * width
    
    # Criar as barras
    fig, ax = plt.subplots()
    bar1 = ax.bar(x_pulmao, cancer_pulmao, width, label='Câncer de Pulmão')
    bar2 = ax.bar(x_colon, cancer_colon, width, label='Câncer de Cólon')
    bar3 = ax.bar(x_pele, cancer_pele, width, label='Câncer de Pele')
    
    # Adicionar rótulos, título e legenda
    ax.set_xlabel('Ano')
    ax.set_ylabel('Casos')
    ax.set_title('Incidência de diferentes tipos de câncer ao longo dos anos')
    
    # Definir as posições e labels no eixo X para cada tipo de câncer
    ax.set_xticks(np.concatenate([x_pulmao, x_colon, x_pele]))
    ax.set_xticklabels(labels + labels + labels, rotation=45, ha="right")
    
    ax.legend()
    
    # Mostrar o gráfico
    plt.show()

def process_first_csv_as_dict(filename, sep=";"):
    """
    Processa o primeiro arquivo CSV, usando a primeira linha como as chaves do dicionário
    e todas as linhas seguintes como valores, removendo aspas dos campos.
    """
    with open(filename, 'r') as fid:
        # Lê todo o conteúdo do arquivo
        contents = fid.read()
    # Divide o conteúdo em linhas e depois em colunas
    lines = contents.split('\n')
    data = [line.split(sep) for line in lines if line]
    M = np.array(data) # Converte para uma matriz numpy
    M = remove_quotes_each_field(M) # Remove as aspas de cada campo
    # A primeira linha são as chaves
    keys = M[0]
    file_information = {key: [] for key in keys}
    # As linhas seguintes são os valores
    for row in M[1:]:
        for i, key in enumerate(keys):
            file_information[key].append(row[i])
    return file_information

def merge_other_csv_with_dict(dict_data, filename, sep=";"):
    """
    Processa o segundo arquivo CSV, removendo aspas dos campos e adicionando os valores às listas
    no dicionário existente. As chaves já foram definidas no primeiro arquivo e não serão modificadas.
    """
    with open(filename, 'r') as fid:
        # Lê todo o conteúdo do arquivo
        contents = fid.read()
    # Divide o conteúdo em linhas e depois em colunas
    lines = contents.split('\n')
    data = [line.split(sep) for line in lines if line]

    M = np.array(data) # Converte para uma matriz numpy
    M = remove_quotes_each_field(M)  # Remove as aspas de cada campo
    # Adiciona os valores ao dicionário existente
    for row in M[1:]:  # Ignora a primeira linha
        for i, key in enumerate(dict_data):
            dict_data[key].append(row[i])
    
    return dict_data

cancer_pulmao= []
cancer_colon = []
cancer_pele = []
arqvs = ['M2016_1.csv','M2016_2.csv','M2017_1.csv', 'M2017_2.csv', 'M2018_1.csv', 'M2018_2.csv', 'M2019_1.csv' , 'M2019_2.csv', 'M2020_1.csv', 'M2020_2.csv',
         'M2021_1.csv' , 'M2021_2.csv']
cnt_list = []

"""""
for i in range (5):
    #arqv_name = input("nome do arquivo ")
    D, arqv= prep_csv(arqvs[i])
    lista_neo = usaPosicao(arqv, Filtro_Idade(D))
    cancer_pulmao.append(Filtro_Neoplasias(lista_neo))
    cancer_colon.append(Filtro_Neoplasias(lista_neo))
    cancer_pele.append(Filtro_Neoplasias(lista_neo))
"""
for i in range(6):
    dict1 = process_first_csv_as_dict(arqvs[i])
    D = merge_other_csv_with_dict(dict1, arqvs[i+1])
    #dict3 = merge_other_csv_with_dict(dict2, "M2016_2.csv")
    #D = merge_other_csv_with_dict(dict3, 'M2016_21.csv')
    #print(D)
    # D, arqv= prep_csv(str(input("Digite o nome do arquivo: ")))
    lista_neo, cnt = usaPosicao(D, Filtro_Idade(D))
    a = 0
    cancer_pulmao.append(Filtro_Neoplasias(lista_neo, a))
    a = 1
    cancer_colon.append(Filtro_Neoplasias(lista_neo, a))
    a = 2
    cancer_pele.append(Filtro_Neoplasias(lista_neo, a))

cnt_list.append(cancer_pulmao)
cnt_list.append(cancer_colon)
cnt_list.append(cancer_pele)
    
labels = ['2016','2017', '2018','2019','2020', '2021']

print("Dados: Pulmao, Colon, Pele", cnt_list)
plot_graph(cancer_pulmao, cancer_colon, cancer_pele, labels)