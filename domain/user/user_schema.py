from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    userId: str
    password: str
    userName: str
    email: str

    @validator('userId','password','userName','email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값이 있습니다!')
        return v

class Token(BaseModel):
    access_token: str
    token_type: str
    userId: str

    