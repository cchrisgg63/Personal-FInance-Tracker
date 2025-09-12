    
# Main program
def main():
    print("Welcome to Garcias Expense Tracker")

    
    expense = get_user_expense()  # make sure this function is defined
    stored_files = store_expenses_file() 
    summary = summarize_expenses() 
    
    

# Get user's expense
def get_user_expense():
    #Name of Expense
    def expense_name():
        purchased_item = input('What was bought?: ')
        print(f'Item purchased was: {purchased_item}')
    expense_name()
    #Amount of it
    def expense_amount():
        cost_amount = float(input('Type the cost: '))
        print(f'Item cost: ${cost_amount:.2f}')
    expense_amount()
    #Category it falls in 
    def category():
        expense_category= [
            "🍔 Food",
            "🏠 Home",
            "🎤 Entertainment",
            "💼 Work",
            "🦷 Misc"
        ]
        #create a index for the list, good for visual effect
        for i, food in enumerate(expense_category):
            print(food)
        
        index = len(expense_category)
        print(index)
        #len puts it at 1-5 so we - 1 later to fix the input since enumerate only does 0-4
        selected_index = int(input(f'Pick the Category this goes under: [1 - {index}]: ')) - 1
        selected_category = expense_category[selected_index]

        print(f'You selected {selected_category}')

    category() 
   



# Store the expense to a file
def store_expenses_file():
    print('Storing Expense Files')




# Summarize all expenses
def summarize_expenses():
    print('Summarizing Expenses')

   


# This will only run if the file is executed directly
if __name__ == "__main__":
    main()