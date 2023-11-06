from models import Wallet
from sqlalchemy.orm import Session

def update_cash(db: Session, num: int, user: str):
    db.query(Wallet).filter(Wallet.userId == user).update({Wallet.cash: Wallet.cash + num})
    db.commit()
    db.close()

def check_cash(db: Session, user: str):
    return db.query(Wallet).filter(Wallet.userId == user).first()