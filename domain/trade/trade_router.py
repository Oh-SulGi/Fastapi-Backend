from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.trade import trade_crud

from dotenv import load_dotenv
load_dotenv()

router = APIRouter(
    prefix='/trade'
)

@router.post('/trade')
async def trade_stock(request: Request, code: str, num: int, trade: str, db: Session = Depends(get_db)):
    user = request.cookies.get("access_user")

    if trade == 'buy':
        trade_crud.buy_stock(db, user, code, num)
        trade_crud.eval_stock(db, user)
    elif trade == 'sell':
        trade_crud.sell_stock(db, user, code, num)
        trade_crud.eval_stock(db, user)

@router.post('/eval')
async def evaluation_stock(request: Request, db: Session = Depends(get_db)):
    user = request.cookies.get("access_user")
    evaluation = trade_crud.eval_stock(db, user)
    return evaluation