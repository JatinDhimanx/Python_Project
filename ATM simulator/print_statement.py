def statement(transaction_history, balance):
    print("\n--- Transaction Statement ---")
    
    if len(transaction_history) == 0:
        print("No transactions yet.")
    else:
        for transaction in transaction_history:
            print(transaction)
            
    print(f"Current Balance: RS.{balance}")
    print("-----------------------------")
