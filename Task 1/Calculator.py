from tkinter import *
from tkinter import messagebox
import math
root =Tk()
root.geometry("450x450")
root.title("Calculator")
root.configure(bg="white")
mylabel=Label(root,text="CALCULATOR",font=("arial",20,"bold"))
mylabel.pack()
myframe=LabelFrame(root)
mydisplay=Entry(root,width=20,borderwidth=5,font=("arial",25),bg="white")
mydisplay.pack()
def one():
    n=1
    mydisplay.insert(10,'1')
def two():
    n=2
    mydisplay.insert(10,'2')
def three():
    n=3
    mydisplay.insert(10,'3')
def four():
    n=4
    mydisplay.insert(10,'4')
def five():
    n=5
    mydisplay.insert(10,'5')
def six():
    n=6
    mydisplay.insert(10,'6')
def seven():
    n=7
    mydisplay.insert(10,'7')
def eight():
    n=8
    mydisplay.insert(10,'8')
def nine():
    n=9
    mydisplay.insert(10,'9')
def zero():
    n=0
    mydisplay.insert(10,'0')
def add():
    mydisplay.insert(10,"+")
def subtract():
    mydisplay.insert(10,"-")
def multiply():
    mydisplay.insert(10,"*")
def divide():
    mydisplay.insert(10,"/")
def dot():
    mydisplay.insert(10,".")
def power():
    mydisplay.insert(10,"")
def sq_root():
    mydisplay.insert(10,"(1/2)")
def square():
    mydisplay.insert(10,"**2")
def clear():
    mydisplay.delete(0,END)
def result():
    try:
        r=eval(mydisplay.get())
        mydisplay.delete(0,END)
        mydisplay.insert(10,r)
    except SyntaxError:
        mydisplay.delete(0,END)
        mydisplay.insert(10,"INVALID")
button1=Button(myframe,text="9",width=8,height=4,command=nine,bg="azure",font=("arial",10,"bold"))
button1.grid(row=1,column=1)
button2=Button(myframe,text="8",width=8,height=4,command=eight,bg="azure",font=("arial",10,"bold"))
button2.grid(row=1,column=2)
button3=Button(myframe,text="7",width=8,height=4,command=seven,bg="azure",font=("arial",10,"bold"))
button3.grid(row=1,column=3)
button4=Button(myframe,text="6",width=8,height=4,command=six,bg="azure",font=("arial",10,"bold"))
button4.grid(row=2,column=1)
button5=Button(myframe,text="5",width=8,height=4,command=five,bg="azure",font=("arial",10,"bold"))
button5.grid(row=2,column=2)
button6=Button(myframe,text="4",width=8,height=4,command=four,bg="azure",font=("arial",10,"bold"))
button6.grid(row=2,column=3)
button7=Button(myframe,text="3",width=8,height=4,command=three,bg="azure",font=("arial",10,"bold"))
button7.grid(row=3,column=1)
button8=Button(myframe,text="2",width=8,height=4,command=two,bg="azure",font=("arial",10,"bold"))
button8.grid(row=3,column=2)
button9=Button(myframe,text="1",width=8,height=4,command=one,bg="azure",font=("arial",10,"bold"))
button9.grid(row=3,column=3)
button10=Button(myframe,text="0",width=8,height=4,command=zero,bg="azure",font=("arial",10,"bold"))
button10.grid(row=4,column=1)
button11=Button(myframe,text=".",width=8,height=4,command=dot,bg="azure",font=("arial",10,"bold"))
button11.grid(row=4,column=2)
button12=Button(myframe,text="=",width=8,height=4,command=result,bg="thistle",font=("arial",10,"bold"))
button12.grid(row=4,column=4)
button13=Button(myframe,text="/",width=8,height=4,command=divide,bg="linen",font=("arial",10,"bold"))
button13.grid(row=2,column=5)
button14=Button(myframe,text="+",width=8,height=4,command=add,bg="linen",font=("arial",10,"bold"))
button14.grid(row=3,column=4)
button15=Button(myframe,text="-",width=8,height=4,command=subtract,bg="linen",font=("arial",10,"bold"))
button15.grid(row=2,column=4)
button16=Button(myframe,text="x",width=8,height=4,command=multiply,bg="linen",font=("arial",10,"bold"))
button16.grid(row=1,column=4)
button17=Button(myframe,text="^",width=8,height=4,command=power,bg="linen",font=("arial",10,"bold"))
button17.grid(row=1,column=5)
button18=Button(myframe,text="AC",width=8,height=4,command=clear,bg="thistle",font=("arial",10,"bold"))
button18.grid(row=4,column=5)
button19=Button(myframe,text="root",width=8,height=4,command=sq_root,bg="linen",font=("arial",10,"bold"))
button19.grid(row=4,column=3)
button20=Button(myframe,text="x^2",width=8,height=4,command=square,bg="linen",font=("arial",10,"bold"))
button20.grid(row=3,column=5)
myframe.pack()
root.mainloop()
