from tkinter import *
from tkinter import messagebox
import math_calc


def clear():
    """Clear entry"""
    calc.delete(0, END)
    calc.insert(0, 0)


def clear_char():
    """Clear char entry"""
    len_v = len(calc.get())
    calc.delete(len_v - 1, END)



def to_square():
    """Calculates the square"""
    value = math_calc.calc_square(float(eval(calc.get())))
    calc.delete(0, END)
    calc.insert(0, value)


def to_cube():
    """Calculates the cube"""
    value = math_calc.calc_cube(float(eval(calc.get())))
    calc.delete(0, END)
    calc.insert(0, value)


def add_digit(digit):
    """Adding a digit"""
    value = calc.get()

    if value[0] == '0':
        value = value[1:]
    
    calc.delete(0, END)
    calc.insert(0, value + digit)


def add_operation(oper):
    """Adding a oparation"""
    value = calc.get()


    if value[-1] in '-/+*':
        value = value[:-1]

    elif '+' or '-' or '/' or '*' in value:
        calculate()
        value = calc.get()
    
    calc.delete(0, END)
    calc.insert(0, value + oper)


def calculate() -> int:
    """Example Solution"""
    value = calc.get()

    if value[-1] in '+-/*':
        value = value + value[:-1]
    
    calc.delete(0, END)

    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        calc.delete(0, END)
        calc.insert(0, 0)
        messagebox.showinfo("Calculator", "Error, it is impossible to divide by 0")
    except:
        calc.delete(0, END)
        calc.insert(0, 0)
        messagebox.showinfo("Calculator", "Error")



def make_degit_btn(digit, bg: str = '#5787d4', fg: str = 'white') -> Button:
    """Makes adding digit button"""
    return Button(text=digit, font=("JetBrains Mono", 13), bg=bg, fg=fg, command=lambda: add_digit(digit))



def make_operation_btn(operation, bg: str = '#5787d4', fg: str = 'white') -> Button:
    """Makes adding operation button"""
    return Button(text=operation, font=("JetBrains Mono", 13), bg=bg, fg=fg, command=lambda: add_operation(operation))


def make_calc_btn(operation, cmd: str = ..., bg: str = '#5787d4', fg: str = 'white') -> Button:
    """Makes calculate"""
    return Button(text=operation, font=("JetBrains Mono", 13), bg=bg, fg=fg, command=cmd)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-/+*':
        add_operation(event.char)
    elif event.char in '.':
        add_digit(event.char)
    elif event.char == '\r':
        calculate()     
    elif event.char == '\x08':
        clear_char()


root = Tk()
root.title('Calculator')
root.geometry('240x331+800+100')
root.resizable(0, 0)
root['bg'] = '#d7d7d7'

root.bind('<Key>', press_key)


calc = Entry(root, justify=RIGHT, font=("JetBrains Mono", 15), bg='#416eb5', fg='white', width=15)
calc.insert(0, 0)
calc.grid(row=0, column=0, columnspan=4, sticky="we")


make_degit_btn('1').grid(row=2, column=0, sticky="wens")
make_degit_btn('2').grid(row=2, column=1, sticky="wens")
make_degit_btn('3').grid(row=2, column=2, sticky="wens")
make_degit_btn('4').grid(row=3, column=0, sticky="wens")
make_degit_btn('5').grid(row=3, column=1, sticky="wens")
make_degit_btn('6').grid(row=3, column=2, sticky="wens")
make_degit_btn('7').grid(row=4, column=0, sticky="wens")
make_degit_btn('8').grid(row=4, column=1, sticky="wens")
make_degit_btn('9').grid(row=4, column=2, sticky="wens")
make_degit_btn('0').grid(row=5, column=1, sticky="wens")
make_degit_btn('.').grid(row=5, column=0, sticky="wens")


make_calc_btn('x^2', cmd=to_square).grid(row=1, column=0, sticky="wens")
make_calc_btn('x^3', cmd=to_cube).grid(row=1, column=1, sticky="wens")
make_calc_btn('=', cmd=calculate).grid(row=5, column=2,sticky="wens")
make_calc_btn('C', cmd=clear).grid(row=1, column=2, sticky="wens")
make_calc_btn('<', cmd=clear_char).grid(row=1, column=3, sticky="wens")

make_operation_btn('/').grid(row=2, column=3, sticky="wens")
make_operation_btn('*').grid(row=3, column=3, sticky="wens")
make_operation_btn('-').grid(row=4, column=3, sticky="wens")
make_operation_btn('+').grid(row=5, column=3, sticky="wens")


root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)


root.mainloop()