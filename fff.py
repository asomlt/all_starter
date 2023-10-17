#oops

class IRCTC:
    def __init__(self):
        
        user_input= input(""" How would you like to proceed?
        1.Enter 1 to check  live train status
        2.Enter 2 to check  live pnr status
        3.Enter 3 to check  live schedule """)
        if user_input == "1":
           print("live train status ")
        elif user_input == "2":
            print("live pnr status ")
        else:
            print("kk")
    def train_schedule(self):
        train_no = input("Enter the train number")
        self.fetch_data(train_no)
    
