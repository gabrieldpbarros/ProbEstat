import numpy as np
import pandas as pd
import stats as sts
from read_data import readData, prepareData

def main():
    archive_name = input("Insira o nome do arquivo a ser lido: ")
    df = readData(archive_name)
    # DataFrame inválido
    if (df.empty):
        return

    # Verifica o tipo de análise que será feita
    analysis = input("Qual análise você deseja fazer? (correlacao, estatistica descritiva) ")
    while (analysis != "correlacao" and analysis != "estatistica descritiva"):
        analysis = input("Texto inválido. Digite uma das opções: [correlacao, estatistica descritiva]")

    # Cria uma lista com os títulos de cada coluna do DataFrame
    all_columns = df.columns.tolist()

    if (analysis == "correlacao"):
        temp = input("Insira os títulos dos dados a serem analisados, separados por espaços: ")
        title1, title2 = temp.split()
      
        # Filtragem para garantir que apenas valores numéricos vão ser analisados.
        time_series1_col = [title1]
        time_series1_col = [col for col in time_series1_col if np.issubdtype(df[col].dtype, np.number)]

        time_series2_col = [title2]
        time_series2_col = [col for col in time_series1_col if np.issubdtype(df[col].dtype, np.number)]

        if not time_series1_col or not time_series2_col:
            print("\nErro: Uma das colunas de séries temporais não foi encontrada. Verifique o formato dos nomes das colunas de dados temporais.")
            return
        # CONTINUA    
    
    else:
        # Estabelece qual a variável que será analisada
        var_series = input("Insira o título da série a ser analisada: ")

        # Cria um dicionário com a série temporal associada ao título definido
        time_series_complete = prepareData(df, "UF", var_series)
        if (not time_series_complete.values()):
            return

        uf = input("Insira a UF (sigla): ")
        series = np.array([value for key, value in time_series_complete.items() if key == uf])
        var_stats = sts.getStats(series)
    
if __name__ == "__main__":
    main()