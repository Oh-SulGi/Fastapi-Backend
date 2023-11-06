from fastapi import FastAPI, Depends, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from database import engine
import uvicorn
import models
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from domain.user import user_router
from domain.quiz import quiz_router
from domain.trade import trade_router
from database import engine
models.base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates") 
app.mount("/static", StaticFiles(directory="static"), name="static") 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(user_router.router)
app.include_router(quiz_router.router)
app.include_router(trade_router.router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)