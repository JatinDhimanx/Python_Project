from display_balance import show_balance
from deposit_money import deposit
from withdraw_money import withdraw
from print_statement import statement

balance = 0.0
transaction_history = []

print("Welcome to the Simple ATM System!")

while True:
    print("\n--- ATM Menu ---")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")
    
    choice = input("Please select an option (1-5): ")
    
    if choice == '1':
        show_balance(balance)
        
    elif choice == '2':
        balance, transaction_history = deposit(balance, transaction_history)
            
    elif choice == '3':
        balance, transaction_history = withdraw(balance, transaction_history)
            
    elif choice == '4':
        statement(transaction_history, balance)
        
    elif choice == '5':
        print("\nThank you for using the ATM System. Goodbye!")
        break
        
    else:
        print("\nInvalid choice. Please choose an option from 1 to 5.")
