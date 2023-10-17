class const_details:
    def __init__(self):
        self.name_proj = ""
        self.amt= 0
        self.date = ""
        self.addres=""
        self.filecharge=50000
        self.a=0
        self.b=0
    def proj_namer(self):
        name=input("enter project ")
        addres=input("address")
        self.name_proj=name
        self.addres=addres
        print("we take this work on ",self.date,"in the addres",self.addres,"with cotation amount",self.amt)
    def proj_amt(self):
        amt=int(input("Amount finale without tax"))
        other_tax=int(input("amount of tax final on other think"))
        self.amt=self.amt+amt
        final_amt=(self.amt*18)/100+self.filecharge+ other_tax
    def __add__(self,a,b):
        return self.a+self.ab
        

