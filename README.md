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

Os dados observados foram extraídos de fontes públicas e confiáveis (Observatório DataMPE Brasil, IBGE, Ipea, etc.) e processados através de [scripts de autoria própria](read_data.py). Foram utilizadas técnicas de [análise estatística](stats.py), como [gráficos](create_graphics.py) (gráfico de linhas, boxplot e gráfico de dispersão) e [associação entre variáveis](stats.py). Todas essas técnicas são executadas através de um [script principal](analysis.py).

Através deste trabalho, espera-se contemplar os [Objetivos de Desenvolvimento Sustentável (ODS)](https://brasil.un.org/pt-br/sdgs) 1, 8 e 11 da Organização das Nações Unidas (ONU), contribuindo para a efetivação desses objetivos propostos pela ONU.

## Sobre os dados

Foram considerados para essa análise a [Quantidade de Estabelecimentos por Porte da Empresa - Sebrae, UF e Ano](data/source_data/RAIS_establishment_2025-07-12T06_26_17.595Z.csv), o [Produto Interno Bruto a preços correntes por UF e Ano](data/source_data/IBGE_Year_State_GDP.csv), a [Taxa de desocupação - PNAD contínua por UF e Ano](data/source_data/IBGE_Year_State_GDP.csv), a quantidade de [Estabelecimentos por Porte da Empresa - Sebrae e Mesoregião (especificamente do Vale do Paraíba)](data/source_data/IBGE_Year_Municipality_GDP.csv) e a quantidade de [Empregados por Mesoregião e Ano (especificamente do Vale do Paraíba)](data/source_data/RAIS_workers_2025-07-13T23_41_48.044Z.csv).

### Fontes

 - **Instituto Brasileiro de Geografia e Estatística (IBGE)[^1]**
 - **Instituto de Pesquisa Econômica Aplicada (Ipea)[^2]**
 - **Observatório DataMPE Brasil[^3]**
 - **Receita Federal[^4]**
 - **Relação Anual de Informações Sociais (RAIS)[^5]**

 [^1]: https://www.ibge.gov.br
 [^2]: https://www.ipeadata.gov.br/Default.aspx
 [^3]: https://datampe.sebrae.com.br
 [^4]: https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos
 [^5]: https://www.rais.gov.br/sitio/index.jsf

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

### Taxa de contribuição para o crescimento do Produto Interno Bruto (PIB) e Taxa de crescimento de quantidade de estabelecimentos

O objetivo é verificar se o surgimento de micro-empreendimentos é um fator positivo para o desenvolvimento financeiro da região. Para isso, foi utilizada a contribuição de cada Estado para o PIB nacional, entre 2017 e 2021, como medida de desenvolvimento econômico.

**Exemplo - Contribuição para o crescimento do PIB em R$ (dados parciais):**

|State   |2017        |2018        |2019        |2020        |2021        | 
|:-------|:-----------|:-----------|:-----------|:-----------|:-----------|
|Rondônia|43516144000 |44913978000 |47091334000 |51598745000 |58170098000 |
|Acre    |14272939000 |15331124000 |15630018000 |16476370000 |21374442000 |
|Amazonas|93240190000 |100109232000|108181093000|116019141000|131531039000|
|Roraima |12104706000 |13369988000 |14292227000 |16024274000 |18202580000 |
|Pará    |155232405000|161349601000|178376983000|215935606000|262904976000|
|Amapá   |15481909000 |16795207000 |17496662000 |18469113000 |20099850000 |

Através do gráfico de dispersão dessa relação (gráfico 1), foi encontrado um **coeficiente de correlação positivo** ($\approx$ 0,195) entre as duas séries, indicando que as séries possuem certo grau de associação diretamente proporcional, ou seja, o aumento de uma das variáveis acarreta no aumento da outra variável simultaneamente.

![grafico1](graphics/Comparação%20da%20Taxa%20Crescimento%20PIB%20x%20Taxa%20Crescimento%20Estabelecimentos%20por%20UF.png)
(gráfico 1)

### Taxa de Pobreza e Taxa de crescimento de quantidade de estabelecimentos

Ao contrário da análise anterior, espera-se encontrar uma associação negativa entre as duas séries, observando que o surgimento de micro-empreendimentos influencia na redução da taxa de pobreza na região. Para isso, utilizou-se a taxa de desocupação de cada Estado, entre 2018 e 2025, como medida de taxa de pobreza.

**Exemplo - Taxa de desocupação - PNAD Contínua (dados parciais):**

| Estado   | 2018 T1 | 2018 T2 | 2018 T3 | 2018 T4 | 2019 T1 | 2019 T2 | 2019 T3 | 2019 T4 | ... | 2024 T1 | 2024 T2 | 2024 T3 | 2024 T4 | 2025 T1 |
|:---------|:--------|:--------|:--------|:--------|:--------|:--------|:--------|:--------|:---:|:--------|:--------|:--------|:--------|:--------|
| Acre     | 14.6    | 13.7    | 13.3    | 13.3    | 18.3    | 13.8    | 13.2    | 13.9    | ... |8.9      | 7.2     | 7.4     | 7.3     | 8.2     |
| Alagoas  | 18      | 17.7    | 17.3    | 16.2    | 16.2    | 14.9    | 15.6    | 13.8    | ... |9.9      | 8.1     | 7.7     | 8.1     | 8.9     |
| Amazonas | 14      | 14.3    | 13.2    | 14.6    | 16      | 14      | 13.5    | 13.1    | ... |9.8      | 7.9     | 8.1     | 8.3     | 10.1    |
| Amapá    | 21.7    | 21.6    | 18.4    | 19.8    | 20.3    | 17.1    | 16.9    | 15.8    | ... |14.2     | 10.9    | 9       | 8.7     | 8.7     |
| Bahia    | 18.1    | 16.8    | 16.4    | 17.6    | 18.5    | 17.5    | 16.9    | 16.5    | ... |14       | 11.1    | 9.7     | 9.9     | 10.9    |
| Ceará    | 12.9    | 11.8    | 10.7    | 10.2    | 11.5    | 11      | 11.4    | 10.3    | ... |8.6      | 7.5     | 6.7     | 6.5     | 8       |

> [!NOTE]
> Como os dados estão separados por trimestres, foi calculada a média entre os quatro valores para ser utilizada como variável relativa ao respectivo ano.
 
Pelo gráfico de dispersão dessa associação (gráfico 2), verificamos um **coeficiente de correlação negativo** ($\approx$ -0,242) entre as duas séries. Isso indica que existe certo grau de relação inversamente proporcional entre as variáveis, ou seja, o aumento de uma delas causa a diminuição da outra simultaneamente.

![grafico2](graphics/Comparação%20da%20Taxa%20Pobreza%20x%20Taxa%20Crescimento%20Estabelecimentos%20por%20UF.png)
(gráfico 2)

### Quantidade total de empregados e a Quantidade total de estabelecimentos

Esta análise busca, em menor escopo, verificar a relação de empregados por quantidade total de micro-empresas. Como citado anteriormente, esta seção reduz o escopo do estudo, voltando a avaliação para os dez maiores municípios do Vale do Paraíba, entre 2018 e 2021.

**Exemplo - Total de micro-empresas x Total de empregados (Maiores cidades do Vale, 2021):**

| Município           | Total de Estabelecimentos | Total de Empregos |
|:--------------------|:--------------------------|:------------------|
| São José dos Campos | 32892                     | 277175            |
| Jacareí             | 10498                     | 59982             |
| Taubaté             | 15761                     | 102871            |
| Pindamonhangaba     | 6127                      | 36681             |
| Caraguatatuba       | 6463                      | 30264             |
| Ubatuba             | 4551                      | 15807             |
| São Sebastião       | 3653                      | 16098             |
| Guaratinguetá       | 6475                      | 37161             |

Observando o gráfico de dispersão dessa análise (gráfico 3), verificamos um **coeficiente de correlação positivo** ($\approx$ 0,962) entre as duas variáveis muito alto. Podemos concluir, assim, uma relação muito forte entre a quantidade de micro-empresas e a quantidade de empregados, ressaltando a importância que esses estabelecimentos têm para a geração de empregos em um município.

![grafico3](graphics/Comparação%20do%20Total%20Estabelecimentos%20x%20Total%20Empregos%20por%20Município%20(Maiores%20do%20Vale%20do%20Paraíba).png)
(gráfico 3)

## Discussão

Pelas duas primeiras análises, podemos afirmar que encontramos resultados conforme o esperado, ou seja, uma relação diretamente proporcional entre o surgimento de micro-empreendimentos e o desenvolvimento econômico e uma relação inversamente proporcional entre a taxa de pobreza e o crescimento de micro-empreendimentos. Contudo, ambos os coeficientes encontrados estão muito próximos de 0, indicando uma relação insignificante entre os dados.

Portanto, devemos verificar, através do p-valor, se os resultados são, de fato, estatisticamente significantivos para concluir uma possível relação entre nossas séries. Para isso, realizamos um teste de hipótese (**[t de Student](#teste-t-de-student)**), em que consideramos a hipótese nula (H<sub>0</sub>) como a ausência de correlação entre os dados e a hipótese alternativa (H<sub>1</sub>) como a existência de correlação entre os dados, encontramos o **[grau de liberdade](#grau-de-liberdade-)** e determinamos o **[p-valor](#p-valor)** para cada correlação encontrada. 

### **Teste t de Student**

Podemos interpretar o teste da seguinte forma:

$$ t = r \times {\sqrt{n - 2 \over 1 - r^2}}  $$

Em que:

- **$r$:** Coeficiente correlacional;

- **$n$:** Tamanho da amostra;

- **$t$:** Valor da estatística do teste.

#### 1. Teste para $r = 0,195$:

$$ t = 0,195 \times {\sqrt{106 - 2 \over 1 - 0,195^2}} \approx 2,0167 $$

#### 2. Teste para $r = −0.242$:

$$ t = −0.242 \times {\sqrt{106 - 2 \over 1 - (−0.242)^2}} \approx −2.5435 $$

### **Grau de liberdade ($df$)**

Precisamos do grau de liberdade para encontrar o valor de $t_c$ na tabela da distribuição t-Sudent, o qual é dado por:

$$ df = n - 2 $$

Como ambas análises têm a mesma quantidade de amostras, temos:

$$ df = 106 - 2 = 104 $$

### **P-valor**

Como desejamos verificar apenas se há correlação entre as variáveis, ou seja, $r \neq 0$, consideramos um teste bilateral. Assim, calculamos o p-valor da seguinte forma:

$$ p = 2 \times \mathrm{P}(t_c < |t|) $$

#### 1. P-valor para $r = 0,195$:

Substituindo os valores:

$$ p = 2 \times \mathrm{P}(t_c < 0,195)\\ \Longleftrightarrow p = 2 \times 0.02316\\ \Longrightarrow p \approx 0.04632$$

#### 2. P-valor para $r = −0.242$:

Temos:

$$ p = 2 \times \mathrm{P}(t_c < 0.242)\\ \Longleftrightarrow p = 2 \times 0.00620\\ \Longrightarrow p \approx 0.01240$$

## Conclusão

## Referências