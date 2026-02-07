
from app.core.database import engin,SessionLocal
from app.models.base import Base
from app.models.user import User
from app.services.hass_password import hash_password

Base.metadata.create_all(engin)



def register():
    
    full_name = input("full_name: ").capitalize()
    username = input("Username: ").capitalize().strip()
    email = input("email: ").lower().strip()
    password_hash= input("Password: ")
    password = hash_password(password_hash)
    
    
    with SessionLocal() as session:
        user = User(full_name=full_name,username=username,email=email,password=password)
        
        session.add(user)
        
        session.commit()
        print("You have successfully registered.")


def login():
    print("Username and password input: ")
    username = input("Username: ").capitalize().strip()
    email = input("email: ").lower().strip()

    with SessionLocal() as session:
        
        user = session.query(User).where(User.username == username).first()
        
        if user:
            email = session.query(User).filter(User.email == email).first()
            
        else :
            print("user yoki email notug'ri")
            
        
       
        
        
     
        

