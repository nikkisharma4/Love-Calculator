from tkinter import *
from tkinter.messagebox import showinfo
from random import randint


love= Tk()
love.title('Love calculator')
love.configure(bg='pink')
love.geometry('370x360')
count=0
def click():
    number = randint(60,100)
    showinfo("LOVE BIRDS",number)

malename= Label(love, text='Enter your partner name :', bg='pink').place(x=40, y=40,)
maleenter = Entry(love, font=('arial', 10,'italic')).place(x=180, y=40)

femalename= Label(love, text='Enter your name :', bg='pink').place(x=40, y=80,)
femaleenter = Entry(love, font=('arial', 10,'italic')).place(x=180, y=80)

btn = Button(love, text='Check it now!', bd='5',bg='red', command= lambda:click()).place(x=150, y=120)

love.mainloop()