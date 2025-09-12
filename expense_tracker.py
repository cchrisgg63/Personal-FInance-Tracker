from expenses import Expense
import calendar
import datetime

def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = "/Users/admin/reactapp/ECGTech/Personal Finance Tracker/expenses.csv"
    budget = 1340

    

#If you want to input more expenses remove the comment
#Get users to input their expense
    expense = get_user_expense()

#ALSO remove below # to save them too
#store the expenses into a file
    save_exp_to_file(expense, expense_file_path)
    
#read the file and summarize the expense against the assets
    summarize_expenses(expense_file_path, budget)

#getting your user expenses from the users
def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))


    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        '💼 Work',
        '🎤 Entertainment',
        '🦷 Misc',
    ]
    #if you don't break out of the true loop, it will keep going forever
    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f'{i +1}, {category_name}')


        value_range = f'[1 - {len(expense_categories)}]'
        selected_index = int(input(f'Enter a category number: {value_range} ' )) - 1

       
      

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)
            
            return new_expense
        else :
            print("Invalid category. Please try again!")
     
            

        break


   
# saving your expenses to files to be called later
def save_exp_to_file(expense: Expense, expense_file_path):
    print(f"Saving expense file: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f" {expense.name}, {expense.amount}, {expense.category} \n")

#summarize your expenses

def summarize_expenses(expense_file_path , budget):
    print(f"Summarizing expense")
    #adding list to calling Expense will give you everything as a list instead of only one input
    expenses : list[Expense] = []

    with open(expense_file_path, "r") as f:
        #this will give us a command that will let us enumerate the lines
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(", ")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category)
            
            expenses.append(line_expense)
 
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += float(expense_amount)
        else: 
            amount_by_category[key] = float(expense_amount)


    print ('Expenses by Category: ')
    for key, amount in amount_by_category.items():
        print(f'  {key}: ${amount:.2f}')

    total_spent = sum([expense.amount for x in expenses])
    print(f'💵 Total Spent: ${total_spent:.2f}  ')

    remaining_budget = budget - total_spent
    print(f'🏦 Budget Remaining: ${remaining_budget:.2f}  ')
    
    now = datetime.datetime.now() 
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print (green(f'💳 Budget Per Day ${daily_budget:.2f}'))

#give text custimzation
def green(text):
    return f"\033[92m{text}\033[0m"






#this will only be true when we run it directly instead of importing it
if __name__ == "__main__":
    main()