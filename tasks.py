from io import StringIO
import pandas as pd
from prefect import task
import requests
from utils import log
from datetime import datetime, timedelta
import pytz
import os.path
import csv

@task

# Observação: 
# O ETL deveria ser separado em 3 funções: extract, transform e load para facilitar a manutenção do código.
# Porém, como o ETL é pequeno, não julguei necessário. 
# O codigo do ETL está comentado em: 
    #SMTR/Script_ETL_comentato/ScriptETL.py


def SCRIPT_ETL():

    current_datetime = datetime.now(pytz.timezone('America/Sao_Paulo'))

    # ETAPA : CONSUMO DOS DADOS
    url = 'https://api.dados.rio/v2/adm_cor_comando/ocorrencias_abertas'
    base_url = 'https://api.dados.rio/v2/adm_cor_comando/ocorrencias_orgaos_responsaveis/?eventoId='

    try:
        response = requests.get(url)
        data = response.json()
        eventos = data['eventos']
        log('Dados de ocorrencias consumido com sucesso.')

    except requests.exceptions.RequestException as e:
        log(f"Erro ao consumir os dados de ocorrencias: {str(e)}")
        eventos = []

    df_ocorrencias = pd.DataFrame(eventos)
    df_ocorrencias = df_ocorrencias[['titulo', 'status', 'inicio', 'informe_id', 'id', 'pop_id']]

    try:
        df_org = pd.DataFrame()
        for evento_id in df_ocorrencias['id']:
            url = base_url + str(evento_id)
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                eventos = data['atividades']

                for evento in eventos:
                    evento['id'] = evento_id
                df_org = pd.concat([df_org, pd.DataFrame(eventos)])
        log('Dados de ocorrencias por por orgão consumidos com sucesso.')

    except requests.exceptions.RequestException as e:
        log(f"Erro ao consumir os dados de ocorrencias: {str(e)}")
        eventos = []
        print(f"Erro ao consumir os dados de ocorrencias: {str(e)}")

    # Etapa - Tratamento dos dados
    log('Iniciando o tratamento dos dados')

    df_CET_RIO = df_org.loc[(df_org['orgao'] == 'CET-RIO')]
    df_CET_RIO = df_CET_RIO.sort_values(by='inicio', ascending=False)

    df_CET_RIO['data_consulta_api'] = current_datetime.strftime("%Y-%m-%d %H:%M")

    df_CET_RIO.reset_index(drop=True, inplace=True)

    df_final = df_CET_RIO.merge(df_ocorrencias[['id', 'titulo']], on='id', how='left')

    df_final = df_final.loc[:, ['titulo', 'data_consulta_api', 'status', 'id']]

    df_final = df_final.drop_duplicates()

    df_csv = df_final.groupby(['titulo', 'data_consulta_api', 'status']).size().reset_index()

    df_csv.columns = ['Tipo_De_Ocorrencia', 'Data_Consulta_Api', 'Status', 'Quantidade_De_Ocorrencias']

    df_csv = df_csv.sort_values(by=['Tipo_De_Ocorrencia', 'Data_Consulta_Api'], ascending=[True, False])

    log('Dados Tratados com sucesso.')

    # Etapa - load dos dados.

    filename = 'dados/dados_ocorrencias2.csv'

    if not os.path.isfile(filename):
        df_csv.to_csv(filename, index=False)
        log('Dados Salvos em dados/dados_ocorrencias2 com sucesso')
    else:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(df_csv.values)
            log('Dados Salvos em dados/dados_ocorrencias2 com sucesso')

