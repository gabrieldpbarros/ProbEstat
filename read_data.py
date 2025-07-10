import numpy as np
import pandas as pd
from typing import Tuple, List, Dict # Auxilar na padronizção dos tipos dos retornos das funções
from create_graphics import bp

""" FUNÇÃO QUE CARREGA OS DADOS E FORMATA EM PANDAS DATAFRAME """
def loadData(archive_name: str) -> pd.DataFrame:
    # Monta o endereço completo do arquivo
    complete_address = "data/" + archive_name

    # Extrai a extensão do arquivo
    ext = archive_name.split(".")[-1]

    # Verifica a extensão do arquivo
    if len(ext) < 2:
        print("Nome de arquivo inválido ou sem extensão.")
        return pd.DataFrame() # Retorna DataFrame vazio para indicar falha
    
    # Inicializa full_data
    full_data = pd.DataFrame()

    try:
        if (ext == "csv"):
            # Para arquivos do IPEADATA, pode ser necessário ajustar:
            # - skiprows: Para pular linhas de metadados no início.
            # - sep: O delimitador pode ser ';', ',' ou '\t' (tab).
            # - encoding: Para lidar com caracteres especiais.
            # Vamos tentar um cenário comum do IPEADATA, mas você precisará verificar.
            full_data = pd.read_csv(complete_address, sep=',', encoding='latin1')
            # Para o arquivo "ipeadata[02-07-2025-09-51] (1).xls - Séries.csv" do IPEADATA, as 
            # primeiras linhas são metadados. E o delimitador comum é ';'. A codificação 'latin1'
            # ajuda com caracteres especiais. skiprows=1 irá pular a primeira linha que geralmente 
            # tem o nome completo da série. Você pode precisar ajustar skiprows, por exemplo, para
            # 4 ou mais, dependendo de quantas linhas de metadados existem antes dos cabeçalhos reais.
            # Abra o CSV em um editor de texto simples para verificar.
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
def prepareData(data: pd.DataFrame, zone_col: str, value_cols: str) -> Dict[str, pd.Series]:
    """
    SOBRE A SINTAXE:
    
    ARGUMENTOS: 
        data (pd.DataFrame): O DataFrame completo contendo os dados.
        zone_col (str): O título/nome da coluna que identifica os Estados.
        value_cols: (List[str]): O título/nome da coluna com o número de pequenas empresas.

    RETORNO:
        Dict[str, pd.Series]: Um dicionário contendo todas as séries do pandas, associadas
                              à respectiva sigla do Estado que se referem.

    """
    # Verifica se as colunas existem no DataFrame
    if zone_col not in data.columns:
        print(f"Erro: Coluna de zona '{zone_col}' não encontrada no DataFrame. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame(), pd.DataFrame()

    missing_cols = [col for col in value_cols if col not in data.columns]
    if missing_cols:
        print(f"Erro: As seguintes colunas de valor não foram encontradas no DataFrame: {missing_cols}. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame(), pd.DataFrame()
    
    # Inicializa um dicionário de séries temporais contendo apenas os dados desejados
    zone_data = {}

    # Agrupa o DataFrame pela coluna "UF"
    grouped = data.groupby("UF")

    # Itera sobre cada Estado
    for zone, group_df in grouped:
        # Cria a série: o índice é o 'Ano', os valores são de 'Empreendimentos'
        state_series = pd.Series(group_df['Empreendimentos'].values, index=group_df['Ano'])
        state_series = state_series.sort_index() # Garante a ordem cronológica
        zone_data[zone] = state_series

    return zone_data

def readData(series_archive_name = "tests/test-data2.csv") -> Dict[str, np.ndarray]:
    dados_df = loadData(series_archive_name)
    if dados_df.empty:
        print("Não foi possível carregar os dados. Encerrando.")
        return
    
    # Cria uma lista com os títulos de cada coluna do DataFrame
    all_columns = dados_df.columns.tolist()

    # Cria uma lista com os títulos correspondentes aos valores numéricos da série temporal.
    time_series_cols = [col for col in all_columns if 'Empreendimentos' in col]   
    # Filtragem para garantir que apenas valores numéricos vão ser analisados.
    time_series_cols = [col for col in time_series_cols if np.issubdtype(dados_df[col].dtype, np.number)]

    if not time_series_cols:
        print("\nErro: Nenhuma coluna de série temporal foi identificada. Verifique o formato dos nomes das colunas de dados temporais.")
        return

    # Dicionário que armazena todas as séries temporais filtradas pela chave sigla do estado
    dados_dict = prepareData(dados_df, "UF", time_series_cols)
    # Preparação para plotagem posterior.
    # Transforma todas as séries em ndarray e armazena em outro dicionário de ndarrays
    dados_ndarray_dict = {}
    for zone in dados_dict.keys():
        dados_ndarray_dict[zone] = dados_dict[zone].values.flatten()

    bp(dados_ndarray_dict)

    return dados_ndarray_dict

readData()