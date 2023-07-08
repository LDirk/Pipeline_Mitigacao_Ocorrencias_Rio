from prefect import Flow, Parameter

from tasks import SCRIPT_ETL

with Flow('Ocorrencias') as flow:
    SCRIPT_ETL()

flow.run()