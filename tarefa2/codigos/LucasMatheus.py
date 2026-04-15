# %%
import csv
import matplotlib.pyplot as plt
import numpy as np

dados = []

with open('tarefa1/duplas/LucasMatheus.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dados.append(linha)

dados.pop(0)

def plotar_histograma(qtBins, nome=False):
    tempos = []
    if (not nome):
        nome = "Dupla 3"
        tempos = sorted([float(linha[2]) for linha in dados])
    else:
        tempos = sorted([float(linha[2]) for linha in dados if linha[0].upper() == nome.upper()])            
    counts, bins, _ = plt.hist(tempos, bins=qtBins, edgecolor='black')
    plt.xticks(bins, rotation=45)
    plt.title(f'Distribuição dos Tempos - {nome}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Frequência')
    plt.grid(axis='y', alpha=0.2, color='black', linestyle='--')
    plt.show()
    
    media = np.mean(tempos)
    
    print("Media dos tempos: ", media)
    print("Gravidade (m/s²):", 2/(media**2))
    print("Desvio padrão dos tempos: ", np.std(tempos))

plotar_histograma(8)