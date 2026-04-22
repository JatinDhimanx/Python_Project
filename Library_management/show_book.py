from utils import books_record

def show_books():
    print("")
    print("--- Available Books ---")
    
    count = 0
    for book_name in books_record:
        book_details = books_record[book_name]
        available_qty = book_details["available_quantity"]
        if available_qty > 0:
            count = count + 1
            print(str(count) + ". " + book_name + " (Available Copies: " + str(available_qty) + ")")
            
    if count == 0:
        print("No books are currently available in the library.")