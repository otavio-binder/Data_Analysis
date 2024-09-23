# map <leader><leader> :wall<cr>:!python %<cr>

from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import scipy
import statsmodels

def font_configuration():
    plt.rcParams.update({
        "text.usetex": False,
        "font.family": "serif",
        "font.serif": ["Palatino"],
        "font.size": 12,
    })

if __name__ == '__main__':
    font_configuration()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = np.linspace(0, 6 * np.pi, 10000)
    x1 = np.sin(t)
    x2 = np.cos(t)
    p, _ = find_peaks(x1)
    pmin, _ = find_peaks(-x1)
    xrange = np.max(t) - np.min(t)
    yrange = np.max(x1) - np.min(x1)
    ax.set_aspect(5.0 * xrange / yrange / 8.0)
    plt.tight_layout()
    plt.plot(t, np.max(x1) + np.zeros(shape = t.shape), '--k', linewidth = 0.8)
    plt.plot(t, np.min(x1) + np.zeros(shape = t.shape), '--k', linewidth = 0.8)
    plt.plot(t, x1, 'b', label = 'Seno')
    plt.plot(t, x2, '--g', label = 'Cosseno')
    plt.plot(t[p], x1[p], 'r.', markersize = 10.0)
    plt.plot(t[pmin], x1[pmin], 'k.', markersize = 10.0)
    plt.xlabel('Tempo ${t}$ (segundos)')
    plt.ylabel('${x_c(t)}$', rotation = 0.0, labelpad = 20)
    xticks_ = np.arange(0, 18.0, 5.0)
    xticks = np.zeros(shape = (len(xticks_) + len(p)))
    xticks[: len(xticks_)] = xticks_
    xticks[len(xticks_) :] = t[p]
    xticks = np.sort(xticks)
    # plt.xticks(xticks)
    plt.grid()
    plt.legend(fontsize=10.0)
    # plt.savefig('plot_example.png', dpi=300, bbox_inches = 'tight')
    input("Press enter")
    plt.show()
    #
    # Exemplo de vetores para comparação estatística
    N = 2000
    x1 = np.random.randn(N, ) * 0.5 + 2.0 # randn: gerador pseudoaleatório com distribuição Gaussiana padrão;
    #                                              (distribuição normal padrão) -> X ~ N((0, 1))
    #                                              Y = 0.5X + 2; Y ~ N((2, 0.25))
    x2 = np.random.rand(N, ) # rand: gerador pseudoaleatório com distribuição uniforme no intervalo [0, 1)
    #                        X ~ U([0, 1))
    # plt.plot(x1)
    # plt.show()
    # plt.plot(x2)
    # plt.show()
    h1, c1 = np.histogram(x1, bins = 100)
    epdf1 = (h1 / N) / (c1[1] - c1[0])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xrange = np.max(c1) - np.min(c1)
    yrange = np.max(epdf1) - np.min(epdf1)
    ax.set_aspect(5.0 * xrange / yrange / 8.0)
    plt.tight_layout()
    plt.plot((c1[1 :] + c1[: len(c1) - 1]) / 2.0, epdf1, label = 'PDF empírica', linewidth = 1.5)
    x = np.linspace(-2, 5, 10000)
    tpdf1 = 1.0 / np.sqrt(2 * np.pi * 0.25) * np.exp(-0.5 * (x - 2.0) ** 2 / (0.25))
    plt.plot(x, tpdf1, 'r--', label = 'PDF teórica', linewidth = 1.5)
    plt.xlabel('${x}$')
    plt.ylabel('${f_X(x)}$', rotation = 0.0, labelpad = 20)
    plt.grid()
    plt.legend(fontsize=12.0)
    input("Press enter")
    plt.show()
    # Teste de normalidade para x1
    s1, p1 = scipy.stats.shapiro(x1)
    print('Valor p para a hipótese nula de que x1 veio de distribuição mormal (no teste de Shapiro)')
    print(p1)
    # plt.savefig('plot_example.png', dpi=300, bbox_inches = 'tight')
    h2, c2 = np.histogram(x2, bins = 100)
    h2 = (h2 / N) / (c2[1] - c2[0])
    plt.plot((c2[1 :] + c2[: len(c2) - 1]) / 2.0, h2)
    plt.ylim((0, 1.2))
    input("Press enter")
    plt.show()
    # Teste de normalidade para x2
    s2, p2 = scipy.stats.shapiro(x2)
    print('Valor p para a hipótese nula de que x2 veio de distribuição mormal (no teste de Shapiro)')
    print(p2)
    # Teste de normalidade para x2
    # s2, p2 = statsmodels.api.stats.diagnostic.kstest_normal(x2)
    # print('Valor p para a hipótese nula de que x2 veio de distribuição mormal (no teste de Lilliefors)')
    # print(p2)
