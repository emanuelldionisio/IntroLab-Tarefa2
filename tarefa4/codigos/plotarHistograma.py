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
    
    counts, bins, _ = plt.hist(tempos, bins=qtBins, edgecolor='black')
    mu, std = norm.fit(tempos)
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    
    bin_width = bins[1] - bins[0]
    p = norm.pdf(x, mu, std)
    p_scaled = p * len(tempos) * bin_width
    
    plt.plot(x, p_scaled, color='purple', linewidth=2)
    
    plt.xticks(bins, rotation=45)
    plt.title(f'Distribuição dos Tempos - {nome}')
    plt.xlabel('Tempo (µs)')
    plt.ylabel('Frequência')
    plt.grid(axis='y', alpha=0.2, color='black', linestyle='--')
    plt.savefig(f'tarefa4/imgs/{nome}_histograma.png', dpi=300, bbox_inches='tight')
    # plt.show()  
    print("Media dos tempos: ", mu)
    print("Gravidade (m/s²):", 2/((mu/1000000)**2))
    print("Desvio padrão dos tempos: ", std)