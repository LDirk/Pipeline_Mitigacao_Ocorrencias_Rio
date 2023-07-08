import pandas as pd

df_verificar = pd.read_csv('dados_ocorrencias2.csv', encoding='latin1')

pd.set_option('display.max_columns', None)

print(df_verificar)