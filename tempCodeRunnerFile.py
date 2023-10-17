from tkinter import*
root=Tk()
root.geometry('420x280')
root.title('Calculator')
root.config(bg='white')
def show(op0):
    pass
roll=StringVar()
roll_e=Entry(root,bg='pink',textvariable=roll,justify='right',font=("Arial",30,"bold"),fg="white")
roll_e.place(x=0,y=0,width=420,height=50)


roll_9=Button(root,text='9',font=('Arial',25,'bold'),fg='white',bg='gray')
roll_9.place(x=5,y=65,width=100,height=40)
roll_9.configure(command=lambda:show('9'))
roll_8=Button(root,text='8',font=('Arial',25,'bold'),fg='white',bg='gray')
roll_8.place(x=105,y=65,width=100,height=40)
roll_8.configure(command=lambda:show('8'))
roll_7=Button(root,text='7',font=('Arial',25,'bold'),fg='white',bg='gray')
roll_7.place(x=205,y=65,width=100,height=40)
roll_7.configure(command=lambda:show('7'))
roll_6=Button(root,text='+',font=('Arial',25,'bold'),fg='white',bg='gray')
roll_6.place(x=305,y=65,width=100,height=40)
roll_6.configure(command=lambda:show('+'))



roll_5=Button(root,text='6',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_5.place(x=5,y=105,width=100,height=40)
roll_5.configure(command=lambda:show('6'))
roll_4=Button(root,text='5',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_4.place(x=105,y=105,width=100,height=40)
roll_4.configure(command=lambda:show('5'))
roll_3=Button(root,text='4',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_3.place(x=205,y=105,width=100,height=40)
roll_3.configure(command=lambda:show('4'))
roll_2=Button(root,text='-',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_2.place(x=305,y=105,width=100,height=40)
roll_2.configure(command=lambda:show("-"))



roll_5=Button(root,text='3',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_5.place(x=5,y=145,width=100,height=40)
roll_5.configure(command=lambda:show('3'))
roll_4=Button(root,text='2',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_4.place(x=105,y=145,width=100,height=40)
roll_4.configure(command=lambda:show('2'))
roll_3=Button(root,text='1',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_3.place(x=205,y=145,width=100,height=40)
roll_3.configure(command=lambda:show('1'))
roll_2=Button(root,text='*',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_2.place(x=305,y=145,width=100,height=40)
roll_2.configure(command=lambda:show('*'))


roll_5=Button(root,text='0',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_5.place(x=5,y=185,width=100,height=40)
roll_5.configure(command=lambda:show('0'))
roll_4=Button(root,text='C',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_4.place(x=105,y=185,width=100,height=40)
roll_4.configure(command=lambda:show('C'))
roll_3=Button(root,text='/',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_3.place(x=205,y=185,width=100,height=40)
roll_3.configure(command=lambda:show('/'))
roll_2=Button(root,text='=',font=('Arial',25,'bold'),fg='white',bg='grey')
roll_2.place(x=305,y=185,width=100,height=40)
roll_2.configure(command=lambda:show('='))



# roll_5=Button(root,text='9',font=('Arial',25,'bold'),fg='white',bg='grey')
# roll_5.place(x=5,y=105,width=100,height=40)
# roll_5.configure(command=lambda:show('9'))
# roll_4=Button(root,text='8',font=('Arial',25,'bold'),fg='white',bg='grey')
# roll_4.place(x=105,y=105,width=100,height=40)