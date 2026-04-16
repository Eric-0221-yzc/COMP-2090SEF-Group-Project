from item import Item
from user import User, Admin
from borrow_system import BorrowSystem

def main():
    # Initialize system
    system = BorrowSystem()

    #Predefined test data
    admin = Admin("A001", "Admin")
    system.add_user(admin)
    system.add_user(User("S001", "Student 1"))
    system.add_item(Item("I001", "Power Bank", "Electronics"))
    system.add_item(Item("I002", "Umbrella", "Daily Necessities"))

    # Main menu
    while True:
        print("\n===== Campus Item Borrowing Management System =====")
        print("1. View all items")
        print("2. Borrow an item")
        print("3. Return an item")
        print("4. View records")
        print("0. Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            for item in system.show_all_items():
                print(item)
        elif choice == "2":
            uid = input("User ID: ")
            iid = input("Item ID: ")
            res, msg = system.borrow_item(uid, iid)
            print(msg)
        elif choice == "3":
            iid = input("Item ID: ")
            res, msg = system.return_item(iid)
            print(msg)
        elif choice == "4":
            records = system.show_records()
            for r in records:
                print(r)
        elif choice == "0":
            print("Exiting system")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
