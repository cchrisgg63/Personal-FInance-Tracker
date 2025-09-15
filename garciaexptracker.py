from garciaexpenses import Expenses

# Main program
def main():
    print("Welcome to Garcias Expense Tracker")
        
    #expense = get_user_expense()  # make sure this function is defined
    expense_file_path = '/Users/admin/reactapp/ECGTech/Personal Finance Tracker/garciaexpenses.csv'
    #store_expenses_file(expense, expense_file_path)
    summarize_expenses(expense_file_path) 
    
    
    

# Get user's expense
def get_user_expense():
    #Name of Expense

    purchased_item = input('What was bought?: ')
    print(f'Item purchased was: {purchased_item}')
   
    #Amount of it
    cost_amount = float(input('Type the cost: '))
    print(f'Item cost: ${cost_amount:.2f}')
   
    #Category it falls in
    expense_category= [
        "🍔 Food",
        "🏠 Home",
        "🎤 Entertainment",
        "💼 Work",
        "🦷 Misc"
        ]
    #create a index for the list, good for visual effect
    for i, food in enumerate(expense_category):
        print(f'{i+1} , {food}')
    
    index = len(expense_category)
    
    #len puts it at 1-5 so we - 1 later to fix the input since enumerate only does 0-4
    selected_index = int(input(f'Pick the Category this goes under: [1 - {index}]: ')) - 1
    selected_category = expense_category[selected_index]
    
        
    return Expenses(name=purchased_item, amount=cost_amount, category=selected_category)

   



# Store the expense to a file
#grab the expense amount, category, and price from the above function and store it into the class Expenses

def store_expenses_file(expense: Expenses, expense_file_path): 
    with open('ECGTech/Personal Finance Tracker/garciaexpenses.csv', 'a') as file:
        print(f"Saving expense file: {expense} to {expense_file_path}\n")
        file.write(f" {expense.name} , {expense.amount} , {expense.category} ")
    return 
 
    





# Summarize all expenses
def summarize_expenses(expense_file_path):
    amount = []

    with open('ECGTech/Personal Finance Tracker/garciaexpenses.csv','r') as file:
        #remove the () in file because it overwrites anything if you add the parantheses
        for line in file:
            line = line.strip().split(',')
            name = line[0].strip()
            amount = float(line[1].strip())
            category = line[2].strip()
            total = sum(amount)
        return print(f'Total Spent is ${total}')
     
        #I want the columns of the columns separated so I can take all the amount #'s and 
        #add them all up to show the total expenditures
        #then subtract it from the budget to see the remaining balance
        #then divide the remaining balance to see what's the budget per day
   


# This will only run if the file is executed directly
if __name__ == "__main__":
    main()