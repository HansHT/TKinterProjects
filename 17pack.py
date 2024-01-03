import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('400x600')
window.title('Pack')

# Widgets
label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='last of the labels', background='green')
button = ttk.Button(window, text='Button') 

# Layout
# label1.pack(side='left', expand = True, fill = 'both')
# label2.pack(side='top', expand = True, fill = 'both') 
# label3.pack(side='top', expand = True, fill = 'both')
# button.pack(side='top', expand = True, fill = 'both')

# Exercise layout
# label1.pack(side='top', fill= 'x')
# label2.pack(side='top', expand=True) 
# label3.pack(side='top', expand=True, fill='both')
# button.pack(side='top', fill= 'x')

# Exercise 2:
label1.pack(side='top', expand=True, fill='both',padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
button.pack(side='bottom', expand=True, fill='both')
label3.pack(side='bottom', expand=True, fill='both')

# Run
window.mainloop()