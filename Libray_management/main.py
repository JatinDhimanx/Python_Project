from add_book import add_book
from show_book import show_books
from issue_book import issue_book
from return_book import return_book

def library():
    print("==================================================")
    print("      LIBRARY MANAGEMENT SYSTEM      ")
    print("==================================================")
    
    is_running = True
    while is_running:
        print("")
        print("--- Main Menu ---")
        print("1. Add a New Book")
        print("2. Show Available Books")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("\nPlease enter your choice (1-5): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            is_running = False
        else:
            print("Invalid Input! Please enter a number between 1 and 5.")


library()