from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    
    user_id = Column("id",Integer,index=True,primary_key=True)
    username = Column("username",String(length=50),unique=True,nullable=False)
    password = Column("password",String(),nullable=False)
    
    created_at = Column("created_at",DateTime,default=datetime.now())
    updated_at = Column("updated_at",DateTime,onupdate=datetime.now)
    
    