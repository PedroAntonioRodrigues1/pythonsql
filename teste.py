import pandas as pd

url = ('https://ifbaiano.edu.br/portal/'
       'wp-content/uploads/2021/08/'
       'Copia-de-Contratos.csv')

empresa_df = pd.read_csv(url, encoding='ISO-8859-1', sep=';')

print(empresa_df['VIGÊNCIA TÉRMINO'].unique())
