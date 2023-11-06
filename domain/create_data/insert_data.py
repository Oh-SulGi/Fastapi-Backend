import MySQLdb

# conn = MySQLdb.connect(host='database-2.cuqfics16vuo.ap-northeast-2.rds.amazonaws.com', user='admin', password='tmcltmcl547', db='mini', charset='utf8', port=3306)
conn = MySQLdb.connect(host='localhost', user='root', password='root', db='mini', charset='utf8', port=3306)

cur = conn.cursor()

def insert_user_data(data):
        cur.execute('insert into user(userId, password, userName, email) values (%s, %s, %s, %s)',
                data)
        
def insert_wallet_data(data):
        cur.execute('insert into wallet(cash, stock_eval) values (%s, %s)',
                data)
        
def insert_portfolio_data(data):
        cur.execute('insert into portfolio(userId, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930, code_005930) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                data)
        
def insert_stock_trade_data(data):
        cur.execute('insert into stock_trade(code, trade, quantity) values (%s, %s, %s)',
                data)
        
def insert_stock_price_now_data(data):
        cur.execute('insert into stock_price_now(code, price, date, time) values (%s, %s, %s, %s)',
                data)

def insert_stock_info_data(data):
        cur.execute('insert into stock_info(회사코드, 한글명, 시가총액, 상장주수, 유동자산, 비유동자산, 자산총계, 유동부채, 비유동부채, 부채총계, 자본금, 이익잉여금, 자본총계, 매출액, 영업이익, 법인세차감전순이익, 당기순이익) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            data)

def insert_stock_daily_data_data(data):
        cur.execute('insert into stock_daily_data(date, open, high, low, close, volume, code) values (%s, %s, %s, %s, %s, %s, %s)',
                data)
        
def insert_quiz_data(data):
        cur.execute('insert into quiz(quiz, answer, commentary, difficulty, reward) values (%s, %s, %s, %s, %s)',
                data)
        
import json
import pandas as pd

stock_price_now_data_path = 'D:\data\9월\mini_project\domain\create_data\data\stock_price_now.json'
with open(stock_price_now_data_path, 'r', encoding='cp949') as f:
        stock_price_now_data = json.load(f)

stock_price_now_data = [list(stock_price_now_data[i].values()) for i in stock_price_now_data]

for data in stock_price_now_data:
        insert_stock_price_now_data(data)

# df = pd.read_csv('D:\data\9월\mini_project\domain\create_data\data\금융퀴즈.csv', encoding='cp949')

# datas = df.values.tolist()
# for data in datas:
#         insert_quiz_data(data)

# stock_info_path = 'D:\data\9월\mini_project\data\stock_info.json'

# with open(stock_info_path, 'r', encoding='utf-8') as f:
#         stock_info = json.load(f)

# stock_info = [list(stock_info[i].values()) for i in stock_info.keys()]

# for i in range(len(stock_info)):
#         if len(stock_info[i]) == 17:
#                 insert_stock_info_data(stock_info[i])

# stock_daily_data_path = 'D:\data\9월\mini_project\domain\create_data\data\stock_daily_price.json'

# with open(stock_daily_data_path, 'r', encoding='utf-8') as f:
#         stock_daily_data = json.load(f)

# stock_daily_data_list = [list(stock_daily_data[i].values()) for i in range(len(stock_daily_data))]

# for i in range(len(stock_daily_data_list)):
#         insert_stock_daily_data_data(stock_daily_data_list[i])

conn.commit()
conn.close()