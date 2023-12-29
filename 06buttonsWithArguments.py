import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func


# Window
window = tk.Tk()
window.title("Buttons, functions and arguments")

# Widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable= entry_string)
entry.pack()

button = ttk.Button(window, text='button', command= lambda:button_func(entry_string))
# button = ttk.Button(window, text='button', command= outer_func(entry_string))
button.pack()

# Run
window.mainloop()