from app.models.user_model import User
from app.database.fake_database import users
from app.services import credential_services

def get_all_users():
    return users

def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        
    return None

def create_user(new_user: User):
    for user in users:
        if user.id == new_user.id:
            return False
        
    users.append(new_user)
    credential_services.set_user_credentials(new_user.id)
    return True

def update_user(updated_user: User):
    for index, user in enumerate(users):
        if user.id == updated_user.id:
            users[index] = updated_user
            return True

    return False            

def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            credential_services.delete_credentials(user_id)
            return True
        
    return False    
