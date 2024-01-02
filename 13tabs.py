import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Tab widget')

# Notebook widgets
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='Button in tab 1')
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack()

# exercise
# add another tab with 2 buttons and one label inside

exrc_tab = ttk.Frame(notebook)
exrc_button1 = ttk.Button(exrc_tab, text='Button 1').pack()
exrc_button2 = ttk.Button(exrc_tab, text='Button 2').pack()
exrc_label = ttk.Label(exrc_tab, text='Text in exercise tab').pack()
notebook.add(exrc_tab, text='Tab 3')

# Run
window.mainloop()