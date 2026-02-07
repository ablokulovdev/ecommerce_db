import hashlib 
from app.models.user import User


def hash_password(password:str):
     return hashlib.sha256(password.encode()).hexdigest()
    

def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash
