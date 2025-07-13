import numpy as np
import pandas as pd
from typing import Dict

""" FUNÇÃO QUE CALCULA AS MEDIDAS DESCRITIVAS DE UMA SÉRIE TEMPORAL """
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
    
    return stats_dict

""" FUNÇÃO QUE CALCULA A CORRELAÇÃO ENTRE DUAS SÉRIES TEMPORAIS """
def associate(series1: pd.Series, series2: pd.Series, title1: str, title2: str) -> float:
    # Estatísticas descritivas
    stats1 = series1.to_numpy()
    stats2 = series2.to_numpy()
    stats1 = getStats(series1)
    stats2 = getStats(series2)

    # Imprime as stats1 e stats2 para visualiazação
    print(f"Estatísticas descritivas de '{title1}':\n{stats1}")
    print(f"Estatísticas descritivas de '{title2}':\n{stats2}")

    # Correlação
    corr = series1.corr(series2)

    return corr