from models import Quiz
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

def get_quiz(db: Session, num: int):
    quiz = db.query(Quiz).where(Quiz.difficulty == num).order_by(func.rand()).limit(1).first()
    return quiz
