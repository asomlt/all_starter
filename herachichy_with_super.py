# class umeshji:
#     def __init__(self):
#         print("happy")
# class chirag(umeshji):
#     def __init__(self):
#         super().__init__()
#         print("ram ji ki kripa")
# class abhinav(umeshji):
#     def __init__(self):
#         super().__init__()
#         print("happy to be hear")
# class om(umeshji):
#     def __init__(self):
#         super().__init__()
#         print("lover")

# a=om()
class shiv():
    s=100
   
    def __init__(self):
        
        print("shiv")

class ram(shiv):
    r=57
    def __init__(self):
        super().__init__()
        print("ram")

class hanuman(shiv):
    h=57
    def __init__(self):
        super().__init__()
        print("hanuma")
        
class krishna(ram,hanuman):
    a=55
    def __init__(self):
        super().__init__()
        print("krishna")

ap=krishna()
