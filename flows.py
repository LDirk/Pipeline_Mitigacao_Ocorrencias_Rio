from prefect import Flow
from datetime import datetime, timedelta
from tasks import SCRIPT_ETL
from prefect.schedules import IntervalSchedule


schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    end_date = datetime.utcnow() + timedelta(seconds=3601),
    interval=timedelta(minutes=1),
)

with Flow('Ocorrencias', schedule = schedule) as flow:
    SCRIPT_ETL()

with Flow('Ocorrencias', schedule=schedule) as flow_f:
    SCRIPT_ETL()

