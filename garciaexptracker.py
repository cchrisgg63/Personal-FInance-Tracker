from garciaexpenses import Expenses
import calendar
import datetime

#Take off "#" in Line 12 and 13 if you want to add more expenses

# Main program
def main():
    budget = 1340
    print("Welcome to Garcias Expense Tracker")
    expense_file_path = '/Users/admin/reactapp/ECGTech/Personal Finance Tracker/garciaexpenses.csv'  
    expense = get_user_expense()  # make sure this function is defined
    store_expenses_file(expense, expense_file_path)
    summarize_expenses(expense_file_path,budget) 
    
    
    

# Get user's expense
def get_user_expense():
    #Name of Expense
    purchased_item = input('What was bought?: ')
    #Amount of it
    cost_amount = float(input('How much was it?: '))
    #Category it falls in
    expense_category= [
        "🍔 Food",
        "🏠 Home",
        "🎤 Entertainment",
        "💼 Work",
        "🦷 Misc"
        ]
    #create a index for the expense_category, cat_var is the variable itself, i is the index number. 
    # i+1 makes a numbered list for each category, good for visual effect
    #index would normally start at 0, so that's why there's a +1
    for i, cat_var in enumerate(expense_category):
        print(f'{i+1}. {cat_var}')
    
    index = len(expense_category)
    #len counts it at 1-5 so we - 1 later to fix the input since enumerate only does 0-4

    selected_index = int(input(f'Pick the Category this goes under: [1 - {index}]: ')) - 1
    selected_category = expense_category[selected_index]
    
    new_expense = Expenses(name=purchased_item, amount=cost_amount, category=selected_category)
    return new_expense

   



# Store the expense to a file
#grab the expense amount, category, and price from the above function and store it into the class Expenses

def store_expenses_file(expense: Expenses, expense_file_path): 
    with open('ECGTech/Personal Finance Tracker/garciaexpenses.csv', 'a') as file:
        print(f"Saving expense file: {expense} to {expense_file_path}\n")
        #making it a expense.name instead of expense_name is because the former is a tool stores the items within expense variable
        #if we use the latter, it will just make two variables that aren't storing any information into the big storage it's
        #just storing it into the small variables which can't be accessed outside store_expense_files
        file.write(f"{expense.name},{expense.amount},{expense.category}\n ")
    return 
 
    





# Summarize all expenses
def summarize_expenses(expense_file_path, budget):
    expenses : list[Expenses] = []

    # I want to separate each of the amounts and grab the categories associated with them then make a total of each
    with open('ECGTech/Personal Finance Tracker/garciaexpenses.csv','r') as file:
        #readlines is a helpful tool that allows you read large amounts of data because it loads it in increments instead of all at once, potentiall crashing your program
        lines=file.readlines()
        for line in lines:
            if len(line) <2:
                continue
            expense_name, expense_amount, expense_category = line.strip().split(',')
            line_expense = Expenses(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)
            

    #we're using a dict because these are strings not floats
    amount_by_category = {}    
    for expense in expenses:
        #all the categoires are being pulled from Expenses into key
        key = expense.category
        if key in amount_by_category:
            #will check current dict and look for the existing jar
            amount_by_category[key] += float(expense_amount)
        else: #if no jar is made, then it will create it and add it to it
            amount_by_category[key] = float(expense_amount)


    #adding the :.2f makes the amounts easier to calculate otherwise it will give out a huger number
    print ('\nExpenses by Category: ')
    #.items will pull both the amount and the category at the same time. Otherwise it will just create a value error
    for cat, amount in amount_by_category.items():
        print(f'  {cat}: ${amount:.2f}')

    total_spent = sum([x.amount for x in expenses])
    print(f'\n Total Spent is: {total_spent}')
    remaining_budget = budget - total_spent
    print(f'\nRemaining Budget: {remaining_budget} ')

    now = datetime.datetime.now() 
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print (green(f'💳 Budget Per Day ${daily_budget:.2f}'))

#give text custimzation
def green(text):
    return f"\033[92m{text}\033[0m"    
   


# This will only run if the file is executed directly
if __name__ == "__main__":
    main()

    #Completed and submitted into github
    