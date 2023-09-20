# from tkinter import *
from tkinter import Tk, Entry, Button, StringVar

class Calculator():
        def __init__(Self,Gui):
                Gui.title("calculator")
                Gui.geometry("357x420+0+0")
                Gui.config(bg="grey")
                Gui.resizable(False,False)

                Self.equation=StringVar()
                Self.entry_value=''
                Entry(width=17,bg='grey',font=('Arial Bold',28),textvariable=Self.equation).place(x=0,y=0)


                Button(width=11,height=4,text='(',relief='flat',bg='white',command=lambda:Self.show('(')).place(x=0,y=50)
                Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:Self.show(')')).place(x=90,y=50)
                Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:Self.show('%')).place(x=180,y=50)
                Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:Self.show('1')).place(x=0,y=125)
                Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:Self.show('2')).place(x=90,y=125)
                Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:Self.show('3')).place(x=180,y=125)
                Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:Self.show('4')).place(x=0,y=200)
                Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:Self.show('5')).place(x=90,y=200)
                Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:Self.show('6')).place(x=180,y=200)
                Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:Self.show('7')).place(x=0,y=275)
                Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:Self.show('9')).place(x=175,y=275)
                Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:Self.show('8')).place(x=90,y=275)
                Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:Self.show('0')).place(x=90,y=350)
                Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:Self.show('.')).place(x=180,y=350)
                Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:Self.show('+')).place(x=270,y=275)
                Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:Self.show('-')).place(x=270,y=200)
                Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:Self.show('/')).place(x=270,y=50)
                Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:Self.show('*')).place(x=270,y=125)
                Button(width=11,height=4,text='=',relief='flat',bg='yellow',command=Self.solve).place(x=270,y=350)
                Button(width=11,height=4,text='C',relief='flat',bg='lightblue',command=Self.clear).place(x=0,y=350)
                


        def show(Self,value):
                Self.entry_value+=str(value)
                Self.equation.set(Self.entry_value)

        def clear(Self):
                Self.entry_value=''
                Self.equation.set(Self.entry_value)

        def solve(Self):
            result=eval(Self.entry_value)
            Self.equation.set(result)

root=Tk()
calculator=Calculator(root)
root.mainloop()

