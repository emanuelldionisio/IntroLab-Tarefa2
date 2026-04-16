import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

def plotar_energiaK(numero):
    dados = []

    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)
    
    tempo = [float(linha[0]) for linha in dados if linha[4] != '']
    energiaK = [float(linha[4]) for linha in dados if linha[4] != '']
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes = np.polyfit(tempo, energiaK, 2)
    energiaKAjustada = np.polyval(coeficientes, x)
    
    plt.plot(tempo, energiaK, 'o', label='Energia Cinética (J)', color='blue', linewidth=0.5)
    plt.plot(x, energiaKAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}t² + {coeficientes[1]:.2f}t + {coeficientes[2]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Energia Cinética - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Energia Cinética (J)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_energiaK.png', dpi=300, bbox_inches='tight')
    
    print("Coeficientes do ajuste de curva: ", coeficientes)
    #plt.show()
    plt.close()
    


if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_energiaK(i)