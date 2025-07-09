import numpy as np
import scipy.stats as st
import pandas as pd
from typing import Tuple, List # Auxilar na padronizacao dos tipos dos retornos das funcoes
from boxplot import bp

""" FUNCAO QUE CARREGA OS DADOS E FORMATA EM PANDAS DATAFRAME """
def loadData(archive_name: str) -> pd.DataFrame:
    # Monta o endereco completo do arquivo
    complete_address = "dados/" + archive_name

    # Extrai a extensao do arquivo
    ext = archive_name.split(".")[-1]

    # Verifica a extensao do arquivo
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
            full_data = pd.read_csv(complete_address, sep=',', encoding='latin1', thousands='.')
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

""" FUNCAO QUE PREPARA OS DADOS PARA SEREM TESTADOS """
def prepareData(data: pd.DataFrame, zone_col: str, value_cols: List[str], zone1: str, zone2: str) -> Tuple[pd.Series, pd.Series]:
    """
    SOBRE A SINTAXE:
    
    ARGUMENTOS: 
        data (pd.DataFrame): O DataFrame completo contendo os dados.
        zone_col (str): O título/nome da coluna que identifica as regiões/estados.
        value_cols: (List[str]): O título/nome da coluna com o número de pequenas empresas.
        zone1 (str): O nome da primeira região/estado a ser comparada.
        zone2 (str): O nome da segunda região/estado a ser comparada.

    RETORNO:
        Tuple[pd.Series, pd.Series]: Uma tupla contendo duas Series do pandas,
                                     uma para cada região com os dados de empresas.

    """

    # Verifica se as colunas existem no DataFrame
    if zone_col not in data.columns:
        print(f"Erro: Coluna de zona '{zone_col}' não encontrada no DataFrame. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame(), pd.DataFrame()

    missing_cols = [col for col in value_cols if col not in data.columns]
    if missing_cols:
        print(f"Erro: As seguintes colunas de valor não foram encontradas no DataFrame: {missing_cols}. Colunas disponíveis: {data.columns.tolist()}")
        return pd.DataFrame(), pd.DataFrame()

    zone1_data = data[data[zone_col] == zone1][value_cols]
    zone2_data = data[data[zone_col] == zone2][value_cols]

    return zone1_data, zone2_data

nome_arq_series = "ipeadata[02-07-2025-09-51] (1).xlsx - Séries.csv"
def main():
    dados_df = loadData(nome_arq_series)
    if dados_df.empty:
        print("Não foi possível carregar os dados. Encerrando.")
        return

    all_columns = dados_df.columns.tolist()

    time_series_cols = [col for col in all_columns if ' T' in col and col.split(' T')[0].isdigit()]   
    time_series_cols = [
        col for col in time_series_cols
        if np.issubdtype(dados_df[col].dtype, np.number) and col != 'Codigo'
    ]

    try:
        time_series_cols.sort(key=lambda x: (int(x.split(' T')[0]), int(x.split(' T')[1].replace('T', ''))))
    except (ValueError, IndexError) as e:
        print(f"Aviso: Não foi possível ordenar todas as colunas de série temporal. Pode haver um formato inesperado nos nomes das colunas. Erro: {e}")
        time_series_cols = [col for col in all_columns if np.issubdtype(dados_df[col].dtype, np.number) and col not in ['Codigo', 'Sigla', 'Estado']]
        time_series_cols.sort()

    if not time_series_cols:
        print("\nErro: Nenhuma coluna de série temporal foi identificada. Verifique o formato dos nomes das colunas de dados temporais.")
        print("Esperado formato como 'YYYY TQ', por exemplo '2015 T1'.")
        return

    dados1, dados2 = prepareData(dados_df, "Estado", time_series_cols, "SÃ£o Paulo", "Minas Gerais")

    dados1_bp = dados1.values.flatten()
    dados2_bp = dados2.values.flatten()
    bp(dados1_bp, dados2_bp, "São Paulo", "Minas Gerais")

    # EXEMPLO DE TESTE T COM OS DADOS ACHATADOS (bagulho q o Gemini criou)
    if dados1_bp.size > 1 and dados2_bp.size > 1: # Precisa de pelo menos 2 pontos para t-test
        estatistica_t, valor_p = st.ttest_ind(dados1_bp, dados2_bp, equal_var=False, nan_policy='omit')
        print(f"\nResultado do Teste T de Independência:")
        print(f"Estatística T: {estatistica_t}")
        print(f"Valor P: {valor_p}")
        if valor_p < 0.05: # Considerando um nível de significância de 5%
            print("Há uma diferença estatisticamente significativa no número de pequenas empresas entre os dois estados.")
        else:
            print("Não há evidências estatisticamente significativas de uma diferença no número de pequenas empresas entre os dois estados.")
    else:
        print("\nNão há dados suficientes para realizar o Teste T (cada grupo precisa de mais de um ponto de dados).")

if __name__ == "__main__":
    main()

# IDEIAS: montar um grafico de boxplot para todos os estados, teste de hipoteses entre 2 ou todos os estados