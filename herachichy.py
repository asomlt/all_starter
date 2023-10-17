class phone:
    a1=9
    def __init__(self):
        print("happuy")
class iphone(phone):
    b2=4
    def __init__(self):
        super().__init__()
        print("ji")
class smasumng(phone):
    c3=89
    def __init__(self):
        super().__init__()
        print("helllo")
c=smasumng(phone())
print(c)