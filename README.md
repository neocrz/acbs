# Criminalidade Baixada Satista
O intuito desse projeto é analisar os índices de criminalidade da baixada santista em 5 anos consecutivos utilizando python e aplicando conceitos de ciência de dados.

## Fonte dos dados
Foram utilizados os Dados Estatísticos do Estado de São Paulo do [site oficial](https://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx) da Secretaria de Segurança Pública do estado de São Paulo.


## Metodologia

### Tecnologias
A análise utilizará tecnologias como a linguagem de programação Python e sua biblioteca Pandas para organização dos dados e SQLAlchemy para criação de um banco de dados.

Os dashboards serão feitos por meio do [Metabase](https://www.metabase.com/).

O Ambiente de Desenvolvimento com as tecnologias apontadas, foi estruturado a partir do package manager [Nix](https://nixos.org/) e seu recurso experimental [Flake](https://nixos.wiki/wiki/Flakes)

Para a organização de procedimentos, optou-se pela criação de um pacote python para estruturação de código.

### Obtenção dos dados
Os foram obtidos manualmente através do [site oficial](https://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx) e dispostos com um padrão de nomemclatura na pasta `src` do projeto.

#### Padrão de nomenclatura dos dados
Os dados foram renomeados em um padrão para fácil tratamento no processo de download dos dados.
A nomemclatura segue o padrão `tipo-nome_cidade-ano`, onde:
- `tipo` é o tipo de dados presente no arquivo .csv representado por dois caracteres
    - `pp` para produtividade policial
    - `tx` para taxa de delito
    - `or` para ocorrências registradas

