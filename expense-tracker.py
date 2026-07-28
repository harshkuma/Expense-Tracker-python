import csv
class Expense_tracker:
    def __init__(self):
        self.day =''
        self.month =''
        self.year =''
        self.amount=0
        self.categories=['food','travel','shopping','bills','entertainment', 'miscellaneous']
        self.category=""
        self.default_description='miscellaneous'
        self.description =""
        self.methods=['cash','upi','card','gpay']
        self.method=""

    def ask_input(self,message):
        value= input(message)
        return value
   
    def collect(self):
        self.day = int(self.ask_input("Enter day: "))
        self.month = int(self.ask_input("Enter month: "))
        self.year = int(self.ask_input("Enter year: "))
        self.amount = int(self.ask_input("Enter amount(rupee): "))
        self.category = self.ask_input("Enter category: ")
        self.description = self.ask_input("Enter short description: ")
        self.method = self.ask_input("Enter payment method: ")
        print('----------')
   

    def display(self):
        print("These are the details:")
        print(f"date(intyyyy/mm/dd): {self.year}/{self.month:02}/{self.day:02}")
        print(f"amount: {self.amount}")
        print(f"category: {self.category}")
        print(f"descripiton: {self.description}")
        print(f"payment method: {self.method}")
        print('----------')
        self.edit_opiton()
       
   
    def edit_opiton(self):
        self.choice= self.ask_input("Would you like to edit any field (y/n): ")
       
        if self.choice.lower() =='y':
            print("1. day")
            print("2. month")
            print("3. year")
            print("4. amount")
            print("5. category")
            print("6. description")
            print("7. payment method")
            print('----------')
            self.edit_input()
      
        elif self.choice.lower()=='n':
            return
       
        else:
            print()
            print("!!!Invalid Input!!!")
            self.edit_opiton()

   
   
    def edit_input(self):
      self.ask_again =self.ask_input("Enter field number[1-7]: ")
      
      if int(self.ask_again)==1:
        self.day = self.ask_input("Enter day: ")
        print()
        self.display()
      
      elif int(self.ask_again)==2:
        self.month = self.ask_input("Enter month: ")
        print()
        self.display()
        
      elif int(self.ask_again)==3:
        self.year = self.ask_input("Enter year: ")
        print()
        self.display()
        
      elif int(self.ask_again)==4:
        self.amount= self.ask_input("Enter amount(rupee): ")
        print()
        self.display()
          
      elif int(self.ask_again)==5:
        self.category= self.ask_input("Enter category: ")
        print()
        self.display()
        
      elif int(self.ask_again)==6:
        self.description =self.ask_input("Enter short description: ")
        print()
        self.display()
        
      elif int(self.ask_again)==7:
        self.method= self.ask_input("Enter payment method: ")
        print()
        self.display()
          
      else:
        
        print("!!!Invalid Input!!!")
        print()
        self.edit_input()
  
    def save_data(self):
      self.file = open("expense.csv",'a',newline="")
      self.afile = csv.writer(self.file)
      self.afile.writerow([f'{self.year}/{(self.month):02}/{(self.day):02}',self.amount,self.category,self.description,self.method])
      self.file.close()


def main():
    tracker =Expense_tracker()
    tracker.collect()
    tracker.display()
    tracker.save_data()

main()