from tkinter import *
def click(number):
    global value
    value=value+str(number)
    scvalue.set(value)
def clearbutton():
    global value
    value=""
    scvalue.set(" ")
def equalbutton():
    global value
    try:
      result=str(eval(value))

    except:
        scvalue.set("error")
    scvalue.set(result)

root=Tk()
root.geometry("360x370")
root.title("calculator")
scvalue=StringVar()
value=""
screen=Entry(root,textvar=scvalue,font="lucida 20 bold",bd=20,bg="powder blue",justify="right")
screen.grid(row=0,columnspan=4)
#row1
b7=Button(root,text="7",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(7))
b7.grid(row=1,column=0)
b8=Button(root,text="8",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(8))
b8.grid(row=1,column=1)
b9=Button(root,text="9",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(9))
b9.grid(row=1,column=2)
b_add=Button(root,text="+",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click("+"))
b_add.grid(row=1,column=3)
#row2
b4=Button(root,text="4",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(6))
b6.grid(row=2,column=2)
b_mul=Button(root,text="*",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click("*"))
b_mul.grid(row=2,column=3)
#row3
b1=Button(root,text="1",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(1))
b1.grid(row=3,column=0)
b2=Button(root,text="2",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(2))
b2.grid(row=3,column=1)
b3=Button(root,text="3",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(3))
b3.grid(row=3,column=2)
b_sub=Button(root,text="-",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click("-"))
b_sub.grid(row=3,column=3)
#row4
bc=Button(root,text="C",font="lucida 12 bold",bd=12,height=2,width=6,command=clearbutton)
bc.grid(row=4,column=0)
b0=Button(root,text="0",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click(0))
b0.grid(row=4,column=1)
b_div=Button(root,text="÷",font="lucida 12 bold",bd=12,height=2,width=6,command=lambda :click("/"))
b_div.grid(row=4,column=2)
b_equal=Button(root,text="=",font="lucida 12 bold",bd=12,height=2,width=6,command=equalbutton)
b_equal.grid(row=4,column=3)
root.mainloop()