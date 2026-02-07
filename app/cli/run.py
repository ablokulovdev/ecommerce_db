from app.repositories.user_repo import(
    register,
    login
)
from .menu import auth_menu, main_menu


def run():
    
    
    while True:
        
        auth_menu()
        choises = input("Select menu: ")
        
        if choises == "1":
            register() # register
        
        elif choises == "2":
            user = login() 
            
            if user :
                
                main_menu()
                choises = input("Select menu: ")
                
                
        
        elif choises == "0":
             exit(0)
        
        