import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plotar_energiaK(numero, posicao):
    dados = []

    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)
    
    tempo = [float(linha[0])/32000 for linha in dados if linha[2] != '']
    tempo = tempo[len(tempo)-len(posicao):]
    
    velocidade = np.gradient(posicao, tempo)
    massa = 7.9*10**(-3)
    
    energiaK = [0.5*massa*v**2 for v in velocidade]
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes, cov = np.polyfit(tempo, energiaK, 2, cov=True)
    energiaKAjustada = np.polyval(coeficientes, x)
    print(f"Incerteza do ajuste de curva energia cinética {numero}: ", np.sqrt(cov[0][0]))
    plt.ylim(0,0.1)
    plt.plot(tempo, energiaK, 'o', label='Energia Cinética (J)', color='blue', markersize=1)
    plt.plot(x, energiaKAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}t² + {coeficientes[1]:.2f}t + {coeficientes[2]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Energia Cinética - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Energia Cinética (J)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_energiaK.png', dpi=300, bbox_inches='tight')
    
    #plt.show()
    plt.close()
    


if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_energiaK(i)