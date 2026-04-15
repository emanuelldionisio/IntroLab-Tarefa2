import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def plotar_histograma(dados, qtBins, nome):
    tempos = []
    if (isinstance(nome, int)):
        nome = f"Dupla {nome}"
        tempos = sorted([float(linha[2]) for linha in dados])
    elif (nome == "Todos"):
        nome = "Grupo"
        tempos = sorted([float(linha[2]) for linha in dados])
    else:
        tempos = sorted([float(linha[2]) for linha in dados if linha[0].upper() == nome.upper()])            
    
    counts, bins, _ = plt.hist(tempos, bins=qtBins, density=True, edgecolor='black')
    mu, std = norm.fit(tempos)
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    
    plt.plot(x, p, 'r', linewidth=2, color='purple')
    plt.xticks(bins, rotation=45)
    plt.title(f'Distribuição dos Tempos - {nome}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Frequência')
    plt.grid(axis='y', alpha=0.2, color='black', linestyle='--')
    plt.savefig(f'tarefa2/imgs/{nome}_histograma.png', dpi=300, bbox_inches='tight')
    # plt.show()

    
    
    print("Media dos tempos: ", mu)
    print("Gravidade (m/s²):", 2/(mu**2))
    print("Desvio padrão dos tempos: ", std)