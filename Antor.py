filename = "items.txt"

# List to store data
data_list = []

# Function to load data from the file
def load_data():
    global data_list
    try:
        with open(filename, 'r') as file:
            data_list = [{"item": line.strip()} for line in file.readlines()]
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")

# Function to save data to the file
def save_data():
    with open(filename, 'w') as file:
        for data in data_list:
            file.write(data['item'] + '\n')

# Function to add an item
def add_item():
    item = input("Enter item to add: ")
    data_list.append({"item": item})
    save_data()  # Save the updated data to the file
    print("Item added successfully!")

# Function to view all items
def view_all():
    if data_list:
        print("\nAll Items:")
        for idx, data in enumerate(data_list):
            print(f"{idx + 1}. {data['item']}")
    else:
        print("No items to display.")

# Function to search for an item
def search_item():
    search = input("Enter item to search: ")
    found = False
    for idx, data in enumerate(data_list):
        if data['item'] == search:
            print(f"Item found at position {idx + 1}: {data['item']}")
            found = True
            break
    if not found:
        print("Item not found.")

# Function to edit an item
def edit_item():
    view_all()
    try:
        idx = int(input("Enter the position of the item to edit: ")) - 1
        if 0 <= idx < len(data_list):
            new_item = input("Enter the new item: ")
            data_list[idx]['item'] = new_item
            save_data()  
            print("Item updated successfully!")
        else:
            print("Invalid position.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def delete_item():
    view_all()
    try:
        idx = int(input("Enter the position of the item to delete: ")) - 1
        if 0 <= idx < len(data_list):
            data_list.pop(idx)
            save_data()  
            print("Item deleted successfully!")
        else:
            print("Invalid position.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main_menu():
    load_data() 
    while True:
        print("\nProject Menu:")
        print("1. Add")
        print("2. View All")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_item()
        elif choice == '4':
            edit_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
