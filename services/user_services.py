from models.users import User
from repositories.file_repository import FileRepo
from typing import List


class UserServices:

    @classmethod
    def create_user(cls, user: User):
        return FileRepo.save_to_file(user.__dict__)

    @classmethod
    def get_users(cls) -> List[User]:
        users_from_file = FileRepo.read_from_file()
        users_list = []
        for user in users_from_file:

            if user['is_active'] == True:
                users_list.append(User(first_name=user['first_name'], last_name=user['last_name'], pin_code=user['pin_code'], is_active=True, id = user['id']))
            else:
                users_list.append(User(first_name=user['first_name'], last_name=user['last_name'], pin_code=user['pin_code'], is_active=True, id = user['id']))
        return users_list
    
    @classmethod
    def get_user(cls, id) -> User:
        users_from_file = FileRepo.read_from_file()
        users_list = []
        if users_from_file != None:
            for user in users_from_file:
    
                if user['is_active'] == True:
                    return (User(first_name=user['first_name'], last_name=user['last_name'], pin_code=user['pin_code'], is_active=True, id = user['id']))
                else:
                    return (User(first_name=user['first_name'], last_name=user['last_name'], pin_code=user['pin_code'], is_active=True, id = user['id']))


    @classmethod
    def update_user(cls, user: User):
        return FileRepo.save_to_file(str(user))
    
    @classmethod
    def delete_user(cls):
        pass
