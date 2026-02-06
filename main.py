from app.db.database import Base,SessionLocal,engin
from app.models.user  import User


Base.metadata.create_all(engin)

session = SessionLocal()


user01 = User(username="wexno",password=1238)

session.add(user01)
session.commit()


print(user01)