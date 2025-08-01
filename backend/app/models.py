from sqlalchemy import Column, Integer, String
from app.core.database import Base
import uuid

def uuid_generate():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, default=uuid_generate)
    name = Column(String)
    email = Column(String, unique=True, index=True)