import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

def plotar_velocidade(numero):
    dados = []

    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)
    
    tempo = [float(linha[0]) for linha in dados if linha[2] != '']
    velocidade = [float(linha[2]) for linha in dados if linha[2] != '']
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes = np.polyfit(tempo, velocidade, 1)
    velocidadeAjustada = np.polyval(coeficientes, x)
    
    plt.plot(tempo, velocidade, 'o', label='Velocidade (m/s)', color='blue', linewidth=0.5)
    plt.plot(x, velocidadeAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}t + {coeficientes[1]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Velocidade - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_velocidade.png', dpi=300, bbox_inches='tight')
    
    print("Coeficientes do ajuste de curva: ", coeficientes)
    #plt.show()
    plt.close()
    


if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_velocidade(i)