import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# Window
window = tk.Tk()
window.title('TKinter Variables')
window.geometry('200x150')

# TKinter variable
string_var = tk.StringVar(value='Start value')


# widgets
label = ttk.Label(master=window, text='Some text', textvariable= string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable= string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

# exercise
# create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of 'test'
new_string_var = tk.StringVar(value='test')

entry1 = ttk.Entry(master=window, textvariable=new_string_var)
entry1.pack(pady=5)
entry2 = ttk.Entry(master=window, textvariable=new_string_var)
entry2.pack()
label1 = ttk.Label(master=window, textvariable=new_string_var)
label1.pack()

# Run
window.mainloop()