from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from domain.quiz import quiz_crud
from domain.user import user_crud, user_router

router = APIRouter(
    prefix='/wallet'
)