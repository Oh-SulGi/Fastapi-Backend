from sqlalchemy.orm import Session
from fastapi import Request
from passlib.context import CryptContext
from domain.user.user_schema import UserCreate
from models import User, Wallet, Portfolio, Access_Token

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(db:Session, user_create:UserCreate):
    db_user = User(
        userId=user_create.userId,
        password=pwd_context.hash(user_create.password),
        userName=user_create.userName,
        email=user_create.email
    )
    db.add(db_user)
    db.commit()

def create_wallet(db:Session, user_create:UserCreate):
    db_wallet = Wallet(
        userId=user_create.userId,
        cash=10000,
        stock_eval=0
    )
    db.add(db_wallet)
    db.commit()

def create_portfolio(db:Session, user_create:UserCreate):
    db_portfolio = Portfolio(
        userId=user_create.userId,code_005930 = 0,code_373220 = 0,code_000660 = 0,
        code_207940 = 0,code_005380 = 0,code_051910 = 0,code_006400 = 0,
        code_035420 = 0,code_003670 = 0,code_012330 = 0,code_068270 = 0,
        code_028260 = 0,code_066570 = 0,code_096770 = 0,code_047050 = 0,
        code_003550 = 0,code_086520 = 0,code_091990 = 0,code_022100 = 0,
        code_066970 = 0,code_028300 = 0,code_035900 = 0,code_196170 = 0,
        code_277810 = 0,code_041510 = 0,code_328130 = 0,code_403870 = 0,
        code_058470 = 0,code_214150 = 0,code_214370 = 0
    )
    db.add(db_portfolio)
    db.commit()

def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.userId == user_create.userId)
    ).first()

def get_user(db: Session, userId: str):
    return db.query(User).filter(User.userId == userId).first()

def get_user_wallet(db: Session, userId: str):
    return db.query(Wallet).filter(Wallet.userId == userId).first()

def get_user_portfolio(db: Session, userId: str):
    return db.query(Portfolio).filter(Portfolio.userId == userId).first()

def get_current_user(request: Request):
    current_access_user = request.cookies.get("access_user")
    return current_access_user

    