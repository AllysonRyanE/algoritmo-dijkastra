import pandas as pd
tabela = pd.read_excel("Base_De_Dados.xlsx")
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO']
colunas = ['ID', 'COD_UF_A', 'CODMUNDV_A', 'COD_UF_B', 'CODMUNDV_B', 'VAR01', 'VAR02', 'VAR04', 'VAR05', 'VAR06', 'VAR07', 'VAR08', 'VAR09', 'VAR10', 'VAR11', 'VAR12', 'VAR13', 'VAR14']
def excluir_col(name):
    tabela.drop(name, axis=1, inplace=True)
for z in colunas:
    excluir_col(z)
for x in estados:
    tabela.drop(tabela[tabela['UF_A'] == x].index, inplace=True)
for y in estados:
    tabela.drop(tabela[tabela['UF_B'] == y].index, inplace=True)
tabela.drop('UF_A', axis= 1, inplace=True)
tabela.drop('UF_B', axis= 1, inplace=True)
tabela.to_excel("Base_De_Dados.xlsx", index=False)
tabela.to_csv('InterMunicipal_SP.txt', ',')

with open('InterMunicipal_SP.txt', 'r', encoding= 'utf-8') as arquivo:
    linhas = arquivo.readlines()

with open('InterMunicipal_SP.txt', 'w', encoding= 'utf-8') as arquivo:
    for linha in linhas:
        valores = linha.strip().split(',')
        novo_valor = ','.join(valores[1:])
        arquivo.write(novo_valor + '\n')
