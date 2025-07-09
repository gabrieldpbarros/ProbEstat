import numpy as np
import pandas as pd
import scipy.stats as st

#def getStats(series: np.ndarray):
def getStats():
    series = np.random.randint(1, 1000, 200)
    disp_size = series.size

    # Inicializa um dicionário que conterá todas as medidas de posição e dispersão da sérieww
    # passada como argumento 
    stats_dic = {}

    # Medidas de poisção
    stats_dic["mean"] = np.mean(series)
    stats_dic["median"] = np.median(series)
    aux, counter = np.unique(series, return_counts=True)
    stats_dic["mode"] = aux[np.argmax(counter)]

    # Medidas de dispersão
    stats_dic["mean deviation"] = np.sum(np.abs(series - stats_dic["mean"])) / disp_size # DM = (sum(|xi - media|)) / qtd_amostras
    stats_dic["variance"] = np.var(series) # VAR = (sum(xi - media)^2) / qtd_amostras
    stats_dic["standard deviation"] = np.std(series)
    print(series)
    print()
    print(stats_dic)

getStats()