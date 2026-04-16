import csv
import matplotlib.pyplot as plt
import numpy as np

def plotar_energiaPot(numero):
    dados = []
    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)
    
    tempo = [float(linha[0]) for linha in dados if linha[5] != '']
    energiaPot = [float(linha[5]) for linha in dados if linha[5] != '']
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes = np.polyfit(tempo, energiaPot, 2)
    energiaPotAjustada = np.polyval(coeficientes, x)
    
    plt.plot(tempo, energiaPot, 'o', label='Energia Potencial (J)', color='blue', linewidth=1)
    plt.plot(x, energiaPotAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}t² + {coeficientes[1]:.2f}t + {coeficientes[2]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Energia Potencial - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Energia Potencial (J)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_energiaPot.png', dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()

if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_energiaPot(i)
    