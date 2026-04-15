# README
## Table of Contents
- [Task 1: Campus Item Borrowing Management System](#task1)
  - [Overview](#task1-overview)
  - [File Structure](#task1-file-structure)
  - [Quick Start](#task1-quick-start)
  - [Code Explanation](#task1-code-explanation)
- [Task 2: MinHeap Implementation and Heap Sort](#task2)
  - [Overview](#task2-overview)
  - [Quick Start](#task2-quick-start)
  - [Code Explanation](#task2-code-explanation)

---

## <a name="task1"></a>Task 1: Campus Item Borrowing Management System
### <a name="task1-overview"></a>Overview
This task implements a lightweight campus item borrowing management system with core functionalities including viewing all items, borrowing items, returning items, and querying borrowing/return records. The system is designed following Object-Oriented Programming (OOP) principles, with clear encapsulation of data and modularization of business logic.

### <a name="task1-file-structure"></a>File Structure
```
├── item.py          # Defines Item class (encapsulates item properties and borrow/return logic)
├── user.py          # Defines User/Admin classes (distinguishes user roles)
├── borrow_system.py # Implements BorrowSystem class (core system logic)
└── main.py          # System entry (interactive command-line interface)
```

### <a name="task1-quick-start"></a>Quick Start
1. Ensure Python 3.x is installed on your machine.
2. Place all Task 1 files (`item.py`, `user.py`, `borrow_system.py`, `main.py`) in the same directory.
3. Launch the system via command line:
   ```shell
   python main.py
   ```
4. Interact with the system through the menu:
   - `1`: View all items (displays item ID, name, category and borrow status)
   - `2`: Borrow an item (requires input of user ID and item ID)
   - `3`: Return an item (requires input of item ID)
   - `4`: View all borrowing/return records
   - `0`: Exit the system

### <a name="task1-code-explanation"></a>Code Explanation
- **item.py**: The `Item` class encapsulates private attributes (`item_id`, `name`, `category`, `is_borrowed`, `borrower_id`) and provides methods to manipulate item status:
  - `borrow_item(student_id)`: Checks if the item is available, updates borrow status and records the borrower if available.
  - `return_item()`: Resets the borrow status and clears the borrower ID when the item is returned.
  - Getter methods (`get_item_id()`, `get_name()`, etc.) and `__str__()` for safe attribute access and human-readable string representation.

- **user.py**: Defines a base `User` class and an inherited `Admin` class:
  - `User` class: Encapsulates `user_id` and `name`, with getter methods for basic information.
  - `Admin` class: Overrides `is_admin()` to mark admin identity (returns `True` for admins, `False` for regular users).

- **borrow_system.py**: The `BorrowSystem` class manages the entire borrowing lifecycle:
  - `add_item()`/`add_user()`: Stores items/users in dictionaries for O(1) time complexity lookup by ID.
  - `borrow_item(user_id, item_id)`: Validates user/item existence, executes borrow logic, and logs the operation to records.
  - `return_item(item_id)`: Validates item existence, executes return logic, and logs the operation.
  - `show_all_items()`/`show_records()`: Returns all items/records for display in the CLI.

- **main.py**: Initializes the system with test data (1 admin, 1 student, 2 items) and provides an infinite loop menu for interactive operations until the user chooses to exit.

---

## <a name="task2"></a>Task 2: MinHeap Implementation and Heap Sort
### <a name="task2-overview"></a>Overview
This task implements a min-heap (minimum heap) data structure from scratch and leverages it to implement heap sort. A min-heap is a complete binary tree where each parent node's value is less than or equal to its child nodes, enabling efficient extraction of the minimum element (O(log n)) and in turn, an O(n log n) sorting algorithm.

### <a name="task2-quick-start"></a>Quick Start
1. Save the `heap_study.py` file to your working directory.
2. Run the script directly:
   ```shell
   python heap_study.py
   ```
3. The script will output the test data and sorted result:
   ```
   Original data:  [8, 3, 5, 1, 10, 2]
   Heap sort result:  [1, 2, 3, 5, 8, 10]
   ```

### <a name="task2-code-explanation"></a>Code Explanation
- **MinHeap Class**: Core implementation of the min-heap data structure:
  - `__init__()`: Initializes an empty list to store heap elements.
  - `parent(i)`/`left_child(i)`/`right_child(i)`: Helper methods to calculate the index of parent/left child/right child nodes (critical for heap traversal).
  - `insert(val)`: Appends a new value to the heap and calls `heapify_up()` to restore the min-heap property.
  - `heapify_up(i)`: Compares the i-th element with its parent; swaps them if the child is smaller, and recurses upward until the heap property is satisfied.
  - `extract_min()`: Removes and returns the minimum element (root of the heap):
    1. Returns `None` if the heap is empty.
    2. Replaces the root with the last element (after popping the last element from the heap).
    3. Calls `heapify_down(0)` to rebalance the heap.
  - `heapify_down(i)`: Finds the smallest element among the i-th node and its children; swaps the parent with the smallest child if needed, and recurses downward to maintain the min-heap property.

- **heap_sort(arr)**: Implements heap sort using the custom min-heap:
  1. Inserts all elements of the input array into the min-heap.
  2. Repeatedly extracts the minimum element from the heap and appends it to the sorted array.
  3. Returns the sorted array (ascending order).

- **Main Execution**: Tests the heap sort with a sample array `[8, 3, 5, 1, 10, 2]`, printing both the original and sorted results for verification.

---

### How to Use
1. Copy all the content above.
2. Create a new file named `README.md` in your project root directory.
3. Paste the content into the file and save it.
4. The README is now ready for use with standard Markdown renderers (GitHub, VS Code, etc.).
