import numpy as np
import pandas as pd
from typing import Tuple, List, Dict # Auxilar na padronizção dos tipos dos retornos das funções
import create_graphics as cg

""" FUNÇÃO QUE CARREGA OS DADOS E FORMATA EM PANDAS DATAFRAME """
def loadData(archive_name: str) -> pd.DataFrame:
    """ Carrega a tabela e retorna o DataFrame """
    # Monta o endereço completo do arquivo
    complete_address = "data/formated_data/" + archive_name

    # Extrai a extensão do arquivo
    ext = archive_name.split(".")[-1]

    # Verifica a extensão do arquivo
    if (len(ext) < 2):
        print("Nome de arquivo inválido ou sem extensão.")
        return pd.DataFrame() # Retorna DataFrame vazio para indicar falha
    
    # Inicializa full_data
    full_data = pd.DataFrame()

    try:
        if (ext == "csv"):
            full_data = pd.read_csv(complete_address, sep=',', encoding='utf-8-sig')
        elif (ext == "xlsx" or ext == "xls"):
            full_data = pd.read_excel(complete_address)
        else:
            print(f"Extensão '{ext}' não contemplada. Use .csv, .xlsx ou .xls.")
            return full_data
        
        return full_data
    # Casos de erro na leitura
    except FileNotFoundError:
        print(f"Erro: O arquivo '{complete_address}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
        return full_data
    except pd.errors.ParserError as pe:
        print(f"Erro de parser ao ler o arquivo CSV. Verifique o delimitador (sep=';' ou sep=',') e o skiprows.")
        print(f"Detalhes do erro: {pe}")
        return full_data
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo '{archive_name}': {e}")
        return full_data

""" FUNÇÃO QUE PREPARA OS DADOS PARA SEREM TESTADOS """
def prepareData(data: pd.DataFrame, zone_col: str, value_col: str) -> Dict[str, pd.Series]:
    """
    SOBRE A SINTAXE:
    
    ARGUMENTOS: 
        data (pd.DataFrame): O DataFrame completo contendo os dados.
        zone_col (str): O título/nome da coluna que identifica os Estados/Municípios.
        value_col: (List[str]): O título/nome da coluna com os valores que serão analisados.

    RETORNO:
        Dict[str, pd.Series]: Um dicionário contendo todas as séries do pandas, associadas
                              à respectiva sigla do Estado que se referem.

    """
    # Verifica se as colunas existem no DataFrame
    if (zone_col not in data.columns):
        print(f"Erro: Coluna de zona '{zone_col}' não encontrada no DataFrame. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame()

    if (value_col not in data.columns):
        print(f"Erro: A seguinte coluna de valor não foi encontrada no DataFrame: {value_col}. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame()
    
    # Inicializa um dicionário de séries temporais contendo apenas os dados desejados
    zone_data = {}

    # Agrupa o DataFrame pela coluna "UF"
    grouped_by_zone = data.groupby(zone_col)

    # Itera sobre cada Estado/Município
    for zone, group_df in grouped_by_zone:
        # Agrupa novamente por 'Ano' e soma (.sum()) os valores de 'value_col'.
        # Isso garante que cada ano tenha um único valor agregado.
        yearly_series = group_df.groupby('Ano')[value_col].sum()
        
        # Garante que a série está ordenada pelo ano
        yearly_series = yearly_series.sort_index()
        
        # Adiciona a série consolidada ao dicionário
        zone_data[zone] = yearly_series

    return zone_data

def readData(series_archive_name: str) -> pd.DataFrame:
    """ Acessa uma tabela (.csv, .xls ou .xlsx) e converte os dados para um DataFrame """
    dados_df = loadData(series_archive_name)
    if (dados_df.empty):
        print("Não foi possível carregar os dados. Encerrando.")
        return
    
    return dados_df