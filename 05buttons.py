import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# Button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text= 'A simple button', command= button_func, textvariable= button_string)
button.pack()

# Checkbutton
check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(
    window, 
    text='checkbox 1', 
    command= lambda: print(check_var.get()),
    variable= check_var,
    onvalue= 10,
    offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text= 'checkbox 2',
    command= lambda: print('test'))
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, 
    text= 'Radiobutton 1', 
    value= 'radio 1', 
    variable= radio_var,
    command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text= 'Radiobutton 2', value= 2, variable= radio_var)
radio2.pack()

# exercise
# create another check button and 2 radio buttions
# radio button:
    # values for the buttons are A and B
    # ticking either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton
# check button:
    # ticking the check button prints the value of the radio button value
    # use tkinter var for Booleans!

def radio_func():
    print(check3_var.get())
    check3_var.set(False)

radio_string = tk.StringVar()
radio3 = ttk.Radiobutton(
    window, 
    text= 'radio A', 
    value='A', 
    variable= radio_string,
    command= radio_func)
radio3.pack()

radio4 = ttk.Radiobutton(
    window, 
    text= 'radio B', 
    value='B', 
    variable= radio_string,
    command= radio_func)
radio4.pack()

check3_var = tk.BooleanVar(value=True)
check3 = ttk.Checkbutton(
    window, 
    text= 'checkbox 3', 
    variable=check3_var, 
    onvalue=True, 
    offvalue=False, 
    command= lambda: print(radio_string.get()))
check3.pack()
# Run
window.mainloop()