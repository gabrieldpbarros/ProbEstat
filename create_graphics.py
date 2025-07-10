import numpy as np
import matplotlib.pyplot as plt
from typing import Dict

""" FUNCAO QUE MONTA BOXPLOTS PARA OS DADOS OBSERVADOS """
def bp(zone_data: Dict[str, np.ndarray]) -> None:
    # Verificar se ha dados para plotar e filtra NaNs (Not a Number)
    data = {}
    for k in zone_data.keys():
        if zone_data[k].size == 0:
            print(f"A coluna {k} não possui dados numéricos. Cancelando plotagem.")
            return
        
        items = zone_data[k]
        data[k] = items[~np.isnan(zone_data[k])]

    # Verifica se ainda há dados após remover NaNs
    for k in zone_data.keys():
        if zone_data[k].size == 0:
            print(f"A coluna {k} não possui dados numéricos após remover valores ausentes. Cancelando plotagem.")
            return

    plt.close("all")
    plt.figure(figsize=(14, 7))
    plt.boxplot([data for data in zone_data.values()], tick_labels=[zone for zone in zone_data.keys()])
    plt.title("Comparação do Número de Empreendimentos por Região/Estado (2015-2025)")
    plt.ylabel("Número de Empreendimentos")
    plt.show()