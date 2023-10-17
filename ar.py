class const_details:
    def __init__(self) -> None:
        self.name_proj = ""
        self.amt= 0
        # self.date = input("date")
        # self.addres=""
        # self.___filecharge=50000
        # self.proj_namer()
        # self.proj_amt()
    def proj_amt(self):
        
        other_tax=int(input("amount of tax final on other think"))
        
        self.final_amt=(self.amt*18)/100+self._const_details__filecharge+ other_tax
        print(self.final_amt)
    
    def proj_namer(self):
        name=input("enter project ")
        addres=input("address")
        amt=int(input("Amount finale without tax"))
        self.amt=self.amt+amt
        self.name_proj=name
        self.addres=addres
        print("we take this work on ",self.date,"in the addres",self.addres,"with cotation amount",self.amt)
   
