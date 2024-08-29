import numpy as np
import matplotlib.pyplot as plt

def plot_graph(cancer_pulmao, cancer_colon, cancer_pele, labels_pulmao, labels_colon, labels_pele):
    width = 0.25  # Largura das barras
    
    # Definir a posição das barras para cada grupo
    x_pulmao = np.arange(len(labels_pulmao))
    x_colon = np.arange(len(labels_colon)) + width
    x_pele = np.arange(len(labels_pele)) + 2 * width
    
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
    ax.set_xticklabels(labels_pulmao + labels_colon + labels_pele, rotation=45, ha="right")
    
    ax.legend()
    
    # Mostrar o gráfico
    plt.show()

# Exemplo de uso
cancer_pulmao = [200, 520, 340, 760, 180]
cancer_colon = [320, 110, 520, 230, 640]
cancer_pele = [100, 280, 320, 250, 240]

labels_pulmao = ['2018', '2019', '2020', '2021', '2022']
labels_colon = ['2018', '2019', '2020', '2021', '2022']
labels_pele = ['2018', '2019', '2020', '2021', '2022']

plot_graph(cancer_pulmao, cancer_colon, cancer_pele, labels_pulmao, labels_colon, labels_pele)



