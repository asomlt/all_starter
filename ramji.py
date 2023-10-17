class Atm:
    #contructor
    #magic method
    #_ _ method _ _
    #magic method are pre define
    #yeh  magic method ko object se call nhi karta
    # yu dont yh
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
        print(id(self))
    def menu(self):
        user_input=input(""" 
        Hello how would yoou like to proceed?
        1. enter 1 to create pin
        2. enter 2 to deposit
        3. enter 3 to withdraw
        4. enter 4 to check balance
        5. enter 5 to exits
""")
        if user_input == "1":
            self.create_pin()
           
        
        elif user_input == "2":
            self.deposit
            
        
        elif user_input == "3":
            self.withdraw()
            
        
        elif user_input == "4":
            self.check_balance()
            
        
        else:
            print("bye")

    def create_pin(self):
        self.pin=input("enter pin")
        print("Pin enter sucessfully")


    def deposit(self):
        temp=(input("enter your pin"))
        if temp==self.pin:
            amount=int(input("enter your amount"))
            self.balance=self.balance+amount
            print("deposit sucessfully")
        else:
            print("invalid pin")

    def withdraw(self):
        temp=(input("enter your pin"))
        if temp==self.pin:
            amount=int(input("enter your amt5"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("operation successful")
            else:
                print("insufficent balance")
        else:
            print("wrong pin")
            
    def check_balance(self):
        temp=(input("enter your pin"))
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")








