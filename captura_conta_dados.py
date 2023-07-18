from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator, BranchPythonOperator
import pandas as pd
import requests
import json
import pendulum

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 18),
    'email': ['xxxxxxx@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'schedule_interval': '*/15 * * * *' 
}

def captura_conta_dados():
    url = "https://data.ny.gov/resource/kwxv-fwze.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

def validando_dados(ti):
    qtd = ti.xcom_pull(task_ids='captura_conta_dados')
    if qtd > 100:
        return 'valido'
    return 'nvalido'

def gerar_arquivo_csv():
    url = "https://data.ny.gov/resource/kwxv-fwze.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    df.to_csv('/home/dataset/dados.csv', index=False)

with DAG('airflow_captura_dados', start_date=datetime(2023, 7, 17), schedule_interval='30 * * * *', catchup=False) as dag:

    captura_conta_dados = PythonOperator(
        task_id='captura_conta_dados',
        python_callable=captura_conta_dados
    )

    validando_dados = BranchPythonOperator(
        task_id='validando_dados',
        python_callable=validando_dados
    )

    valido = PythonOperator(
        task_id='valido',
        python_callable=lambda: print('Quantidade OK')
    )

    nvalido = PythonOperator(
        task_id='nvalido',
        python_callable=lambda: print('Quantidade não está OK')
    )

    gerar_csv = PythonOperator(
        task_id='gerar_csv',
        python_callable=gerar_arquivo_csv
    )

    captura_conta_dados >> validando_dados >> [valido, nvalido]
    valido >> gerar_csv