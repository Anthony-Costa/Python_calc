#!/usr/bin/env/ python3

from tkinter import *
import operations
import operator
import math

root = Tk() #create window
root.resizable(width=0, height=0) #fixed window size
root.title("The ultimate calculator of the death. Not really.")

#output creation
output = ""
outnum = IntVar()
outnum.set("0")
num_temp = ""
ope_temp = ""
prev_num = ""
display = ""

def clear():
    global output
    output = "0"
    outnum.set(output)

def clear_temp():
    global output
    output = ""
    outnum.set(output)

def set_output(x):
    global ope_temp
    global output
    global num_temp
    global prev_num
    global display
    if display == True:
        clear_temp()
        display = False
    # if "." in num_temp: #pour éviter double virgule
    #     Button48.config(state=DISABLED)
    if output == "0" or "":
        output = str(x)
    else:
        output = str(output)+str(x)
    outnum.set(output)
    num_temp = output
    print("prev_num:", prev_num)
    print("num_temp:", num_temp)


def add(x, y):
    global output
    ops = {"+": operator.add}
    output = (ops["+"](int(x), int(y)))
    outnum.set(output)
    print(output)

def sub(x, y):
    global output
    ops = {"-": operator.sub}
    output = (ops["-"](int(x), int(y)))
    outnum.set(output)
    print(output)

def divide(x, y):
    global output
    ops = {"/": operator.truediv}
    output = (ops["/"](int(x), int(y)))
    outnum.set(output)
    print(output)

def multiply(x, y):
    global output
    ops = {"*": operator.mul}
    output = (ops["*"](int(x), int(y)))
    outnum.set(output)
    print(output)

def percent(x):
    global output
    ops = {"/": operator.truediv}
    output = (ops["/"](x.get(), 100))
    outnum.set(output)

def square(x):
    global output
    ops = {"x2": operator.mul}
    output = (ops["x2"](x.get(), x.get()))
    outnum.set(output)

def cubic(x):
    global output
    ops = {"x2": operator.mul}
    num_temp = (ops["x2"](x.get(), x.get()))
    output = (ops["x2"](num_temp, x.get()))
    outnum.set(output)

def opposite(y, x):
    global output
    output = -x.get()
    outnum.set(output)

def exponentiel(x):
    global output
    output = math.exp(x.get())
    outnum.set(output)

def log10(x):
    global output
    output = math.log10(x.get())
    outnum.set(output)

def racinecarre(x):
    global output
    output = math.sqrt(x.get())
    outnum.set(output)

def power(x, y):
    global output
    output = math.pow(int(x), int(y))
    outnum.set(output)

def ten_power(x):
    global output
    output = math.pow(10, x.get())
    outnum.set(output)

def sinus(x):
    global output
    output = math.sin(x.get())
    outnum.set(output)

def cosinus(x):
    global output
    output = math.cos(x.get())
    outnum.set(output)

def tangente(x):
    global output
    output = math.tan(x.get())
    outnum.set(output)

def sinush(x):
    global output
    output = math.sinh(x.get())
    outnum.set(output)

def cosinush(x):
    global output
    output = math.cosh(x.get())
    outnum.set(output)

def tangenteh(x):
    global output
    output = math.tanh(x.get())
    outnum.set(output)

def Radians(x):
    global output
    output = math.radians(x.get())
    outnum.set(output)

def Degrees(x):
    global output
    output = math.degrees(x.get())
    outnum.set(output)

def pi():
    global output
    output = math.pi
    outnum.set(output)

def mathconst():
    global output
    output = math.e
    outnum.set(output)

def stock_operator(x):
    global ope_temp
    global output
    global prev_num
    global display
    ope_temp = x
    prev_num = output
    print("output:", output)
    print("ope_temp:", ope_temp)
    display = True

def equal():
    global ope_temp
    if ope_temp == "+":
        add(prev_num, num_temp)
        ope_temp = ""
    elif ope_temp == "-":
        sub(prev_num, num_temp)
    elif ope_temp == "÷":
        divide(prev_num, num_temp)
    elif ope_temp == "*":
        multiply(prev_num, num_temp)
    elif ope_temp == "xy":
        power(prev_num, num_temp)
    else:
        print("else")

Output = Entry(root, textvariable = outnum, justify='right', font=("Inconsolata", 50), fg="white", bg="black").grid(row=0, column=0, columnspan=10)

#buttons creation
Button01 = Button(root, text="(", width=3, height=2, command=lambda: set_output("(")).grid(row=1, column=0)
Button02 = Button(root, text=")", width=3, height=2, command=lambda: set_output(")")).grid(row=1, column=1)
Button03 = Button(root, text="", width=3, height=2).grid(row=1, column=2)
Button04 = Button(root, text="", width=3, height=2).grid(row=1, column=3)
Button05 = Button(root, text="", width=3, height=2).grid(row=1, column=4)
Button06 = Button(root, text="", width=3, height=2).grid(row=1, column=5)
Button07 = Button(root, text="AC", width=3, height=2, command=lambda: clear()).grid(row=1, column=6)
Button08 = Button(root, text="+/-", width=3, height=2, command=lambda: opposite(0, outnum)).grid(row=1, column=7)
Button09 = Button(root, text="%", width=3, height=2, command=lambda: percent(outnum)).grid(row=1, column=8)
Button10 = Button(root, text="÷", width=3, height=2, command=lambda: stock_operator("÷")).grid(row=1, column=9)
Button11 = Button(root, text="", width=3, height=2).grid(row=2, column=0)
Button12 = Button(root, text="x²", width=3, height=2, command=lambda: square(outnum)).grid(row=2, column=1)
Button13 = Button(root, text="x³", width=3, height=2, command=lambda: cubic(outnum)).grid(row=2, column=2)
Button14 = Button(root, text="xy", width=3, height=2, command=lambda: stock_operator("xy")).grid(row=2, column=3)
Button15 = Button(root, text="ex", width=3, height=2, command=lambda: exponentiel(outnum)).grid(row=2, column=4)
Button16 = Button(root, text="10x", width=3, height=2, command=lambda: ten_power(outnum)).grid(row=2, column=5)
Button17 = Button(root, text="7", width=3, height=2, command=lambda: set_output(7)).grid(row=2, column=6)
Button18 = Button(root, text="8", width=3, height=2, command=lambda: set_output(8)).grid(row=2, column=7)
Button19 = Button(root, text="9", width=3, height=2, command=lambda: set_output(9)).grid(row=2, column=8)
Button20 = Button(root, text="×", width=3, height=2, command=lambda: stock_operator("*")).grid(row=2, column=9)
Button21 = Button(root, text="", width=3, height=2).grid(row=3, column=0)
Button22 = Button(root, text="²√x", width=3, height=2, command=lambda: racinecarre(outnum)).grid(row=3, column=1)
Button23 = Button(root, text="³√x", width=3, height=2).grid(row=3, column=2)
Button24 = Button(root, text="y√x", width=3, height=2).grid(row=3, column=3)
Button25 = Button(root, text="", width=3, height=2).grid(row=3, column=4)
Button26 = Button(root, text="log10", width=3, height=2, command=lambda: log10(outnum)).grid(row=3, column=5)
Button27 = Button(root, text="4", width=3, height=2, command=lambda: set_output(4)).grid(row=3, column=6)
Button28 = Button(root, text="5", width=3, height=2, command=lambda: set_output(5)).grid(row=3, column=7)
Button29 = Button(root, text="6", width=3, height=2, command=lambda: set_output(6)).grid(row=3, column=8)
Button30 = Button(root, text="-", width=3, height=2, command=lambda: stock_operator("-")).grid(row=3, column=9)
Button31 = Button(root, text="Deg", width=3, height=2, command=lambda: Degrees(outnum)).grid(row=4, column=0)
Button32 = Button(root, text="sin", width=3, height=2, command=lambda: sinus(outnum)).grid(row=4, column=1)
Button33 = Button(root, text="cos", width=3, height=2, command=lambda: cosinus(outnum)).grid(row=4, column=2)
Button34 = Button(root, text="tan", width=3, height=2, command=lambda: tangente(outnum)).grid(row=4, column=3)
Button35 = Button(root, text="e", width=3, height=2, command=lambda: mathconst()).grid(row=4, column=4)
Button36 = Button(root, text="", width=3, height=2, command=lambda: set_output("nobody uses that button")).grid(row=4, column=5)
Button37 = Button(root, text="1", width=3, height=2, command=lambda: set_output(1)).grid(row=4, column=6)
Button38 = Button(root, text="2", width=3, height=2, command=lambda: set_output(2)).grid(row=4, column=7)
Button39 = Button(root, text="3", width=3, height=2, command=lambda: set_output(3)).grid(row=4, column=8)
Button40 = Button(root, text="+", width=3, height=2, command=lambda: stock_operator("+")).grid(row=4, column=9)
Button41 = Button(root, text="Rad", width=3, height=2, command=lambda: Radians(outnum)).grid(row=5, column=0)
Button42 = Button(root, text="sinh", width=3, height=2, command=lambda: sinush(outnum)).grid(row=5, column=1)
Button43 = Button(root, text="cosh", width=3, height=2, command=lambda: cosinush(outnum)).grid(row=5, column=2)
Button44 = Button(root, text="tanh", width=3, height=2, command=lambda: tangenteh(outnum)).grid(row=5, column=3)
Button45 = Button(root, text="π", width=3, height=2, command=lambda: pi()).grid(row=5, column=4)
Button46 = Button(root, text="", width=3, height=2).grid(row=5, column=5)
Button47 = Button(root, text="0", width=3, height=2, command=lambda: set_output(0)).grid(row=5, column=7)
Button48 = Button(root, text=".", width=3, height=2, command=lambda: set_output(".")).grid(row=5, column=6)
Button49 = Button(root, text="=", width=3, height=2, command=lambda: equal()).grid(row=5, column=9)
Button50 = Button(root, text="00", width=3, height=2, command=lambda: set_output("00")).grid(row=5, column=8)
