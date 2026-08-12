import csv
from datetime import datetime as dt
import time

class Expense_tracker:
    
  def __init__(self):
    self.day =''
    self.month =''
    self.year =''
    self.amount=0
    self.category=""
    self.default_category='yaad nahi'
    self.description =""
    self.method=""

  def ask_input(self,message):
    value= input(message)
    return value

  def collect(self):
    while True:
      try:
        day = self.ask_input("Enter day (press enter for today): ")
        if day.strip()=="":
          self.day=dt.now().day
          break

        self.day = int(day)

        if not 1<= self.day <=31:
          print("!!!Invalid date!!!")
          time.sleep(2)
          continue
        
        break
        
      except ValueError:
        print("!!!Invalid Input!!!")
        time.sleep(2)
        print()
      
    while True:
      try:
        month = self.ask_input("Enter month (press enter for today): ")

        if month.strip() == "":
          self.month = dt.now().month
          break

        self.month =int(month)

        if not 1<= self.month <=12:
          print("!!!Invalid Month!!!")
          time.sleep(2)
          continue

        break
        
      except ValueError:
        print("!!!Invalid Input!!!")
        time.sleep()
        print()
            
    while True:
      try:
        year = self.ask_input("Enter year (press enter for today): ")

        if year.strip() =="":
          self.year = dt.now().year
          break

        self.year = int(year)

        if not dt.now().year>= self.year:
          print(f"!!!Year must not exceed {dt.now().year}!!!")
          time.sleep(2)
          continue
        break
        
      except ValueError:
        print("!!!Invalid Input!!!")
        time.sleep(2)
        print()   
            
    while True:
      try:
        self.amount = float(self.ask_input("Enter amount(rupee): "))
        if self.amount<0:
          print("Amount must be greater than 0")
          time.sleep(2)
          continue
        break
        
      except ValueError:
        print("!!!Invalid Input!!!")
        time.sleep(2)
        print()
    
    print()
    self.category = self.ask_input("(leave blank if not remember)\nWhat did you spend your money on: ")
    if self.category.strip() =="":
      self.category =self.default_category
      
    print()
    self.description = self.ask_input("(leave blank if don't want to)\nEnter short description: ")
    if self.description.strip() =="":
      self.description ="No description"
    
    print()
    self.method = self.ask_input("(leave blank if not sure)\n[upi, cash, card]\nEnter payment method: ")
    if self.method.strip() =="":
      self.method = "unknown"
    print('----------')


  def display(self):
    print()
    print("These are the details:")
    print(f"date(yyyy/mm/dd): {self.year}/{self.month:02}/{self.day:02}")
    print(f"amount: {self.amount}")
    print(f"money spent on: {self.category}")
    print(f"descripiton: {self.description}")
    print(f"payment method: {self.method}")
    print('----------')
    time.sleep(6)
    self.edit_opiton()
    
  
  def edit_opiton(self):
    self.choice= self.ask_input("Would you like to edit any field (yes/no): ")
      
    if self.choice.lower() =='yes':
      print("1. day")
      print("2. month")
      print("3. year")
      print("4. amount")
      print("5. category")
      print("6. description")
      print("7. payment method")
      print('----------')
      self.edit_input()
    
    elif self.choice.lower()=='no':
      return
      
    else:
      print()
      print("!!!Invalid Input!!!")
      print("Enter (yes/no)")
      time.sleep(2)
      self.edit_opiton()

  
  def edit_input(self):
    while True:
      self.ask_again =self.ask_input("Enter field number[1-7]: ")
      if self.ask_again in '1234567':
        break

      else:

        print("!!!INVALID INPUT!!!")
        print("Enter a value between [1-7]")
        time.sleep(2)
        print()
        continue

    if self.ask_again.strip()=='1':
      while True:
        try:
          day = self.ask_input("Enter day (press enter for today): ")
          if day.strip()=="":
            self.day=dt.now().day
            break
      
          self.day = int(day)

          if not 1<= self.day <=31:
            print("!!!Invalid date!!!")
            time.sleep(2)
            continue
          
          break
          
        except ValueError:
          print("!!!Invalid Input!!!")
          time.sleep(2)
          print()
      self.display()

    
    elif self.ask_again.strip()=='2':
      while True:
        try:
          month = self.ask_input("Enter month (press enter for today): ")
  
          if month.strip() == "":
            self.month = dt.now().month
            break
  
          self.month =int(month)
  
          if not 1<= self.month <=12:
            print("!!!Invalid Month!!!")
            time.sleep(2)
            continue
  
          break
          
        except ValueError:
          print("!!!Invalid Input!!!")
          time.sleep(2)
          print()
      
    elif self.ask_again.strip()=='3':
      while True:
        try:
          self.year = int(self.ask_input("Enter year: "))
          if not dt.now().year>= self.year:
            print(f"!!!Year must not exceed {dt.now().year}!!!")
            time.sleep(2)
            continue
          break
          
        except ValueError:
          print("!!!Invalid Input!!!")
          time.sleep(2)
          print()
      self.display()
      
    elif self.ask_again.strip()=='4':
      while True:
        try:
          year = self.ask_input("Enter year (press enter for today): ")
  
          if year.strip() =="":
            self.year = dt.now().year
            break
  
          self.year = int(year)
  
          if not dt.now().year>= self.year:
            print(f"!!!Year must not exceed {dt.now().year}!!!")
            time.sleep(2)
            continue
          break
          
        except ValueError:
          print("!!!Invalid Input!!!")
          time.sleep(2)
          print()   
      self.display()
        
    elif self.ask_again.strip()=='5':
      print()
      self.category = self.ask_input("(leave blank if not remember)\nWhat did you spend your money on: ")
      if self.category.strip() =="":
        self.category =self.default_category
      self.display()
      
    elif self.ask_again.strip()=='6':
      print()
      self.description = self.ask_input("(leave blank if don't want to)\nEnter short description: ")
      if self.description.strip() =="":
        self.description ="No description"
      self.display()
      
    elif self.ask_again.strip()=='7':
      print()
      self.method = self.ask_input("[upi, cash, card]\n(leave blank if not sure)\nEnter payment method: ")
      print()
      self.display()
        
    else:
      print("!!!Invalid Input!!!")
      time.sleep(2)
      print()

  def save_data(self):
    self.file = open("expense.csv",'a',newline="")
    self.afile = csv.writer(self.file)
    self.afile.writerow([f'{self.year}/{(self.month):02}/{(self.day):02}',self.amount,self.category.lower(),self.description.lower(),self.method.lower()])
    self.file.close()

  def ask_salary(self):
    while True:
      try:
        print(f"⚠️  WARNING: This will delete old balance.")
        time.sleep(5)
        salary = self.ask_input("Enter amount (press enter for cancel): ")
        if salary.strip() =="":
          return
        else:
          salary = float(salary)
          

        if salary<=0:
          print("!!!Salary cannot be below 0!!!")
          time.sleep(2)
          print()
          continue
        break
      
      except ValueError:
        print("!!!Invalid input!!!")
        time.sleep(2)
        print()
        
    
    with open('salary_file.csv','w',newline="") as salary_file:
      asalary_file= csv.writer(salary_file)
      asalary_file.writerow([salary])
      print("Balance updated")
      time.sleep(2)
    

  def add_amount(self):
    while True:
      try:
        self.add_amt = float(self.ask_input("Enter amount to add: "))
        if self.add_amt<=0:
          print("Amount must be greater than 0")
          time.sleep(2)
          continue

        print()
        print(f"⚠️  WARNING: This will add ₹{self.add_amt} to existing balance.")
        time.sleep(4)

        while True:
          confirm = input("Would you like to continue [yes/no]: ")
          if confirm.strip() =='yes':
            break

          elif confirm.strip()=='no':
            print("Amount not added.")
            time.sleep(2)
            return

          else:
            print()
            print("Enter [yes/no]")
            time.sleep(2)
            continue
        break
      
      except ValueError:
        print("!!!Invalid input!!!")
        time.sleep(2)
        print()

        
        
    with open('salary_file.csv','r') as abc:
      reader = csv.reader(abc)
      for row in reader:
        number =row[0]
        actual_int =float(number)
        actual_int+=self.add_amt

    with open("salary_file.csv",'w',newline="") as open_again:
      write_again = csv.writer(open_again)
      write_again.writerow([actual_int])
      print("Amount added successfully")
      time.sleep(2)

  def update_salary(self):
    with open("salary_file.csv", 'r') as for_update_salaryr:
      aupdate_salary = csv.reader(for_update_salaryr)
      for num in aupdate_salary:
        number1 =num[0]
        actual_num =float(number1)
        actual_num-=self.amount

    with open("salary_file.csv",'w',newline="") as for_update_salaryw:
      new_salary = csv.writer(for_update_salaryw)
      new_salary.writerow([actual_num])

  def show_salary(self):
    with open("salary_file.csv",'r') as for_show_salary:
      reading = for_show_salary.read()
      print(f"Your updated balance is ₹{reading}")

  def category_spending(self):
    self.category_dict ={}
    with open("expense.csv",'r',newline="") as for_category_spending:
      reading = csv.reader(for_category_spending)

      next(reading)

      for i in reading:
        cat=i[2]
        amount=i[1]

        if cat in self.category_dict:
          self.category_dict[cat]+=float(amount)

        else:
          self.category_dict[cat] = float(amount)

    for category, amt in self.category_dict.items():
      print(category,amt)

  def summary_report(self):
    print()
    print(f"========================\n")
    self.show_salary()
    print(f"Here are your spendings category wise:")
    self.category_spending()
    print()
    print(f"Total money you've spent: {sum(self.category_dict.values())}")
    print(f"========================\n")
    print()
    time.sleep(10)
   
  def add_expense(self):
    self.collect()
    self.display()
    self.save_data()
    self.update_salary()
    print("Details saved.")
    time.sleep(2)

  def clear_expense(self):
    clear_data = self.ask_input("Are you sure you want to remove all data [yes/no]: ")

    if clear_data.lower().strip() =="yes":
      print()
      print("⚠️  WARNING: This will permanently delete all your tracking data.")
      time.sleep(5)
      clear_data_again = self.ask_input("Are you sure you want to proceed? (yes/no): ")

      if clear_data_again.lower().strip() =="yes":
        with open('expense.csv',"w",newline="") as  for_clear_expense:
          write = csv.writer(for_clear_expense)
          write.writerow(['date','amount','category','description','payment_method'])
        print("Data deleted successfully.")
        time.sleep()
        print()

      elif clear_data.lower().strip()=='no':
        print("Data not deleted.")
        time.sleep(2)
        print()
        return

      else:
        print()
        print("!!!ENTER 'yes'/'no' only!!!")
        time.sleep(2)
        print()
        self.clear_expense()

    elif clear_data.lower().strip()=='no':
      print("Data not deleted.")
      time.sleep(2)
      print()
      return

    else:
      print()
      print("!!!ENTER 'yes'/'no' only!!!")
      time.sleep(2)
      print()
      self.clear_expense()

def start_menu():
  print()
  print("1. Update balance (it reset the previous balance amount)")
  print("2. Add amount to existing balance")
  print("3. Add expense")
  print("4. Show summary")
  print("5. Clear expense data")
  print("6. Exit")
  ask = input("Choose action [1-6]: ")
  print()
  return ask

def main():
  while True:
    tracker =Expense_tracker()
    choice = start_menu()
    if choice =="1":
      tracker.ask_salary()
      print()

    elif choice=='2':
      tracker.add_amount()
      print()

    elif choice=='3':
      tracker.add_expense()
      print()

    elif choice=='4':
      tracker.summary_report()

    elif choice=='5':
      tracker.clear_expense()
    
    elif choice=='6':
      print("!!!Program ended!!!")
      break

    else:
      print("Enter value between [1-6]")
      time.sleep(2)
      print()


main()