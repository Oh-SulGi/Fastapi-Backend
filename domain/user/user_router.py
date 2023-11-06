from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
from fastapi.templating import Jinja2Templates

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context
import os
from dotenv import load_dotenv
load_dotenv()

algo = os.getenv('ALGORITHM')
secret_key = os.getenv('ACCESS_TOKEN_SECRET_KEY')

templates = Jinja2Templates(directory="templates")
router = APIRouter(
    prefix='/user'
)

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algo)
    return encoded_jwt

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
async def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='이미 존재하는 사용자입니다.')
    user_crud.create_user(db=db, user_create=_user_create)
    user_crud.create_wallet(db=db, user_create=_user_create)
    user_crud.create_portfolio(db=db, user_create=_user_create)

@router.get('/login')
async def get_login_form(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@router.post('/login')
async def login(response: Response, login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.get_user(db, login_form.username)

    if not user or not pwd_context.verify(login_form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='아이디나 비밀번호가 일치하지 않습니다.',
            headers={'WWW-Authenticate': 'Baerer'},
        )
    
    access_token_expire = timedelta(minutes=60)
    data = {
        'sub': user.userId,
        'exp': datetime.utcnow() + access_token_expire
    }
    access_token = create_access_token(data, expires_delta=access_token_expire)
    response.set_cookie(key='access_token', value=access_token, expires=access_token_expire, httponly=True)
    response.set_cookie(key='access_user', value=user.userId, expires=access_token_expire, httponly=True)

    return user_schema.Token(access_token=access_token, token_type="bearer", userId=user.userId)

@router.get('/logout')
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return HTTPException(status_code=status.HTTP_200_OK, detail="Logout successful")

@router.get('/current_user')
async def current_user(request: Request):
    current_access_user = request.cookies.get("access_user")
    cyrrent_access_token = request.cookies.get("access_token")
    return {
        'access_user' : current_access_user,
        'access_token' : cyrrent_access_token
    }