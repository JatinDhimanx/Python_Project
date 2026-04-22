from utils import books_record
import datetime

def issue_book():
    print("")
    print("--- Issue a Book ---")
    book_name = input("Enter the book name to issue: ").upper()
    
    found = False
    for book in books_record:
        if book == book_name:
            found = True
            break
            
    if found == False:
        print("The book '" + book_name + "' is not recognized in our Library.")
        return
        
    if books_record[book_name]["available_quantity"] <= 0:
        print("Sorry, no copies of '" + book_name + "' are currently available.")
        return
        
    student_name = input("Enter the student's name: ")
    
    allotted_days = input("Enter the number of allotted days for this issue: ")
    if allotted_days.isdigit():
        allotted_days = int(allotted_days)
    else:
        print("Please enter a valid integer for allotted days.")
        return
            
    issue_date = datetime.datetime.now()
        
    new_record = {
        "student_name": student_name,
        "issue_date": issue_date,
        "allotted_days": allotted_days
    }

    books_record[book_name]["issued_records"].append(new_record)
    books_record[book_name]["available_quantity"] = books_record[book_name]["available_quantity"] - 1
    
    print("")
    print("Book '" + book_name + "' has been successfully issued to " + student_name + ".")
    print("Issue Date & Time: " + str(issue_date))
    print("Allotted Days: " + str(allotted_days))
    
    print("")
    print("*** IMPORTANT NOTICE REGARDING LATE RETURNS ***")
    print("If the book is not returned within the allotted days, late charges will apply as follows:")
    print("  - 1st week late: 10 Rs / day / book")
    print("  - 2nd week late: 20 Rs / day / book (10 * 2)")
    print("  - 3rd week late: 60 Rs / day / book (10 * 2 * 3)")
    print("  - And so on, progressively increasing each week.")