import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

def plotar_posicao(numero):

    dados = []

    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)

    tempo = [float(linha[0])/32000 for linha in dados if linha[2] != '']
    posicao = [float(linha[2])/1000 for linha in dados if linha[2] != '']
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes = np.polyfit(tempo, posicao, 2)
    posicaoAjustada = np.polyval(coeficientes, x)
    
    plt.plot(tempo, posicao, 'o', label='Posição (m)', color='blue', markersize=1)
    plt.plot(x, posicaoAjustada, '--', label=f'Ajuste de curva: {coeficientes[0]:.2f}t² + {coeficientes[1]:.2f}t + {coeficientes[2]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Posição - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_posicao.png', dpi=300, bbox_inches='tight')
    
    print("Coeficientes do ajuste de curva: ", coeficientes)
    #plt.show()
    plt.close()
    
if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_posicao(i)
