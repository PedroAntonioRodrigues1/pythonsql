import pandas as pd

url = ('https://ifbaiano.edu.br/portal/'
       'wp-content/uploads/2021/08/'
       'Copia-de-Contratos.csv')

# Pule as linhas de cabeçalho adicionais e leia o arquivo CSV
empresa_df = pd.read_csv(url, encoding='ISO-8859-1', sep=';', skiprows=2)

# Renomeie as colunas para os nomes corretos
empresa_df.columns = ['CNPJ', 'NOME DA EMPRESA', 'TIPO DE CONTRATO', 'VALOR', 'VIGÊNCIA INÍCIO', 'VIGÊNCIA TÉRMINO']

# Converte a coluna 'VIGÊNCIA TÉRMINO' para o formato de data
coluna = 'VIGÊNCIA TÉRMINO'
empresa_df[coluna] = pd.to_datetime(empresa_df[coluna], format='%d/%m/%Y', errors='coerce')

# Filtra as linhas onde 'VIGÊNCIA TÉRMINO' é maior do que 24/04/2021
empresa_df_filtrado = empresa_df[empresa_df[coluna] > '2021-04-24']

# Salva o DataFrame filtrado em um novo arquivo CSV
empresa_df_filtrado.to_csv('empresa_df_filtrado.csv', index=False)
