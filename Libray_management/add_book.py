from utils import books_record

def add_book():
    print("")
    print("--- Add a New Book ---")
    book_name = input("Enter the name of the book to add: ").upper()
    
    if book_name == "":
        print("Book name cannot be empty.")
        return
        
    quantity_str = input("Enter the quantity of books: ")
    if quantity_str.isdigit():
        quantity = int(quantity_str)
    else:
        print("Invalid quantity. Please enter a valid number.")
        return
        
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    found = False
    for book in books_record:
        if book == book_name:
            found = True
            break

    if found:
        print("The book '" + book_name + "' already exists. Adding " + str(quantity) + " more copies.")
        books_record[book_name]["total_quantity"] = books_record[book_name]["total_quantity"] + quantity
        books_record[book_name]["available_quantity"] = books_record[book_name]["available_quantity"] + quantity
    else:
        books_record[book_name] = {
            "total_quantity": quantity,
            "available_quantity": quantity,
            "issued_records": []
        }
        print("Book '" + book_name + "' added successfully with quantity " + str(quantity) + "!")