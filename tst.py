import re

def Filtro_Neoplasias(D: list):
    listaprocura = []
    cont = 0
    lista_armazena_posi = []

    procurado = str(input("Digite o que quer procurar na coluna (*C18X, *C43X ou *C34X): "))

    # Adicionando tratamento para caracteres especiais na entrada
    procurado = re.escape(procurado)
    procurado_regex = procurado.replace('X', r'[0-9X]')

    try:
        # Tentando compilar a expressão regular
        pattern = re.compile(procurado_regex)
    except re.error as e:
        print(f"Erro ao compilar a expressão regular: {e}")
        return 0

    for i, value in enumerate(D):
        if pattern.search(value):
            listaprocura.append(value)
            cont += 1
            lista_armazena_posi.append(i)

    print(listaprocura)
    print("achou", cont, "elementos")
    return cont

# Exemplo de uso
D = ["*C180", "*C43A", "*C440", "*C341", "*C342", "*C183", "*C18X"]
Filtro_Neoplasias(D)


