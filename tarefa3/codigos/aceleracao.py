import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plotar_aceleracao(numero, posicao):
    dados = []
    with open(f'tarefa3/dados/Tracker{numero}.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
    dados.pop(0)
    
    tempo = [float(linha[0])/32000 for linha in dados if linha[2] != '']
    tempo = tempo[len(tempo)-len(posicao):]
    
    velocidade = np.gradient(posicao, tempo)
    aceleracao = np.gradient(velocidade, tempo)

    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes, cov = np.polyfit(tempo, aceleracao, 0, cov=True)
    aceleracaoAjustada = np.polyval(coeficientes, x)
    print(f"Incerteza do ajuste de curva da aceleração {numero}: ", np.sqrt(cov[0][0]))
    
    #plt.ylim(-15, 0)
    plt.plot(tempo, aceleracao, 'o', label='Aceleração (m/s²)', color='blue', markersize=1)
    plt.plot(x, aceleracaoAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Aceleração - Tracker {numero}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Aceleração (m/s²)')
    plt.grid()
    plt.savefig(f'tarefa3/imgs/Tracker{numero}_aceleracao.png', dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()

if (__name__ == "__main__"):
    for i in range(1, 6):
        plotar_aceleracao(i)
    