from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from datetime import datetime

with DAG(
    "extract_stock_price",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
        'wait_for_downstream': True,
    },

    description="extract_stock_price",
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2023, 9, 27),
    catchup=False,
    tags=["STOCK"],
) as dag:

    def update_stock_price():
        import mojito
        from datetime import datetime
        import json
        import MySQLdb

        conn = MySQLdb.connect(host='172.31.0.1', user='ente', password='ente', db='mini', charset='utf8', port=3306)
        cur = conn.cursor()
        
        api_key = 'PSuSKPmbXmJl9nn7xQrCR78ZKQAXHXRloX6p'
        secret_key = 'eEIdVY5w+2RMLRp0Jr2C0/3PUsIs1+MdyObLe1CrGBeNYP0HR2U6u/r4D+s4DhvFw5ifN0V7O+xbX+qM5PrzzJrUt8eIgwAnXlwkiLCwkRZK1ZaLoJ8cx1ZGDu3y3OOb+7oDDI6AlODGYLKdjvVwoCeancOyJwwg6g8ClYH+gMhZt6AzIkg='
        acc_no = '68175363-01'

        broker = mojito.KoreaInvestment(
            api_key=api_key,
            api_secret=secret_key,
            acc_no=acc_no
        )

        path = './dags:/opt/airflow/dags/data/code_list.text'
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()

        code_list = list(data.split('\n'))
        now = datetime.now()

        dict_ = {}
        for code in code_list:
            resp = broker.fetch_price(code)

            dict_[code] = {
                'code' : code,
                'price' : resp['output']['stck_prpr'],
                'date' : f'{now.date()}',
                'time' : f'{now.hour}:{now.minute}'
            }
        
        stock_price_now_data = json.load(dict_)
        stock_price_now_data = [list(stock_price_now_data[i].values()) for i in stock_price_now_data]
        for data in stock_price_now_data:
            cur.execute('insert into stock_price_now(code, price, date, time) values (%s, %s, %s, %s)', data)

        conn.commit()
        conn.close()

    def update_wallet():
        import MySQLdb

        conn = MySQLdb.connect(host='172.31.0.1', user='ente', password='ente', db='mini', charset='utf8', port=3306)
        cur = conn.cursor()

        cur.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "portfolio"')
        result = cur.fetchall()
        code_list = [row[0] for row in result][:-2]

        cur.execute('SELECT userId FROM mini.wallet')
        result = cur.fetchall()
        user_list = [row[0] for row in result]

        for user in user_list:
            evaluation = 0
            for code in code_list:
                price = cur.execute(f'SELECT price FROM mini.stock_price_now where stock_price_now.code == "{code[5:]}"').fetchall()
                price = int(price[0])

                amount = cur.execute(f'select {code} from mini.portfolio where userId = "{user}"').fetchall()
                amount = int(amount[0])
                evaluation += price * amount
            cur.execute(f'update mini.wallet set stock_eval = {evaluation} where mini.wallet.userId = "{user}"')
        conn.commit()
        conn.close()

    t1 = MySqlOperator(
        task_id="truncate_table",
        mysql_conn_id="mysql",
        sql='truncate table stock_price_now'
    )

    t2 = PythonOperator(
        task_id="update_stock",
        python_callable=update_stock_price,
        dag=dag,
    )

    t3 = PythonOperator(
        task_id="update_wallet",
        python_callable=update_wallet,
        dag=dag,
    )

    t1 >> t2 >> t3