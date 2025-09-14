#init will make boxes but you still need to let them know each of those inputs will be a 
class Expenses:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
    
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"
