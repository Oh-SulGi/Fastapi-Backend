from sqlalchemy import Column, Integer, String, Date
from database import base

class User(base):
    __tablename__ = 'user'

    userId = Column(String(20), primary_key=True)
    password = Column(String(20), unique=True, nullable=False)
    userName = Column(String(10), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

class Wallet(base):
    __tablename__ = 'wallet'

    wallet_id = Column(Integer, autoincrement=True, primary_key=True)
    userId = Column(String(20), unique=True, nullable=False)
    cash = Column(Integer, unique=False, nullable=False)
    stock_eval = Column(Integer, unique=False, nullable=False)

class Portfolio(base):
    __tablename__ = 'portfolio'

    portfolio_id = Column(Integer, autoincrement=True, primary_key=True)
    userId = Column(String(20), unique=True, nullable=False)
    code_005930 = Column(Integer, unique=False, nullable=False)
    code_373220 = Column(Integer, unique=False, nullable=False)
    code_000660 = Column(Integer, unique=False, nullable=False)
    code_207940 = Column(Integer, unique=False, nullable=False)
    code_005380 = Column(Integer, unique=False, nullable=False)
    code_051910 = Column(Integer, unique=False, nullable=False)
    code_006400 = Column(Integer, unique=False, nullable=False)
    code_035420 = Column(Integer, unique=False, nullable=False)
    code_003670 = Column(Integer, unique=False, nullable=False)
    code_012330 = Column(Integer, unique=False, nullable=False)
    code_068270 = Column(Integer, unique=False, nullable=False)
    code_028260 = Column(Integer, unique=False, nullable=False)
    code_066570 = Column(Integer, unique=False, nullable=False)
    code_096770 = Column(Integer, unique=False, nullable=False)
    code_047050 = Column(Integer, unique=False, nullable=False)
    code_003550 = Column(Integer, unique=False, nullable=False)
    code_086520 = Column(Integer, unique=False, nullable=False)
    code_091990 = Column(Integer, unique=False, nullable=False)
    code_022100 = Column(Integer, unique=False, nullable=False)
    code_066970 = Column(Integer, unique=False, nullable=False)
    code_028300 = Column(Integer, unique=False, nullable=False)
    code_035900 = Column(Integer, unique=False, nullable=False)
    code_196170 = Column(Integer, unique=False, nullable=False)
    code_277810 = Column(Integer, unique=False, nullable=False)
    code_041510 = Column(Integer, unique=False, nullable=False)
    code_328130 = Column(Integer, unique=False, nullable=False)
    code_403870 = Column(Integer, unique=False, nullable=False)
    code_058470 = Column(Integer, unique=False, nullable=False)
    code_214150 = Column(Integer, unique=False, nullable=False)
    code_214370 = Column(Integer, unique=False, nullable=False)

class Quiz(base):
    __tablename__ = 'quiz'

    quiz_id = Column(Integer, autoincrement=True, primary_key=True)
    quiz = Column(String(100), unique=False, nullable=False)
    answer = Column(String(10), unique=False, nullable=False)
    commentary = Column(String(100), unique=False, nullable=False)
    difficulty = Column(Integer, unique=False, nullable=False)
    reward = Column(Integer, unique=False, nullable=False)

class Access_Token(base):
    __tablename__ = 'access_token'

    userId = Column(String(20), primary_key=True)
    access_token = Column(String(200), unique=True, nullable=False)

class Stock_Daily_Data(base):
    __tablename__ = 'stock_daily_data'

    Stock_daily_id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(Date, unique=False, nullable=False)
    open = Column(Integer, unique=False, nullable=False)
    high = Column(Integer, unique=False, nullable=False)
    low = Column(Integer, unique=False, nullable=False)
    close = Column(Integer, unique=False, nullable=False)
    volume = Column(Integer, unique=False, nullable=False)
    code = Column(String(10), unique=False, nullable=False)

class Stock_Price_Now(base):
    __tablename__ = 'stock_price_now'

    Stock_price_now_id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String(10), unique=False, nullable=False)
    price = Column(Integer, unique=False, nullable=False)
    date = Column(String(20), unique=False, nullable=False)
    time = Column(String(20), unique=False, nullable=False)