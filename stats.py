import numpy as np
import pandas as pd
import scipy.stats as st
from typing import Dict

def getStats(series: np.ndarray) -> Dict[str, np.number]:
    disp_size = series.size

    # Inicializa um dicionário que conterá todas as medidas de posição e dispersão da sérieww
    # passada como argumento 
    stats_dict = {}

    # Medidas de poisção
    stats_dict["mean"] = np.mean(series)
    stats_dict["median"] = np.median(series)
    aux, counter = np.unique(series, return_counts=True)
    stats_dict["mode"] = aux[np.argmax(counter)]

    # Medidas de dispersão
    stats_dict["mean deviation"] = np.sum(np.abs(series - stats_dict["mean"])) / disp_size # DM = (sum(|xi - media|)) / qtd_amostras
    stats_dict["variance"] = np.var(series) # VAR = (sum(xi - media)^2) / qtd_amostras
    stats_dict["standard deviation"] = np.std(series)
    
    # TESTES
    print(series)
    print()
    print(stats_dict)

def associate():
    series1 = np.random.randint(1, 1000, 200)
    series2 = np.random.randint(1, 1000, 200)
    # INCOMPLETO