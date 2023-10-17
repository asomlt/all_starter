class phone:
    def __init__(self,price,brand,camera):
       
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying phone")
class Smartphone(phone):
    def buy(self):
        super().buy()
        print("buying Smartphone")
        
