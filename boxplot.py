import numpy as np
import matplotlib.pyplot as plt

""" FUNCAO QUE MONTA BOXPLOTS PARA OS DADOS OBSERVADOS """
def bp(zone1_data: np.ndarray, zone2_data: np.ndarray, zone1: str, zone2: str) -> None:
     # Verificar se ha dados para plotar
    if zone1_data.size == 0 and zone2_data.size == 0:
        print("Não há dados válidos para plotar o boxplot.")
        return
    
    # Filtra NaNs        
    data1 = zone1_data[~np.isnan(zone1_data)] 
    data2 = zone2_data[~np.isnan(zone2_data)]

    # Verifica se ainda há dados após remover NaNs
    if data1.size == 0 and data2.size == 0:
        print("Não há dados numéricos válidos para plotar o boxplot após remover valores ausentes.")
        return

    plt.close("all")
    plt.figure(figsize=(8, 5))
    plt.boxplot([data1, data2], tick_labels=[zone1, zone2])
    plt.title("Comparação do Número de Desempregados por Região/Estado (2015-2025)")
    plt.ylabel("Número de Desempregados")
    plt.show()