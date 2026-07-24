
class Expense_tracker:
    def __init__(self):
        self.day =''
        self.month =''
        self.year =''
        self.amount=0
        self.categories=['food','travel','shopping','bills','entertainment', 'miscellaneous']
        self.category=""
        self.description='miscellaneous'
        self.methods=['cash','upi','card','gpay']
        self.method=""

    def ask_input(self,message):
        value= input(message)
        return value
   
    def collect(self):
        self.day = self.ask_input("Enter day: ")
        self.month = self.ask_input("Enter month: ")
        self.year = self.ask_input("Enter year: ")
        self.amount= self.ask_input("Enter amount: ")
        self.category= self.ask_input("Enter category: ")
        self.description =self.ask_input("Enter short desctiption: ")
        self.method= self.ask_input("Enter payment method: ")
   

    def display(self):
        print(f"date: {self.year}/{int(self.month):2}/{int(self.day):2}")
        print(f"amount: {self.amount}")
        print(f"category: {self.category}")
        print(f"descripiton: {self.descripiton}")
        print(f"payment method: {self.method}")
        self.ask_again()
       
   
    def ask_again(self):
        choice= input("Would you like to edit info (y/n): ")
        if choice.lower() =='y':
            self.edit_opiton()
           
        elif choice.lower()=='n':
            return
   
    def edit_opiton(self): pass

   
   
    def edit_input(self): pass

   
   
    def save_data(self): pass


def main():
    tracker =Expense_tracker()
    tracker.collect()
    tracker.display()

main()
