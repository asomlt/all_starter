from tkinter import*

root=Tk()
def select():
    x=op.get()
    print(x)
def show():
    a=rm.get()

op=IntVar()
rm=StringVar()
en1=Entry(root,textvariable=rm,bg="pink")
en1.pack()
rad_male=Radiobutton(root,text="male",font=("Arial,"),value=0,variable=op,command=select)
rad_male.place(x=35,y=60)

rad_female=Radiobutton(root,text="female",font=("Arial,"),value=1,variable=op,command=select)
rad_female.place(x=150,y=60)
root.mainloop()