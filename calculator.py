import tkinter as tk
from tkinter import messagebox

#input global variable
mainWindowChars = ""
 
#var add
def Btn(charFromMain):
    global mainWindowChars
    mainWindowChars = mainWindowChars + str(charFromMain)
    equation.set(mainWindowChars)
 
#char add      
def charBtn(charFromMain):
    global mainWindowChars
    if  mainWindowChars != "":
        mainWindowChars = mainWindowChars + str(charFromMain)
        equation.set(mainWindowChars)
    else:
        messagebox.showinfo(title = "Error", message = "Incorrect input format,pls try again!")
        equation.set(" Error ")
        mainWindowChars = ""
# obliczanie wyniku
def isEqualTo():
    try: 
        global mainWindowChars
        # eval daje wynik
        result = str(eval(mainWindowChars))
        mainWindowChars = mainWindowChars + "=" + result
        firstEquation.set(mainWindowChars)
        equation.set(result) 
        mainWindowChars = result
 
    except:
        messagebox.showinfo(title = "Error", message = "Equation error, pls try again!")
        equation.set(" Error ")
        mainWindowChars = ""
  
# clear all
def AC():
    global mainWindowChars
    mainWindowChars = ""
    equation.set("")

 
# Backspace
def Backspace():
    global mainWindowChars
    mainWindowChars=mainWindowChars[:-1]
    equation.set(mainWindowChars)
 
if __name__ == "__main__":

    gui = tk.Tk() 
    gui.configure(bg = "light gray")
    gui.title("Simple Calculator")
    gui.geometry("403x365")
    equation = tk.StringVar()
    firstEquation = tk.StringVar()

    #history
    historia = tk.Entry(gui, textvariable = firstEquation, font = 'Arial 12')
    historia.grid(columnspan = 4,rowspan = 1,ipady = 10, ipadx = 110)
    
    #equation field
    pole = tk.Entry(gui, textvariable = equation, font = 'Arial 12')
    pole.grid(columnspan = 4,rowspan = 1,ipady = 25, ipadx = 110)
    
    #btns
    clear = tk.Button(gui, text = 'AC', fg = 'white', bg = '#125751', font = 'Arial 12',
                command = AC, height = 2, width = 10)
    clear.grid(row = 2, column = 0)
    
    back = tk.Button(gui, text = '<-', fg = 'white', bg = '#125751', font = 'Arial 12',
                command = Backspace, height = 2, width = 10)
    back.grid(row = 2, column = 1)
    
    power = tk.Button(gui, text = "^", fg = 'white', bg = '#125751', font = 'Arial 12',
                      command = lambda:charBtn('**'), height = 2, width = 10)
    power.grid(row = 2, column = 2)
    
    divide = tk.Button(gui, text = '/', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: charBtn("/"), height = 2, width = 10)
    divide.grid(row = 2, column = 3)
 
    button1 = tk.Button(gui, text = '1', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(1), height = 2, width = 10)
    button1.grid(row = 3, column = 0)
 
    button2 = tk.Button(gui, text = '2', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(2), height = 2, width = 10)
    button2.grid(row = 3, column = 1)
 
    button3 = tk.Button(gui, text = '3', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command=lambda: Btn(3),height = 2, width = 10)
    button3.grid(row = 3, column = 2)
     
    multiply = tk.Button(gui, text = '*', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: charBtn("*"), height = 2, width = 10)
    multiply.grid(row = 3, column = 3)
 
    button4 = tk.Button(gui, text = '4', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(4), height = 2, width = 10)
    button4.grid(row = 4, column = 0)
 
    button5 = tk.Button(gui, text = '5', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(5), height = 2, width = 10)
    button5.grid(row = 4, column = 1)
 
    button6 = tk.Button(gui, text = '6', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(6), height = 2, width = 10)
    button6.grid(row = 4, column = 2)
    
    plus = tk.Button(gui, text = '+', fg = 'white', bg = '#125751', font = 'Arial 12',
                command = lambda: charBtn("+"), height = 2, width = 10)
    plus.grid(row = 4, column = 3)
 
    button7 = tk.Button(gui, text = '7', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(7), height = 2, width = 10)
    button7.grid(row = 5, column = 0)
 
    button8 = tk.Button(gui, text = '8', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(8), height = 2, width = 10)
    button8.grid(row = 5, column = 1)
 
    button9 = tk.Button(gui, text = '9', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: Btn(9), height = 2, width = 10)
    button9.grid(row = 5, column = 2)
 
    minus = tk.Button(gui, text = '-', fg = 'white', bg = '#125751', font = 'Arial 12',
                command = lambda: charBtn("-"), height = 2, width = 10)
    minus.grid(row = 5, column = 3)

    Decimal= tk.Button(gui, text = '.', fg = 'white', bg = '#125751', font = 'Arial 12',
                    command = lambda: charBtn('.'), height = 2, width = 10)
    Decimal.grid(row = 7, column = 0)
    
    button0 = tk.Button(gui, text = '0', fg = 'white', bg  = '#125751', font = 'Arial 12',
                    command  = lambda: Btn(0), height = 2, width = 10)
    button0.grid(row = 7, column = 1) 
    
    equal = tk.Button(gui, text = '=', fg = 'white', bg = '#125751', font = 'Arial 12',
                command = isEqualTo, height = 2, width = 10)
    equal.grid(row = 7, column = 2, columnspan = 2,ipadx = 50.5)
     
    gui.mainloop()

