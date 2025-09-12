#this class holds the expense infomration
class  Expense:
    #init runs everytime you add new data
    #self is a box that allows us to put in those identifiers into a box. then, continues to
    # make more boxes based off the other programs data
    def __init__ (self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
        
    #prints out the expense value instead of a memory address 
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount: .2f} >"