from prefect import Flow, Parameter

from tasks import SCRIPT_ETL

with Flow('Ocorrencias') as flow:
    SCRIPT_ETL()



from prefect import Flow
from tasks import SCRIPT_ETL

schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    interval=timedelta(minutes=1),
)

with Flow('Ocorrencias', schedule=schedule) as flow_f:
    SCRIPT_ETL()

