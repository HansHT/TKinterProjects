import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Combobox & Spinbox')

# Combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.configure(values=items)
combo.pack()

# Events
combo.bind(
    '<<ComboboxSelected>>', 
    lambda event: combo_label.configure(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text='a label')
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value= 12)
spin = ttk.Spinbox(
    window, 
    from_ = 3, 
    to = 20, 
    increment = 3, 
    command= lambda: print(spin_int.get()),
    textvariable= spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['values'] = (1,2,3,4,5)
spin.pack()


# exercise:
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decresed

spin_string = tk.StringVar(value='A')
spin_letters = ('A','B','C','D','E')
exercise_spin = ttk.Spinbox(window, textvariable=spin_string, values=spin_letters)
# exercise_spin['values'] = ('A','B','C','D','E')
exercise_spin.bind('<<Decrement>>', lambda event: print(spin_string.get()))
exercise_spin.pack()

# Run
window.mainloop() 