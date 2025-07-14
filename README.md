# Trabalho final de Probabilidade e Estatística - 2025.1: Análise do desempenho econômico de diferentes regiões/estados brasileiros com base no surgimento de pequenas empresas.

Discentes: Daniel Ribeiro, Gabriel Delgado, João Vitor Gomes, Sarah Mynssen, Vinícius Dantas

## Conteúdo

- [Resumo](#resumo)
- [Dados](#sobre-os-dados)
- [Algoritmos](#algoritmos)
- [Análise](#análise)
- [Discussão](#discussão)
- [Conclusão](#conclusão)

## Resumo

O trabalho tem como foco analisar como o surgimento de pequenas empresas, ou microempreendimentos, afeta no desempenho econômico do estado em que esses empreendimentos se originam.

Os dados observados foram extraídos de fontes públicas e confiáveis ([Observatório DataMPE Brasil](https://datampe.sebrae.com.br), [IBGE](https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html), [Ipea](https://www.ipea.gov.br/portal/index.php?option=com_content&view=article&id=1825), etc.) e processados através de [scripts de autoria própria](read_data.py). Foram utilizadas técnicas de [análise estatística](stats.py), como [gráficos](create_graphics.py) (gráfico de linhas, boxplot e gráfico de dispersão) e [associação entre variáveis](stats.py). Todas essas técnicas são executadas através de um [script principal](analysis.py).

Através deste trabalho, espera-se contemplar os [Objetivos de Desenvolvimento Sustentável (ODS)](https://brasil.un.org/pt-br/sdgs) 1, 8 e 11 da Organização das Nações Unidas (ONU), contribuindo para a efetivação desses objetivos propostos pela ONU.

## Sobre os dados

Foram considerados para essa análise a [Quantidade de Estabelecimentos por Porte da Empresa - Sebrae, UF e Ano](data/source_data/RAIS_establishment_2025-07-12T06_26_17.595Z.csv), o [Produto Interno Bruto a preços correntes por UF e Ano](data/source_data/IBGE_Year_State_GDP.csv), a [Taxa de desocupação - PNAD contínua por UF e Ano](data/source_data/IBGE_Year_State_GDP.csv), a quantidade de [Estabelecimentos por Porte da Empresa - Sebrae e Mesoregião (especificamente do Vale do Paraíba)](data/source_data/IBGE_Year_Municipality_GDP.csv) e a quantidade de [Empregados por Mesoregião e Ano (especificamente do Vale do Paraíba)](data/source_data/RAIS_workers_2025-07-13T23_41_48.044Z.csv).

### Fontes

 - **[Instituto Brasileiro de Geografia e Estatística (IBGE)](https://www.ibge.gov.br)**
 - **[Instituto de Pesquisa Econômica Aplicada (Ipea)](https://www.ipeadata.gov.br/Default.aspx)**
 - **[Observatório DataMPE Brasil](https://datampe.sebrae.com.br)**
 - **[Receita Federal](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos)**
 - **[Relação Anual de Informações Sociais (RAIS)](https://datampe.sebrae.com.br/data-explorer?cube=RAIS_establishment&drilldowns%5B0%5D=Establishment+Size&drilldowns%5B1%5D=Geography.Municipality.State&drilldowns%5B2%5D=Year&drilldowns%5B3%5D=Type+Establishment&measures%5B0%5D=Establishments)**

### Séries

As séries utilizadas estão contidas na pasta [source_data](data/source_data/), com algumas alterações de formatação em relação à fonte original. Essa escolha foi feita para facilitar a manipulação das séries pelas funções dos códigos.

### Informações relevantes

Para a conveniência do script, os dados extraídos foram filtrados e formatados através de inteligência artificial, mas avaliados após essa etapa a fim de garantir a acurácia da análise. Todos esses dados estão localizados na pasta [formated_data](data/formated_data/).

A Taxa de Pobreza foi valorizada para a associação com a ODS 1 e a Contribuição no PIB foi utilizada para a relação com a ODS 8. 

## Algoritmos

### Visão geral

O arquivo principal ([analysis.py](analysis.py)) solicita o nome da tabela que será analisada, armazenada na pasta de dados formatados, faz a leitura da tabela ([read_data.py](read_data.py)), convertendo os dados em um DataFrame da biblioteca pandas, e oferece os tipos de análise que podem ser feitas. O usuário segue as instruções dadas durante a execução, fornecendo os títulos das séries analisadas, a UF estudada, por exemplo.

De acordo com o tipo de análise solicitada pelo usuário, o arquivo chama outras funções auxiliares ([criação de gráficos](create_graphics.py), [processamento dos dados](read_data.py) e [dados estatísticos](stats.py)) e retorna a análise solicitada pelo usuário.

### Resumo dos algoritmos

- **[analysis](analysis.py):** função principal, responsável por executar todos os outros algoritmos.

- **[create_graphics](create_graphics.py):** recebe séries temporais, formatadas como um dicionário, e gera um gráfico (dispersão ou boxplot), conforme as instruções dadas pelo usuário na função principal.

- **[read_data](read_data.py):** responsável por tudo que envolve leitura e processamento das tabelas analisadas, como acessar a tabela armazeanada, converter em um pandas DataFrame e retornar uma série temporal específica.

- **[stats](stats.py):** possui duas funções, a primeira retorna as medidas de posição e de dispersão de uma série temporal, e a segunda faz a análise associativa de duas séries temporais, utilizando o coeficiente de correlação.

## Análise

As principais análises neste trabalho envolvem as comparações entre a [Taxa de crescimento de quantidade de estabelecimentos e a Taxa de contribuição para o crescimento do Produto Interno Bruto (PIB)](#taxa-de-crescimento-de-quantidade-de-estabelecimentos-e-a-taxa-de-contribuição-para-o-crescimento-do-produto-interno-bruto-pib) e entre a [Taxa de crescimento de quantidade de estabelecimentos e a Taxa de Pobreza](#taxa-de-crescimento-de-quantidade-de-estabelecimentos-e-taxa-de-pobreza), ambas análies por UF e Ano; e entre a [Quantidade total de empregados e a Quantidade total de estabelecimentos](#quantidade-total-de-empregados-e-a-quantidade-total-de-estabelecimentos), analisada por Município, voltada para o Vale do Paraíba.

### Taxa de crescimento de quantidade de estabelecimentos e Taxa de contribuição para o crescimento do Produto Interno Bruto (PIB)

O objetivo é verificar se o surgimento de micro-empreendimentos é um fator positivo para o desenvolvimento financeiro da região. Para isso, foi utilizada a contribuição de cada Estado para o PIB nacional, entre 2017 e 2021, como medida de desenvolvimento econômico.

**Exemplo (dados parciais):**

|State   |2017        |2018        |2019        |2020        |2021        | 
|:-------|:-----------|:-----------|:-----------|:-----------|:-----------|
|Rondônia|43516144000 |44913978000 |47091334000 |51598745000 |58170098000 |
|Acre    |14272939000 |15331124000 |15630018000 |16476370000 |21374442000 |
|Amazonas|93240190000 |100109232000|108181093000|116019141000|131531039000|
|Roraima |12104706000 |13369988000 |14292227000 |16024274000 |18202580000 |
|Pará    |155232405000|161349601000|178376983000|215935606000|262904976000|
|Amapá   |15481909000 |16795207000 |17496662000 |18469113000 |20099850000 |



### Taxa de crescimento de quantidade de estabelecimentos e Taxa de Pobreza

### Quantidade total de empregados e a Quantidade total de estabelecimentos

## Discussão

## Conclusão