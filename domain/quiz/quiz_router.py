from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from domain.quiz import quiz_crud
from domain.wallet import wallet_crud

router = APIRouter(
    prefix='/quiz'
)

@router.get('/random')
async def random_quiz(num, answer, request: Request, db: Session = Depends(get_db)):
    quiz = quiz_crud.get_quiz(db, num)
    
    current_access_user = request.cookies.get("access_user")
    reward = quiz.reward

    if quiz.quiz and quiz.answer == answer:
        wallet_crud.update_cash(db, reward, current_access_user)
        current_cash = wallet_crud.check_cash(db, current_access_user)
        return {'reward': f'+{reward}', 'answer': f'{current_access_user}님 정답입니다. 현재 cash는 {current_cash.cash}원 있습니다'}
    return {'hint': quiz.commentary, 'answer': '오답입니다.'}
