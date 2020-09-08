from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo alguns argumentos básicos
default_args = {
    'owner': 'pcesar_costa',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 7),
    'retries': 0,
}

# Nomeando a DAG e definindo quando ela vai ser executada
with DAG(
    'bookstoscrape',
    schedule_interval=timedelta(minutes=15),
    catchup=False,
    default_args=default_args
) as dag:
    # Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
    t1 = BashOperator(
    task_id='coleta-de-dados',
    bash_command="""
    cd $AIRFLOW_HOME/dags/bookstoscrape/
    python3 coleta-de-dados.py
    """)

    t2 = BashOperator(
    task_id='tratamento-dos-dados',
    bash_command="""
    cd $AIRFLOW_HOME/dags/bookstoscrape/
    python3 tratamento-dos-dados.py
    """)

    t3 = BashOperator(
    task_id='persistencia-de-dados',
    bash_command="""
    cd $AIRFLOW_HOME/dags/bookstoscrape/
    python3 persistencia-de-dados.py
    """)

    dag.doc_md = __doc__

    t1.doc_md = """\
    #### Task Documentation
    Responsável por coletar os dados do site e gerar um arquivo csv  
    """

    t2.doc_md = """\
    #### Task Documentation
    Responsável por tratar os dados e gerar um arquivo para importação no MongoDB
    """

    t3.doc_md = """\
    #### Task Documentation
    Responsável por realizar a persistencia dos dados no MongoDB
    """

    # Definindo a ordem de execução
    t1 >> t2 >> t3