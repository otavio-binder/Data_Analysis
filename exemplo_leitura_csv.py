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

def remove_quotes_each_field(M):
    N = M
    for i in range(0, M.shape[0]):
        for j in range(0, M.shape[1]):
            L = N[i, j]
            N[i, j] = L[1 : len(L) - 1]
    return N

if __name__ == '__main__':
    if len(argv) >= 2:
        filename  = argv[1]
    else:
        filename = 'exemplopronto.csv'
    fid = open(filename, 'r')
    contents = fid.read()
    fid.close()
    file_information = []
    contents = contents.split('\n')
    for k in range(0, len(contents)):
        L = contents[k].split(';')
        file_information.append(L)
    # print(file_information)
    # print(file_information)
    # print('')
    # print('')
    # print(file_information[4])
    # print('')
    # print('Coluna 5 da linha 7:')
    # print(file_information[6][4])
    # print(tablefield2int(file_information[6][4]))
    # print(len(file_information))
    # print(len(file_information[0]))
    M = np.array(file_information)
    M = remove_quotes_each_field(M)
    # print(M[3, 5])
    N = M[:, [1, 7]]
    # print(N)
    D = table2dic(M)
    print(D["LINHAA"])
    print(D['IDADE'][4:8])
    print(D['PESO'])
    print(D['CAUSABAS_O'])
    print(D['CAUSABAS'])
