
#Dice Roller Project using Python GUI
from tkinter import *

die = {
    1:'\u2680',
    2:'\u2681',
    3:'\u2682',
    4:'\u2683',
    5:'\u2684',
    6:'\u2685',

}

App = Tk()
App.title('Dice')

dice = Label(App,text=die[1],font=('Times',100),foreground='black',width=2,height=2)
dice.grid(row=0,column=0,padx=25,pady=5)

def roll():
    from random import randint
    i=randint(1,6)
    msg= Label(App,text=die[i],font=('Times',100),foreground='black',)
    msg.grid(row=0, column=0, padx=25, pady=5)


rollB=Button(App,text='Roll',command=roll,padx=15,pady=5)
rollB.grid(row=1,column=1)
rollB.place(relx=0.5,rely=1.0,anchor=S)
App.mainloop()