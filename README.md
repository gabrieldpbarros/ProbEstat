# Trabalho final de Probabilidade e Estatística - 2025.1: Análise do desempenho econômico de diferentes regiões/estados brasileiros com base no surgimento de pequenas empresas.

Discentes: Daniel Ribeiro, Gabriel Delgado, João Vitor Gomes, Sarah Mynssen, Vinícius Dantas

## Conteúdo

- [Resumo](#resumo)
- [Dados](#sobre-os-dados)
- [Análise](#análise)
- [Discussão](#discussão)
- [Conclusão](#conclusão)

## Resumo

O trabalho tem como foco analisar como o surgimento de pequenas empresas, ou microempreendimentos, afeta no desempenho econômico do estado em que esses empreendimentos se originam.

Os dados observados foram extraídos de fontes públicas e confiáveis ([Observatório DataMPE Brasil](https://datampe.sebrae.com.br), ...) e processados através de [scripts de autoria própria](read_data.py). Foram utilizadas técnicas de [análise estatística](stats.py), como [gráficos](create_graphics.py) (boxplot e gráfico de dispersão) e [associação entre variáveis](stats.py). Todas essas técnicas são executadas através de um [script principal](analysis.py).

Através deste trabalho, espera-se contemplar os [Objetivos de Desenvolvimento Sustentável (ODS)](https://brasil.un.org/pt-br/sdgs) 1, 8 e 11 da Organização das Nações Unidas (ONU), contribuindo para a efetivação desses objetivos propostos pela ONU.

## Sobre os dados

Foram considerados para essa análise a Quantidade de Estabelecimentos por Porte da Empresa - Sebrae, UF e Ano, ...

### Fontes
 - **[Relação Anual de Informações Sociais (RAIS)](https://datampe.sebrae.com.br/data-explorer?cube=RAIS_establishment&drilldowns%5B0%5D=Establishment+Size&drilldowns%5B1%5D=Geography.Municipality.State&drilldowns%5B2%5D=Year&drilldowns%5B3%5D=Type+Establishment&measures%5B0%5D=Establishments)**
 - **fonte 2**
 - **fonte 3**

.

.

.


### Séries

As séries utilizadas estão contidas na pasta [source data](data/source_data/), com algumas alterações de formatação em relação à fonte original. Essa escolha foi feita para facilitar a manipulação das séries pelas funções dos códigos.

### Informações relevantes

Para a conveniência do script, os dados extraídos foram filtrados e formatados através de inteligência artificial, mas avaliados após essa etapa a fim de garantir a acurácia da análise. Todos esses dados estão localizados na pasta [formated_data](data/formated_data/).

A Taxa de Pobreza foi valorizada para a associação com a ODS 1 e a Contribuição no PIB foi utilizada para a relação com a ODS 8. 

## Análise

## Discussão

## Conclusão