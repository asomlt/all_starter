# # #oops

# # class IRCTC:
# #     def __init__(self):
        
# #         user_input= input(""" How would you like to proceed?
# #         1.Enter 1 to check  live train status
# #         2.Enter 2 to check  live pnr status
# #         3.Enter 3 to check  live schedule """)
# #         if user_input == "1":
# #            print("live train status ")
# #         elif user_input == "2":
# #             print("live pnr status ")
# #         else:
# #             print("kk")
# #     def train_schedule(self):
# #         train_no = input("Enter the train number")
# #         self.fetch_data(train_no)
    
# # #  #
# # class Fraction:
# #     def __init__(self,n,d):
# #         self.num=n
# #         self.den=d
# #     def __str__(self):
# #         return " hello {}/{}".format(self.num,self.den)
# #     def __add__(self,other):
# #         temp_num=self.num*other.den + other.num*self.den
# #         temp_den=self.den *other.den

# #         return "{}/{}".format(temp_num,temp_den)
    
# # class ad():
# #     def area(self,a,b):
# #         return a*b*3.14
# #     def sq(self,a):
# #         return a*a
    
# # a=ad()
# # print(a.area(5,6))
# # print(a.sq(5))

# #getter/ascceser
# #setter/mutator

# # class hid():
# #     def __init__(self,n,cl):
# #         self.__name=n
# #         self.__clas=cl
# #     def show(self):
# #         return self.__name, "hloo ram ji",self.__clas
# #     def chg(self,p,f):
# #         self.__name=p
# #         self.__clas=f
# #         print("changee")

# # a=hid("ram",14)

# # print(a.show())

# # (a.chg("ramram",15))
# # print(a.show())


# # class a():
# #     a=7
# #     print("a")
# # class b(a):
# #     b=5
# #     print("aaaa")
# # class c(a):
# #     c=5
# #     print("aaaa")
# # class d(b,c):
# #     a=55
# #     d=78
# #     print("her is this")
    
# # a=d()
# # print(a.a)

# # class wrk():
# #     a=589
# #     @classmethod
# #     def shw(cls):
# #         print("hii")
# #     def ck(cls,a,b):
# #         return cls.a+a+b
    
# #     @staticmethod
# #     def howe():
# #         print("ram ram ram")
# # a=wrk()
# # print(a.ck(5,6))
# # a.howe()
# # a.a=855
# # print(a.a)
# # b=wrk()
# # print(b.a)
# g=(i for i in range(50))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in g:
#     print(i)
# li=[i for i in range(50)  if i%2==0 ]
# print(li)
# lii=["even" if i%2==0 else "odd" for i in range(10)]
# print(lii)
from tkinter import*
root=Tk()
root.geometry('420x280')
root.resizable(True,True)
root.title("calculator")
root.config(bg='white')
roll=StringVar()



roll_e=Entry(root,textvariable=roll,justify='right',font=("Areial",30,"bold"),fg='red',bg="pink")
roll_e.place(x=0,y=0,width=420,height=65)

def show(e):
    roll.set(roll.get()+e)
    # pass
    
def equal():
    exp=roll.get()
    roll.set(eval(exp))
    #here main function is eval =evaluation of an expression it evaaluate your expression
def clr():
    roll.set("")

roll_1=Button(root,text="1",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='white')
roll_1.place(x=5,y=65,width=100,height=50)
roll_1.configure(command=lambda:show("1"))
roll_2=Button(root,text="2",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='white')
roll_2.place(x=110,y=65,width=100,height=50)
roll_2.configure(command=lambda:show("2"))
roll_3=Button(root,text="3",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='white')
roll_3.place(x=210,y=65,width=100,height=50) 
roll_3.configure(command=lambda:show("3"))
roll_4=Button(root,text="+",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='white')
roll_4.place(x=315,y=65,width=100,height=50)

roll_4.configure(command=lambda:show("+"))
roll_5=Button(root,text="4",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_5.place(x=5,y=115,width=100,height=50)
roll_5.configure(command=lambda:show("4"))
roll_6=Button(root,text="5",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_6.place(x=110,y=115,width=100,height=50)
roll_6.configure(command=lambda:show("5"))
roll_7=Button(root,text="6",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_7.place(x=210,y=115,width=100,height=50) 
roll_7.configure(command=lambda:show("6"))
roll_8=Button(root,text="-",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_8.place(x=315,y=115,width=100,height=50)

roll_8.configure(command=lambda:show("-"))

roll_9=Button(root,text="7",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_9.place(x=5,y=165,width=100,height=50)
roll_9.configure(command=lambda:show("7"))
roll_10=Button(root,text="8",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_10.place(x=110,y=165,width=100,height=50)
roll_10.configure(command=lambda:show("8"))
roll_11=Button(root,text="9",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_11.place(x=210,y=165,width=100,height=50)
roll_11.configure(command=lambda:show("9"))
roll_12=Button(root,text="*",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_12.place(x=315,y=165,width=100,height=50)
roll_12.configure(command=lambda:show("*"))
roll_13=Button(root,text="0",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_13.place(x=5,y=215,width=100,height=50)
roll_13.configure(command=lambda:show("0"))
roll_10=Button(root,text="/",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_10.place(x=110,y=215,width=100,height=50)
roll_10.configure(command=lambda:show("/"))
roll_11=Button(root,text="C",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_11.place(x=210,y=215,width=100,height=50) 
roll_11.configure(command=clr)
roll_12=Button(root,text="=",font=("Areial",30,"bold"),fg='red',bg='yellow',activebackground="blue",activeforeground='black')
roll_12.place(x=315,y=215,width=100,height=50)
roll_12.configure(command=equal)


# print(roll.get())
root.mainloop() 
