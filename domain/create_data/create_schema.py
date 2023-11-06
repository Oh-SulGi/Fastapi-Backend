
def drop_table(table_name):
        import MySQLdb

        # conn = MySQLdb.connect(host='database-2.cuqfics16vuo.ap-northeast-2.rds.amazonaws.com', user='admin', password='tmcltmcl547', db='mini', charset='utf8', port=3306)
        conn = MySQLdb.connect(host='localhost', user='root', password='root', db='mini', charset='utf8', port=3306)

        cur = conn.cursor()

        cur.execute(f'drop table if exists {table_name}')

        conn.commit()
        conn.close()

def create_table(table_name):
        import MySQLdb

        conn = MySQLdb.connect(host='localhost', user='root', password='root', db='mini', charset='utf8', port=3306)

        cur = conn.cursor()

        if table_name == 'user':
                cur.execute('''
                        create table user(
                        userId varchar(20) primary key,
                        password varchar(100) not null,
                        userName varchar(10) not null,
                        email varchar(50) not null
                )
                ''')
        if table_name == 'wallet':
                cur.execute('''
                        create table wallet(
                        wallet_id mediumint auto_increment primary key,
                        userId varchar(20) not null,
                        cash int(10) not null,
                        stock_eval int(10) not null,
                        foreign key (userId) references user(userId)
                )
                ''')
        if table_name == 'portfolio':
                cur.execute('''
                        create table portfolio(
                        portfolio_id mediumint auto_increment primary key,
                        userId varchar(20) not null,
                        code_005930 int(10) not null,
                        code_373220 int(10) not null,
                        code_000660 int(10) not null,
                        code_207940 int(10) not null,
                        code_005380 int(10) not null,
                        code_051910 int(10) not null,
                        code_006400 int(10) not null,
                        code_035420 int(10) not null,
                        code_003670 int(10) not null,
                        code_012330 int(10) not null,
                        code_068270 int(10) not null,
                        code_028260 int(10) not null,
                        code_066570 int(10) not null,
                        code_096770 int(10) not null,
                        code_047050 int(10) not null,
                        code_003550 int(10) not null,
                        code_086520 int(10) not null,
                        code_091990 int(10) not null,
                        code_022100 int(10) not null,
                        code_066970 int(10) not null,
                        code_028300 int(10) not null,
                        code_035900 int(10) not null,
                        code_196170 int(10) not null,
                        code_277810 int(10) not null,
                        code_041510 int(10) not null,
                        code_328130 int(10) not null,
                        code_403870 int(10) not null,
                        code_058470 int(10) not null,
                        code_214150 int(10) not null,
                        code_214370 int(10) not null
                )
                ''')
        if table_name == 'stock_trade':
                cur.execute('''
                        create table stock_trade(
                        stock_trade_id mediumint auto_increment primary key,
                        userId varchar(20) not null,
                        code varchar(10) not null,
                        trade varchar(10) not null,
                        quantity int not null,
                        foreign key (userId) references user(userId)
                )
                ''')
        if table_name == 'stock_price_now':
                cur.execute('''
                        create table stock_price_now(
                        stock_price_now_id mediumint auto_increment primary key,
                        code varchar(10) not null,
                        price int not null,
                        date varchar(20) not null,
                        time varchar(20) not null
                )
                ''')
        if table_name == 'stock_info':
                cur.execute('''
                        create table stock_info(
                        stock_info_id mediumint auto_increment primary key,
                        회사코드 varchar(20),
                        한글명 varchar(20),
                        시가총액 varchar(20),
                        상장주수 varchar(20),
                        유동자산 varchar(20),
                        비유동자산 varchar(20),
                        자산총계 varchar(20),
                        유동부채 varchar(20),
                        비유동부채 varchar(20),
                        부채총계 varchar(20),
                        자본금 varchar(20),
                        이익잉여금 varchar(20),
                        자본총계 varchar(20),
                        매출액 varchar(20),
                        영업이익 varchar(20),
                        법인세차감전순이익 varchar(20),
                        당기순이익 varchar(20)
                )
                ''')
        if table_name == 'stock_daily_data':
                cur.execute('''
                        create table stock_daily_data(
                        stock_daily_id mediumint auto_increment primary key,
                        date varchar(20) not null,
                        open varchar(10) not null,
                        high varchar(10) not null,
                        low varchar(10) not null,
                        close varchar(10) not null,
                        volume varchar(10) not null,
                        code varchar(10) not null
                )
                ''')
        if table_name == 'quiz':
                cur.execute('''
                        create table quiz(
                        quiz_id mediumint auto_increment primary key,
                        quiz varchar(100) not null,
                        answer varchar(10) not null,
                        commentary varchar(100) not null,
                        difficulty varchar(10) not null,
                        reward int not null
                )
                ''')
        if table_name == 'access_token':
                cur.execute('''
                        create table access_token(
                        userId varchar(20) primary key,
                        access_token varchar(200) not null
                )
                ''')

        conn.commit()
        conn.close()

table_list = ['user','wallet','portfolio','stock_trade','stock_price_now','stock_info','stock_daily_data','quiz','access_token']

for table in table_list:
        # drop_table(table)
        create_table(table)