from prefect import Flow
from datetime import datetime, timedelta
from tasks import SCRIPT_ETL
from prefect.schedules import IntervalSchedule


schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    end_date = datetime.utcnow() + timedelta(seconds=3650),
    interval=timedelta(minutes=20),
)

with Flow('Ocorrencias', schedule = schedule) as flow:
    SCRIPT_ETL()


