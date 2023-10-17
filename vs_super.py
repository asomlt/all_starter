class atm:
    arpit=5655666666665656565655555555
    def __init__(self):
        print(id(self))
        self.__a=8
        self.__b=9
        self.__c=0
    def sum_work(self):
        return self.__a+self.__b+self.__c
    def changer_work(self,ws,we):
        self.__a=ws
        self.__b=we
    def shower_work(self):
        return self.__a,self.__b,self.__c

    @staticmethod
    def ram():
        print("jai shree ram")
