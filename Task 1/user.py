class User:
    """Base class for regular users"""
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_user_id(self):
        return self.__user_id
    
    def get_name(self):
        return self.__name

    #Check if this user is admin
    def is_admin(self):
        return False
    
class Admin(User):
    """Admin class, inherited from User"""
    def is_admin(self):
        return True #Override method
