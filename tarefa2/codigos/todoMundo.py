# %%
import csv
import matplotlib.pyplot as plt
import numpy as np
from plotarHistograma import plotar_histograma

from EmanuelFilipe import dados as dados1
from GabryelLucas import dados as dados2
from LucasMatheus import dados as dados3

dados = dados1 + dados2 + dados3

if (__name__ == "__main__"):
    plotar_histograma(dados, 10, 4)