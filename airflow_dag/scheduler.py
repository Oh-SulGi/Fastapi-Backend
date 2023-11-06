import schedule
import sys
import time

def job():
    import mojito
    from datetime import datetime
    import MySQLdb
    import json
    import os
    from dotenv import load_dotenv
    load_dotenv()

    conn = MySQLdb.connect(host='localhost', user='root', password='root', db='mini', charset='utf8', port=3306)
    cur = conn.cursor()
    cur.execute('truncate table stock_price_now')

    api_key = os.environ.get('APP_KEY')
    secret_key = os.environ.get('APP_SECRET_KEY')
    acc_no = os.environ.get('STOCK_ACCOUNT')

    broker = mojito.KoreaInvestment(
        api_key=api_key,
        api_secret=secret_key,
        acc_no=acc_no
    )

    path = 'D:\data\9월\mini_project\domain\create_data\data\code_list.text'
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    code_list = list(data.split('\n'))
    now = datetime.now()
    print(f'Job Start : {now}')

    dict_ = {}
    for code in code_list:
        resp = broker.fetch_price(code)

        dict_[code] = {
            'code' : code,
            'price' : resp['output']['stck_prpr'],
            'date' : f'{now.date()}',
            'time' : f'{now.hour}:{now.minute}'
        }

    stock_price_now_data = [list(dict_[i].values()) for i in dict_]

    for data in stock_price_now_data:
        cur.execute('insert into stock_price_now(code, price, date, time) values (%s, %s, %s, %s)',
                    data)
    
    cur.execute('SELECT userId FROM mini.user')
    rows = cur.fetchall()
    user_list = [row[0] for row in rows]

    cur.execute('SELECT userId FROM mini.portfolio')
    rows = cur.fetchall()
    portfolio_user = [row[0] for row in rows]

    cur.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "portfolio"')
    rows = cur.fetchall()
    columns = [row[0] for row in rows][:-2]
    
    
    for user in user_list:
        if user in portfolio_user:
            evaluation = 0
            for column in columns:
                cur.execute(f'select price from stock_price_now where code = "{column[5:]}"')
                result = cur.fetchall()
                price = result[0][0]

                cur.execute(f'select {column} from mini.portfolio where userId = "{user}"')
                result = cur.fetchall()
                amount = result[0][0]

                evaluation += price * amount
            cur.execute(f'UPDATE wallet SET stock_eval = {evaluation} WHERE userId = "{user}"')

    conn.commit()
    conn.close()

def exit():
    print('Job Finish')
    sys.exit()

if __name__ == "__main__":
    schedule.every(5).minutes.do(job)
    schedule.every().day.at('15:30').do(exit)