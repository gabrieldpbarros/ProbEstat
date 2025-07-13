import os
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from typing import Dict
from adjustText import adjust_text

""" FUNÇÃO QUE FILTRA OS NaNs E RETORNA UM DICIONÁRIO FILTRADO """
def filterNaNs(data: Dict[str, pd.Series], title: str) -> Dict[str, pd.Series]:
    data_nan = {}
    for k in data.keys():
        if data[k].size == 0:
            print(f"A coluna {k} da série {title} não possui dados numéricos. Cancelando plotagem.")
            return {}
        
        items = data[k]
        data_nan[k] = items[~np.isnan(data[k])]

    # Verifica se ainda há dados após remover NaNs
    for k in data.keys():
        if data[k].size == 0:
            print(f"A coluna {k} da série {title} não possui dados numéricos após remover valores ausentes. Cancelando plotagem.")
            return {}
    
    return data_nan

""" FUNÇÃO QUE MONTA BOXPLOTS PARA OS DADOS OBSERVADOS """
def bp(data: Dict[str, pd.Series], title: str, xlabel: str, ylabel: str) -> None:
    # Preparação para plotagem.
    # Transforma todas as séries em ndarray e armazena em outro dicionário de ndarrays
    data_ndarray_dict = {}
    for key in data.keys():
        data_ndarray_dict[key] = data[key].to_numpy()

    plt.close("all")
    plt.figure(figsize=(14, 7))
    plt.boxplot([value for value in data_ndarray_dict.values()], tick_labels=[key for key in data.keys()])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

""" FUNÇÃO QUE MONTA UM GRÁFICO DE DISPERSÃO ESTÁTICO PARA DUAS SÉRIES OBSERVADAS """
def scatStatic(data1: Dict[str, np.ndarray], data2: Dict[str, np.ndarray], title: str, xlabel: str, ylabel: str) -> None:
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
    fig, ax = plt.subplots(figsize=(14, 8))

    ax.scatter(df[xlabel], df[ylabel])

    # Cria uma lista de objetos de texto para cada ponto
    texts = []
    for index, row in df.iterrows():
        label_text = f"{row['UF']}-{str(row['Ano'])[-2:]}"
        texts.append(ax.text(row[xlabel], row[ylabel], label_text, size='small'))

    # A função adjust_text irá reposicionar os textos para evitar sobreposição
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))

    # Adiciona a linha de tendência separadamente
    sns.regplot(data=df, x=xlabel, y=ylabel, scatter=False, ax=ax, line_kws={"color": "darkred", "linewidth": 2})

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()

""" FUNÇÃO QUE MONTA UM GRÁFICO DE DISPERSÃO INTERATIVO PARA DUAS SÉRIES OBSERVADAS """
def scatInteractive(data1: Dict[str, pd.Series], data2: Dict[str, pd.Series], title: str, xlabel: str, ylabel: str) -> None:
    """
    Cria um gráfico de dispersão interativo com Plotly Express.
    As informações aparecem ao passar o mouse sobre os pontos.
    """
    aux = []
    # Converte os dicionários em um DataFrame (mesma lógica da sua função 'scat')
    for uf in data1.keys():
        for ano in data1[uf].index:
            registro = {
                'UF': uf,
                'Ano': ano,
                xlabel: data1[uf].loc[ano],
                ylabel: data2[uf].loc[ano]
            }
            aux.append(registro)
    
    df = pd.DataFrame(aux)

    # Cria o gráfico de dispersão interativo
    fig = px.scatter(
        df,
        x=xlabel,
        y=ylabel,
        title=title,
        trendline="ols",  # Adiciona a linha de tendência (regressão)
        hover_data=['UF', 'Ano']
    )

    # Salva o gráfico em um arquivo HTML no caminho especificado
    output_dir = "graphics"
    output_filename = os.path.join(output_dir, 'grafico_interativo.html')
    fig.write_html(output_filename)
    print(f"Gráfico interativo salvo como '{output_filename}'. Abra este arquivo em seu navegador.")
    
    # Mostra o gráfico no navegador
    fig.show()

# def scat(data1: Dict[str, np.ndarray], data2: Dict[str, np.ndarray], title: str, xlabel: str, ylabel: str) -> None:
#     aux = []
#     # Converte o dicionário em um dataframe
#     for uf in data1.keys():
#     # Itera sobre os anos (o índice da Series)
#         for ano in data1[uf].index:
#             registro = {
#                 'UF': uf,
#                 'Ano': ano,
#                 xlabel: data1[uf].loc[ano],
#                 ylabel: data2[uf].loc[ano]
#             }
#             aux.append(registro)
#     df = pd.DataFrame(aux)
# 
#     plt.close("all")
#     plt.figure(figsize=(14, 8))
# 
#     # Desenha o gráfico de dispersão e a linha de regressão
#     plot = sns.regplot(data=df, x=xlabel, y=ylabel, line_kws={"color": "darkred", "linewidth": 2})
# 
#     # Itera sobre cada linha do DataFrame para adicionar o texto
#     for index, row in df.iterrows():
#         # Formata o texto do rótulo, por exemplo: "SP-22"
#         label_text = f"{row['UF']}-{str(row['Ano'])[-2:]}"
#         
#         # Adiciona o texto no gráfico na posição (x, y) do ponto, com um pequeno deslocamento
#         plot.text(row[xlabel], row[ylabel], label_text, 
#                   size='small', # Tamanho da fonte
#                   color='black', # Cor da fonte
#                   ha='left', # Alinhamento horizontal
#                   va='bottom') # Alinhamento vertical
# 
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.show()

""" FUNÇÃO GERAL QUE DETERMINA QUAL O TIPO DE GRÁFICO SERÁ MONTADO """
def createGraphic(data1: Dict[str, pd.Series], data2: Dict[str, pd.Series], graph_type: str, g_title:str, g_xlabel: str, g_ylabel: str) -> None:
    # Lista que contém todos os tipos de gráficos disponíveis.
    av_graphs = [
                    "boxplot",
                    "scatter",
                    "scatter_interactive"
                ]
    
    data1_nan = filterNaNs(data1, g_xlabel)
    data2_nan = filterNaNs(data2, g_ylabel)
    
    # Verifica qual o tipo de gráfico a ser montado
    if (not any(graph_type != graphs for graphs in av_graphs)):
        print("Tipo de gráfico inválido. Gráficos disponíveis:", end=" ")
        for graphic in av_graphs:
            print(graphic, end=" ")

        return
    else:
        if(graph_type == av_graphs[0]):
            bp(data1_nan, g_title, g_xlabel, g_ylabel)
        elif(graph_type == av_graphs[1]):
            scatStatic(data1_nan, data2_nan, g_title, g_xlabel, g_ylabel)
        elif(graph_type == av_graphs[2]):
            scatInteractive(data1_nan, data2_nan, g_title, g_xlabel, g_ylabel)