import tkinter as tk
from tkinter import ttk
from random import choice

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# Data
first_names = ['Bob','Maria','Alex','James','Susan','Henry','Lisa','Anna','Lisa']
last_names  = ['Smith','Brown','Wilson','Thomson','Cook','Taylor','Walker','Clark']

# Treeview
table = ttk.Treeview(window, columns=('first','last','email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill= 'both', expand= True)

# Insert values into a table
# table.insert(parent='', index=0, values=('John', 'Doe', 'JohnDoe@email.com'))
for i in range(100):
    fname = choice(first_names)
    lname = choice(last_names)
    email = f'{fname[0]}{lname}@email.com'
    table.insert(parent='', index=i, values=(fname,lname,email))

table.insert(parent='', index=tk.END, values=('XXXXX','YYYYY','ZZZZZ'))

# Events
def item_select(_):
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
        
# exercise
# Create a function to delete rows in the table
def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# Items

# Run
window.mainloop()