from tkinter import *
from tkinter import messagebox

equation=""

#functions for calculator functionality
def show(value):
    global equation
    equation +=value
    display.config(text=equation)

def clear():
    global equation
    equation = ""
    display.config(text=equation)

def calculate():
    global equation
    result=""

    if equation !=result:
        try:
            result = eval(equation)
        except:
            result = messagebox.showerror("Calculator app","Error")
            equation = ""
        display.config(text=result)



win = Tk()
win.title("Calculator App")
win.geometry("400x285")
win.config(bg='black')
#Calculator app features
display = Label(win,bg='cyan',fg="black",font=("britannic bold",20),width=350,height=4)
display.pack()

but0= Button(win,text="AC",bg="red",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :clear())
but0.place(x=3,y=130)
but1= Button(win,text="%",bg="blue",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("%"))
but1.place(x=80,y=130)
but2= Button(win,text="/",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("/"))
but2.place(x=160,y=130)
but3= Button(win,text="X",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("x"))
but3.place(x=240,y=130)
but4= Button(win,text="-",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("-"))
but4.place(x=320,y=130)

but5= Button(win,text="9",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
             command=lambda :show("9"))
but5.place(x=3,y=160)
but6= Button(win,text="8",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
             command=lambda :show("8"))
but6.place(x=80,y=160)
but7= Button(win,text="7",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
             command=lambda :show("7"))
but7.place(x=160,y=160)
but8= Button(win,text="6",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
             command=lambda :show("6"))
but8.place(x=240,y=160)
but9= Button(win,text="+",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
             command=lambda :show("+"))
but9.place(x=320,y=160)

but10= Button(win,text="5",bg="black",fg="white",font=('arial bold',10),width=8,bd=3,
              command=lambda :show("5"))
but10.place(x=3,y=190)
but11=Button(win,text="4",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("4"))
but11.place(x=80,y=190)
but12=Button(win,text="3",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("3"))
but12.place(x=160,y=190)
but13=Button(win,text="2",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("2"))
but13.place(x=240,y=190)
but14=Button(win,text="1",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("1"))
but14.place(x=320,y=190)

but16=Button(win,text="0",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("0"))
but16.place(x=3,y=220)
but16=Button(win,text="sin",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("sin"))
but16.place(x=80,y=220)
but16=Button(win,text="cos",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("cos"))
but16.place(x=160,y=220)
but16=Button(win,text="tan",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("tan"))
but16.place(x=240,y=220)
but16=Button(win,text="^",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("^"))
but16.place(x=320,y=220)

but17=Button(win,text="log",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("log"))
but17.place(x=3,y=250)
but17=Button(win,text="()",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("()"))
but17.place(x=80,y=250)
but17=Button(win,text="pi",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("pi"))
but17.place(x=160,y=250)
but17=Button(win,text="sqr",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :show("sqr"))
but17.place(x=240,y=250)
but17=Button(win,text="=",bg="black",fg="white",font=("arial bold",10),width=8,bd=3,
             command=lambda :calculate())
but17.place(x=320,y=250)



win.mainloop()