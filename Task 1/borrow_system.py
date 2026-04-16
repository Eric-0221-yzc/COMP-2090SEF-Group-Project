class BorrowSystem:
    """Core logic for campus item borrowing system"""
    def __init__(self):
        self.items = {}  # Store items: {item_id: Item object}
        self.users = {}  # Store users: {user_id: User object}
        self.records = [] # Borrow/return history

    # Add a new item
    def add_item(self, item):
        self.items[item.get_item_id()] = item

    # Add a new user
    def add_user(self, user):
        self.users[user.get_user_id()] = user

    # Get item by ID
    def get_user(self, user_id):
        return self.users.get(user_id)

    # Get item by ID
    def get_item(self, item_id):
        return self.items.get(item_id)

    # Borrow an item
    def borrow_item(self, user_id, item_id):
        user = self.users.get(user_id)
        item = self.items.get(item_id)
        if not user or not item:
            return False, "User/Item doesn't exist"
        if item.borrow_item(user_id):
            self.records.append(f"{user_id} borrow {item_id}")
            return True, "Borrowing Successfully"
        return False, "Item has been borrowed"

    # Return an item
    def return_item(self, item_id):
        item = self.get_item(item_id)
        if not item:
            return False, "Item doesn't exist"
        if item.return_item():
            self.records.append(f"{item_id} Item returned")
            return True, "Return Successfully"
        return False, "Item was not lent out"

    # Show all items 
    def show_all_items(self):
        return list(self.items.values())

    # Show all operation records
    def show_records(self):
        return self.records
