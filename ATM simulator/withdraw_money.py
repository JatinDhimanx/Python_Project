def withdraw(balance, transaction_history):
    amount_str = input("Enter the amount to withdraw: RS.")
    amount = float(amount_str)
    
    if amount > 0:
        if amount <= balance:
            balance = balance - amount
            transaction_history.append(f"Withdrew: RS.{amount}")
            print(f"\nSuccessfully withdrew RS.{amount}. Your new balance is RS.{balance}")
        else:
            print(f"\nInsufficient funds! Your balance is only RS.{balance}.")
    else:
        print("\nInvalid amount. Please enter a positive number.")
        
    return balance, transaction_history
