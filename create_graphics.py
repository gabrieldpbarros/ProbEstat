import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict

""" FUNÇÃO QUE MONTA BOXPLOTS PARA OS DADOS OBSERVADOS """
def bp(data: Dict[str, pd.Series], title: str, xlabel: str, ylabel: str) -> None:
    # Preparação para plotagem.
    # Transforma todas as séries em ndarray e armazena em outro dicionário de ndarrays
    data_ndarray_dict = {}
    for key in data.keys():
        data_ndarray_dict[key] = data[key].values.flatten()

    plt.close("all")
    plt.figure(figsize=(14, 7))
    plt.boxplot([value for value in data_ndarray_dict.values()], tick_labels=[key for key in data.keys()])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

""" FUNÇÃO QUE MONTA UM GRÁFICO DE DISPERSÃO PARA DUAS SÉRIES OBSERVADAS """
def scat(data1: Dict[str, np.ndarray], data2: Dict[str, np.ndarray], title: str, xlabel: str, ylabel: str):
    aux = []
    # Converte o dicionário em um dataframe
    for uf in data1.keys():
    # Itera sobre os anos (o índice da Series)
        for ano in data1[uf].index:
            registro = {
                'UF': uf,
                'Ano': ano,
                xlabel: data1[uf].loc[ano],
                ylabel: data2[uf].loc[ano]
            }
            aux.append(registro)
    
    df = pd.DataFrame(aux)

    plt.close("all")
    plt.figure(figsize=(14, 7))
    sns.regplot(data=df, x=xlabel, y=ylabel, line_kws={"color": "darkred", "linewidth": 2})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

""" FUNÇÃO GERAL QUE DETERMINA QUAL O TIPO DE GRÁFICO SERÁ MONTADO """
def createGraphic(data: Dict[str, np.ndarray], graph_type: str, g_title:str, g_xlabel: str, g_ylabel: str) -> None:
    # Lista que contém todos os tipos de gráficos disponíveis.
    av_graphs = [
                    "boxplot",
                    "scatter"
                ]
    
    # Verificar se ha dados para plotar e filtra NaNs (Not a Number)
    data_nan = {}
    for k in data.keys():
        if data[k].size == 0:
            print(f"A coluna {k} não possui dados numéricos. Cancelando plotagem.")
            return
        
        items = data[k]
        data_nan[k] = items[~np.isnan(data[k])]

    # Verifica se ainda há dados após remover NaNs
    for k in data.keys():
        if data[k].size == 0:
            print(f"A coluna {k} não possui dados numéricos após remover valores ausentes. Cancelando plotagem.")
            return
        
    # Verifica qual o tipo de gráfico a ser montado
    if (not any(graph_type != graphs for graphs in av_graphs)):
        print("Tipo de gráfico inválido. Gráficos disponíveis:", end=" ")
        for graphic in av_graphs:
            print(graphic, end=" ")

        return
    else:
        if(graph_type == av_graphs[0]):
            bp(data_nan, g_title, g_xlabel, g_ylabel)
        elif(graph_type == av_graphs[1]):
            scat(data, g_title, g_xlabel, g_ylabel)