# map <leader><leader> :wall<cr>:!python %<cr>

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

#Filtros pequenos para auxiliar o principal Filtro_Estado
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

def Filtro_Neoplasias2(D: list):
    listaprocura = []
    cont = 0
    # Definindo os padrões de neoplasias usando expressões regulares
    dic_Neoplasia = {
        "Neoplasia de colon": r"^\*C18\d?X$",
        "Melanoma Maligno": r"^\*C43\d?X$",
        "Outras Neoplasias de pele": r"^\*C44\d?X$",
        "Neoplasia de Pulmao": r"^\*C34\d?X$"
    }
    lista_armazena_posi = []
    procurado = str(input("Digite o que quer procurar na coluna: "))
    for i in range(len(D)):
        value = str(D[i])
        # Comparar utilizando regex para ver se o valor corresponde ao padrão
        for nome, padrao in dic_Neoplasia.items():
            if re.match(padrao, procurado):
                dist = lv.distance(procurado, value)
                if dist <= 1:
                    listaprocura.append(value)
                    cont += 1
                    lista_armazena_posi.append(i)
                break
    print(listaprocura)
    print("Achou", cont, "elementos")
    return cont, lista_armazena_posi

def Filtro_Idade(D: dict):
    listaprocura = []
    cont = 0
    lista_armazena_posi = []
    idade1 = int(input("Digite a idade menor: " ))
    idade2 = int(input("Digite a idade maior: " ))
    idade1 = idade1 + 400
    idade2 = idade2 + 400
    for i in range(len(D["IDADE"])):
        b = int(D["IDADE"][i])
        if (b >= idade1) and (b <= idade2) :
            b = b -400
            listaprocura.append(b)
            cont = cont + 1
            lista_armazena_posi.append(i)
    print(listaprocura)
    print("achou", cont, "elementos")
    return cont, lista_armazena_posi, listaprocura


def Filtro_Assit_Med(D: dict):
    listaprocura = []
    cont = 0
    for i in D["ASSISTMED"]:
        if  i == '1':
            listaprocura.append(i)
            cont += 1
    print("antes da morte houveram", cont, "asstências medicas")
    return listaprocura

def Filtro_Cirurgia(D: dict):
    listaprocura0 = []
    cont = 0
    aux = int(input("digite 1 se quer saber se passou por cirurgia, ou 2 se não passou por cirurgia: "))
    for i in D["CIRURGIA"]:
        if  i == aux:
            listaprocura0.append(i)
            cont = cont + 1
    print("resultado obtido", cont)

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
            print(f"{key}e {value}")
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

# Essa função usa as posições dos dados que foram filtrados na função exportaPosicao()
# e aplica ela em outra cluna
def usaPosicao(D: dict):
    teste = []
    listStoragePos = exportaPosicao()
    key = str(input("Digite onde você quer usar a lista de posições: "))
    keyEscolhida = D[key]
    for i in listStoragePos:
        teste.append(keyEscolhida[i])
    print(teste)
    return teste

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

# Essa funcao recebe uma coluna e um filtro e retorna uma lista com as posicoes
# que aquele filtro aparece na coluna
def exportaPosicao(D: dict):
    keyOrigem = str(input("Digite a coluna a ser usada: ")).upper()
    filter = str(input("Digite o filtro a ser usado: " ))
    listStoragePos = []
    keyValues = D[keyOrigem]
    print(keyValues)
    for cnt in range(len(D[keyOrigem])):
        if filter == keyValues[cnt]:
            listStoragePos.append(cnt)
    print(listStoragePos)
    return listStoragePos

# Essa função recebe uma coluna e um valor, e retorna as linhas as quais os valores na coluna 
# escolhida sao iguais ao valor escolhido
def filtroDataframe(df: pd.DataFrame): #ESSA FUNção funciona
    coluna, filtro = input("exemplo: se voce quer linhas onde rows[8] == 2, digite: 8 2. ").split()
    coluna = int(coluna)
    #filtro = str(filtro)
    df_vazio = []
    for rows in df.values.tolist():
        if rows[coluna] == filtro: 
            df_vazio.append(rows)
    tabela = pd.DataFrame(df_vazio)
    print(tabela)
    return tabela

#Função igual a anterior, porém especifico para sempre pegar a idade e armazenar as outras infos
def filtroDataframe_Idade(dataframe: pd.DataFrame):
    filtro1 = int(input("digite a menor idade que deseja buscar: " ))
    filtro2 = int(input("digite a maior idade que deseja buscar: " ))
    filtro1 = filtro1 + 400
    filtro2 = filtro2 + 400
    df = []
    for rows in dataframe.values.tolist():
        if (rows[7] <= filtro2) and (rows[7] >= filtro1): #7 porque é a coluna da idade
            df.append(rows)
    tabela = pd.DataFrame(df)
    print(tabela)
    return tabela

def Filtrodataframe_Neoplasia(data_f: pd.DataFrame):
    dic_Neoplasia= {"*C18X": "Neoplasia de colon", "*C43X" : "Melanoma Maligno", "*C44X": "Outras Neoplasias de pele",
                    "*C33X": "Neoplasia de Pulmao", "*R571" : "teste"}
    dic_Listas_Neo = {41: "LINHAA", 42 : "LINHAB", 43 : "LINHAC"}
    procurado = str(input("Digite o que quer procurar na coluna(Ex: Neoplasia de colon): ")) 
    procurado2 = input("Digite qual linha deseja procurar(Ex: LINHAA, LINHAB ou LINHAC): ").upper()
    for key, value in dic_Neoplasia.items():
        distancia = lv(procurado, value)
        if	distancia <= 2:
            print(f"{key} e {value}")
    for key2, value2 in dic_Listas_Neo.items():
        if procurado2 == value2:
            print(f"{key2} e {value2}")
    resultados_do_filtro = (data_f[procurado2] == key)
    data_f_filtrado = data_f[resultados_do_filtro]
    print(data_f_filtrado)
    return data_f_filtrado

def filtroUsandoPandas(df: pd.DataFrame):
    coluna = str(input("Digite o nome da coluna (ex: NATURAL, CODMNRES): ")).upper()
    valor_especifico = input("Digite o valor especifico: ")
    if valor_especifico.isdigit():
        valor_especifico = int(valor_especifico)
    filtro = (df[coluna] == valor_especifico)
    df_filtrado = df[filtro]
    print(df_filtrado)
    return df_filtrado

# def exportarColuna()

#Essa função pede um estado e retorna o tipo de morte e a idade de todos os individuos
# def Morte_Idade():
#     count, estado_sel = Filtro_Estado(D)
#     dic_0 = {}
#     for i in M:
#         if 




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
    #idade_cria=filtroDataframe_Idade(df_exemplopronto)
    #filtroDataframe(idade_cria)
    #Filtro_Estado(df_exemplopronto)
    #Filtro_Idade(Neoplasia_desejada)
    #filtroUsandoPandas(df_exemplopronto)