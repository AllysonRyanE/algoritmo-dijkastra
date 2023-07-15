# Algoritmo De Dijkastra
Tratando-se de aspectos de urbanização foi explorado uma estrutura de dados em grafo advinda de uma base da dados com todas as conexões intermunicipais nacionais. Filtrando para tratar de uma exemplificação o escopo focou-se em São Paulo com 645 municípios e 4848 conexões. 
Assim, foi implementado, após o tratamento de dados com a biblioteca Pandas, um algoritmo que busca o caminho mais barato (com uso de transporte público) e mais curto entre as duas cidades informadas pelo usuário.

Foi utilizado o algoritmo de Dijkastra, a qual é muito eficiente, tal trata-se de uma realização da busca do caminho mais curto entre dois vértices em um grafo ponderado e direcionado, realizando esse processo atribuindo um peso para cada aresta, ele mantémuma estrutura que comporta nós visualizados e outra com o oposto, por fim através de heap ele trata de atualizar as distâncias frequentemente.
