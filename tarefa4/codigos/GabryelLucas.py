import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from plotarHistograma import plotar_histograma

dados = []

with open('tarefa4/duplas/LucasGabryel.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dados.append(linha)

dados.pop(0)

if (__name__ == "__main__"):
    plotar_histograma(dados, 10, 2)