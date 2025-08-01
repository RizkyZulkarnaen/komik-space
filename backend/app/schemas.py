from pydantic import BaseModel, EmailStr

class userOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class config:
        orm_mode = True