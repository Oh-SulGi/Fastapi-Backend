from models import Wallet, Stock_Price_Now
from sqlalchemy.orm import Session
from sqlalchemy import text

def buy_stock(db: Session, user: str, code: str, num: int):
    price = db.query(Stock_Price_Now.price).filter(Stock_Price_Now.code == code).first()
    price = int(price[0])
    money = db.query(Wallet.cash).filter(Wallet.userId == user).first()
    money = int(money[0])

    if price * num <= money:
        db.query(Wallet).filter(Wallet.userId == user).update({Wallet.cash: Wallet.cash - (price * num)})
        db.execute(text(f'update mini.portfolio set code_{code} = code_{code} + {num} where mini.portfolio.userId = "{user}"'))
        db.execute(text('insert into stock_trade(userId, code, trade, quantity) values (:user_id,:code,:trade,:quantity)'),{'user_id': user,'code':code,'trade':'buy','quantity':num})
        db.commit()
        db.close()
    else:
        return '잔액이 부족합니다.'
    
def sell_stock(db: Session, user: str, code: str, num: int):
    price = db.query(Stock_Price_Now.price).filter(Stock_Price_Now.code == code).first()
    price = int(price[0])

    if num > 0:
        db.query(Wallet).filter(Wallet.userId == user).update({Wallet.cash: Wallet.cash + (price * num)})
        db.execute(text(f'update mini.portfolio set code_{code} = code_{code} - {num} where mini.portfolio.userId = "{user}"'))
        db.execute(text('insert into stock_trade(userId, code, trade, quantity) values (:user_id,:code,:trade,:quantity)'),{'user_id': user,'code':code,'trade':'sell','quantity':num})
        db.commit()
        db.close()
    else:
        return '매도 수량을 1이상 입력해주세요'
    
def eval_stock(db: Session, user: str):
    code_list = db.execute(text('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "portfolio"'))
    columns = [row[0] for row in code_list][2:]

    evaluation = 0
    for column in columns:
        price = db.execute(text(f'select price from stock_price_now where code = "{column[5:]}"')).fetchone()
        price = int(price[0])
        amount = db.execute(text(f'select {column} from mini.portfolio where userId = "{user}"')).fetchone()
        amount = int(amount[0])
        evaluation += price * amount
    
    db.query(Wallet).filter(Wallet.userId == user).update({Wallet.stock_eval: Wallet.stock_eval + evaluation})
    db.commit()
    db.close()
    return evaluation