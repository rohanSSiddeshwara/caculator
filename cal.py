from tkinter import *
import tkinter.font as font
import math

root=Tk()
root.title("calculator")
root.configure(bg="black")
root.geometry("548x410")

# define font
myFont = font.Font(family='Helvetica',size=15)

input=Entry(root,width=40,borderwidth=1,bd=0,font=("Helvetica",18),justify="right",highlightbackground="white",bg="#191a1c",fg='white')
input.grid(row=0,column=0,columnspan=5,padx=10,pady=10,ipady=10)

ne=font.Font(family="Times", size=20,weight="bold")



def button_click(t):
    c=str(input.get())
    input.delete(0,END)
    input.insert(0,c+str(t))

def button_clear():
    input.delete(0,END)
def button_add():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='+'
def button_sub():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='-'
def button_mul():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='*'
def button_div():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='/'
def button_per():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='%'
def button_pow():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='po'
def button_root():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='sqrt'
def button_fact():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='fact'
def button_log10():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='log10'
def button_tan():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='tan'
def button_sin():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='sin'
def button_cos():
    global x_g
    global o_G
    x_g=float(input.get())
    input.delete(0,END)
    o_G='cos'
def equal_button():
    if input.get()=='':
        y=0
    else:
        y=float(input.get())

    input.delete(0,END)
    if o_G=='+':
        input.insert(0,str(x_g+y))
    elif o_G=='-':
        input.insert(0,str(x_g-y))
    elif o_G=='*':
        input.insert(0,str(x_g*y))
    elif o_G=='/':
        if y==0:
            input.insert(0,"can't divide by zero")
        else:
            input.insert(0,str(x_g/y))
    elif o_G=='%':
        input.insert(0,str(x_g/y*100))
    elif o_G=='po':
        t=math.pow(x_g,y)
        input.insert(0,str(t))
    elif o_G=='sqrt':
        t=math.sqrt(x_g)
        input.insert(0,str(t))
    elif o_G=="fact":
        t=math.factorial(x_g)
        input.insert(0,str(t))
    elif o_G=="log10":
        t=math.log10(x_g)
        input.insert(0,str(t))
    elif o_G=="tan":
        t=math.degrees(math.tan(x_g))
        input.insert(0,str(t))
    elif o_G=="sin":
        t=math.degrees(math.sin(x_g))
        input.insert(0,str(t))
    elif o_G=="cos":
        t=math.degrees(math.cos(x_g))
        input.insert(0,str(t))

button_1=Button(root,text="1",command=lambda:button_click(1),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_2=Button(root,text="2",command=lambda:button_click(2),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_3=Button(root,text="3",command=lambda:button_click(3),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_4=Button(root,text="4",command=lambda:button_click(4),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_5=Button(root,text="5",command=lambda:button_click(5),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_6=Button(root,text="6",command=lambda:button_click(6),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_7=Button(root,text="7",command=lambda:button_click(7),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_8=Button(root,text="8",command=lambda:button_click(8),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_0=Button(root,text="0",command=lambda:button_click(0),padx=26,pady=10,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_9=Button(root,text="9",command=lambda:button_click(9),pady=10,padx=26,bg='black',fg='white',relief='groove',borderwidth=0,font=("Helvetica",15,'bold'))
button_add=Button(root,text="+",command=button_add,pady=0,padx=22,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",18,'bold'))
button_sub=Button(root,text="-",command=button_sub,pady=0,padx=25,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",18,'bold'))
button_multiply=Button(root,text="*",command=button_mul,pady=0,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",18,'bold'))

button_div=Button(root,text="/",command=button_div,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_per=Button(root,text="%",command=button_per,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_pow=Button(root,text="power",command=button_pow,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_sqrt=Button(root,text="x^1/2",command=button_root,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))

button_fact=Button(root,text="X!",command=button_fact,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_log10=Button(root,text="log10",command=button_log10,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_tan=Button(root,text="tan",command=button_tan,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_sin=Button(root,text="sin",command=button_sin,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))
button_cos=Button(root,text="cos",command=button_cos,pady=24,padx=24,bg='black',fg='#ff6600',relief='groove',borderwidth=0,font=("Helvetica",9))

button_equal=Button(root,text="=",command=equal_button,padx=53,bg='#ff6600',fg='white',relief='groove',borderwidth=0,font=("Helvetica",18))
button_clear=Button(root,text="CL",command=button_clear,padx=18,pady=10,bg='black',fg='red',relief='groove',borderwidth=0,font=("Helvetica",18))


button_1["font"]=myFont
button_2["font"]=myFont
button_3["font"]=myFont
button_4["font"]=myFont
button_5["font"]=myFont
button_6["font"]=myFont
button_7["font"]=myFont
button_8["font"]=myFont
button_9["font"]=myFont
button_0["font"]=myFont
button_add["font"]=ne
button_multiply["font"]=ne
button_sub["font"]=ne
button_equal["font"]=ne
button_clear["font"]=myFont
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=2,column=3)
button_sub.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=1,column=3)

button_div.grid(row=5,column=0)
button_per.grid(row=5,column=1)
button_sqrt.grid(row=5,column=2)
button_pow.grid(row=5,column=3)

button_log10.grid(row=1,column=4)
button_tan.grid(row=2,column=4)
button_sin.grid(row=3,column=4)
button_cos.grid(row=4,column=4)
button_fact.grid(row=5,column=4)
root.mainloop()
