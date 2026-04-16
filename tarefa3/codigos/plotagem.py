import posicao
import aceleracao
import velocidade
import energiaK
import energiaPot

if (__name__ == "__main__"):
    for i in range(1, 6):
        dadosposicao = posicao.plotar_posicao(i)
        velocidade.plotar_velocidade(i, dadosposicao)
        aceleracao.plotar_aceleracao(i, dadosposicao)
        energiaK.plotar_energiaK(i, dadosposicao)
        energiaPot.plotar_energiaPot(i, dadosposicao)