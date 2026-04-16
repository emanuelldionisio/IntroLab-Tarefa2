import csv
import matplotlib.pyplot as plt
import numpy as np

dados = []
with open('tarefa5/dados/ultrassom.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dados.append(linha)
dados.pop(0)

def plotar_aceleracao(numero):
    
    tempo = [float(linha[numero*3+1])/10**6 for linha in dados]
    posicao = [float(linha[numero*3])/100 for linha in dados]

    print(tempo)
    print(posicao)
    
    x = np.linspace(min(tempo), max(tempo), 100)
    coeficientes, cov = np.polyfit(tempo, posicao, 2, cov=True)
    posicaoAjustada = np.polyval(coeficientes, x)
    incerteza = np.sqrt(np.diag(cov))

    print(incerteza)

    plt.plot(tempo, posicao, 'o', label='Posição (m)', color='blue', linewidth=1)
    plt.plot(x, posicaoAjustada, label=f'Ajuste de curva: {coeficientes[0]:.2f}t² + {coeficientes[1]:.2f}t + {coeficientes[2]:.2f}', color='red', linewidth=2)
    plt.legend()
    plt.title(f'Posição - Ultrassom {numero+1}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.grid()
    plt.savefig(f'tarefa5/imgs/Ultrassom{numero+1}_posicao.png', dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()

    velocidade = np.polyval([coeficientes[0]*2, coeficientes[1]], x)
    aceleracao = np.polyval([coeficientes[0]*2], x)
    
    plt.plot(x, posicaoAjustada, label='Posição (m)', color='red', linewidth=2)
    plt.plot(x, velocidade, label='Velocidade (m/s)', color='orange', linewidth=2)
    plt.plot(x, aceleracao, label=f'Aceleração (m/s²) - {coeficientes[0]*2:.2f}', color='green', linewidth=2)
    plt.legend()
    plt.grid()
    plt.title(f'Posição, velocidade e aceleração - Ultrassom {numero+1}')
    plt.xlabel('Tempo (s)')
    plt.savefig(f'tarefa5/imgs/Ultrassom{numero+1}_completo.png', dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()


if (__name__ == "__main__"):
    for i in range(0, 5):
        plotar_aceleracao(i)
    