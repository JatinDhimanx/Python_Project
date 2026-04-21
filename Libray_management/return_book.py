from utils import books_record
import datetime

def return_book():
    print("")
    print("--- Return a Book ---")
    book_name = input("Enter the book name to return: ").upper()
    
    found = False
    for book in books_record:
        if book == book_name:
            found = True
            break
            
    if found == False:
        print("The book '" + book_name + "' is not recognized in our database.")
        return
        
    student_name = input("Enter the student's name returning the book: ")
    
    issued_records = books_record[book_name]["issued_records"]
    found_record = False
    record_indx = 0
    actual_record_indx = -1
    
    for record in issued_records:
        if record["student_name"].upper() == student_name.upper():
            found_record = True
            actual_record_indx = record_indx
            break
        record_indx = record_indx + 1
        
    if found_record == False:
        print("This book was not issued to student named '" + student_name + "'.")
        return
        
    student_record = issued_records[actual_record_indx]
    
    issue_date = student_record["issue_date"]
    allotted_days = student_record["allotted_days"]
    
    print("")
    print("Book Details: Issued to " + student_name + " for " + str(allotted_days) + " days.")
    
    return_date = datetime.datetime.now()
        
    time_difference = return_date - issue_date
    days_kept = time_difference.days
    
    if days_kept < 0:
        print("Return date cannot be earlier than the issue date. Please try again.")
        return
        
    late_days = days_kept - allotted_days
    
    print("")
    print("The book was kept for " + str(days_kept) + " days.")
    
    if late_days > 0:
        fine = 0
        days_left = late_days
        current_week_number = 1
        current_rate = 10
        
        while days_left > 0:
            if days_left < 7:
                days_in_this_week = days_left
            else:
                days_in_this_week = 7
                
            fine = fine + (days_in_this_week * current_rate)
            
            days_left = days_left - days_in_this_week
            current_week_number = current_week_number + 1
            current_rate = current_rate * current_week_number
            
        print("The book is returned " + str(late_days) + " day(s) late!")
        print("Total fine applicable: " + str(fine) + " Rs.")
    else:
        print("The book was returned on time. No fine applicable. Thanks!")
        
    books_record[book_name]["available_quantity"] = books_record[book_name]["available_quantity"] + 1
    
    new_records = []
    index = 0
    for record in issued_records:
        if index != actual_record_indx:
            new_records.append(record)
        index = index + 1
        
    books_record[book_name]["issued_records"] = new_records
    
    print("")
    print("Book '" + book_name + "' has been successfully returned to the library.")
