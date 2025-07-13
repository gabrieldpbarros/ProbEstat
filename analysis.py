import numpy as np
import pandas as pd
import stats as sts
import create_graphics as cg
from read_data import readData, prepareData

def formatTitle(var1: str):
    title_source = var1.split("_")
    title_formated = ''

    for i in title_source:
        title_formated += i + ' '

    return title_formated

def main():
    archive_name = input("Insira o nome do arquivo a ser lido: ")
    df = readData(archive_name)
    # DataFrame inválido
    if (df.empty):
        return

    # Verifica o tipo de análise que será feita
    analysis = input("Qual análise você deseja fazer? (grafico, correlacao) ")
    while (analysis != "grafico" and analysis != "correlacao"):
        analysis = input("Texto inválido. Digite uma das opções: [grafico, correlacao] ")

    # Extrai os título dos dados que serão analisados
    temp = input("Insira os títulos dos dados a serem analisados, separados por espaços: ")
    title1, title2 = temp.split()
    # Verifica se as séries temporais existem na tabela
    if not title1 or not title2:
        print("\nErro: Uma das colunas de séries temporais não foi encontrada. Verifique o formato dos nomes das colunas de dados temporais.")
        return
    #uf = input("Insira a UF (sigla): ")

    # Cria uma lista com os títulos de cada coluna do DataFrame
    all_columns = df.columns.tolist()

    if (analysis == "grafico"):
        # Prepara os dados no formato desejado para serem analisados
        series1 = prepareData(df, "UF", title1)
        series2 = prepareData(df, "UF", title2)       

        title = f"Comparação da {formatTitle(title1)}x {formatTitle(title2)}por UF"
        #uf_1 = input("Insira a UF (sigla): ")
        cg.createGraphic(series1, series2, "scatter", title, "Novos micro-empreendimentos", "Contribuição no PIB")
    
    elif (analysis == "correlacao"):
        # Cria duas pd.Series contendo as séries temporais completas
        series1 = df[title1]
        series2 = df[title2]

        # Faz a correlação, retornando as estatísticas descritivas de cada série e a própria correlação
        cor = sts.associate(series1, series2, title1, title2)
        print(f"Coeficiente de correlação entre {title1} e {title2}: ~ {cor:.3f}")
        if cor > 0:
            print(" Correlação positiva (as variáveis aumentam juntas)")
        elif cor < 0:
            print(" Correlação negativa (uma variável aumenta enquanto a outra diminui)")
        else:
            print(" Sem correlação linear")
    
if __name__ == "__main__":
    main()