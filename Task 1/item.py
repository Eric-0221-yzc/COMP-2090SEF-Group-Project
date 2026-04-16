class Item:
    """Item class: Encapsulates item in information and borrowwwing status"""
    def __init__(self, item_id, name, category):
        #Private attributes (encapsulation)
        self.__item_id = item_id
        self.__name = name
        self.__category = category
        self.__is_borrowed = False #Default: available
        self.__borrower_id = None # Borrower ID

    #Get item ID 
    def get_item_id(self):
        return self.__item_id

    #Get item name
    def get_name(self):
        return self.__name

    #Get item category
    def get_category(self):
        return self.__category

    #Check if item is borrowed
    def is_borrowed(self):
        return self.__is_borrowed

     #Borrow this item
    def borrow_item(self, student_id):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            self.__borrower_id = student_id
            return True
        return False

    #Return this item
    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            self.__borrower_id = None
            return True
        return False

    #Get current borrower ID
    def get_borrower(self):
        return self.__borrower_id

    #String representation
    def __str__(self):
        status = "Lent out" if self.__is_borrowed else "Can be borrowed"
        return f"ID: {self.__item_id} | {self.__name} | {self.__category} | status:{status}"
