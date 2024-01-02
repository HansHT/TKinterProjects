import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Template')

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_command(label='Open', command=lambda: print('Open File'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)

# another sub_menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help entry', command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar(value='off')
help_menu.add_checkbutton(label= 'check', onvalue='on', offvalue='off', variable= help_check_string)

menu.add_cascade(label= 'Help', menu=help_menu)

# exercise:
# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
exrc_menu = tk.Menu(menu, tearoff= False)
sub_menu = tk.Menu(exrc_menu, tearoff=False)
sub_menu.add_command(label='Sub selection', command= lambda: print('Bingo!'))

exrc_menu.add_cascade(label='Sub menu', menu=sub_menu)
menu.add_cascade(label='Exercise', menu=exrc_menu)


window.configure(menu = menu)

# menu button
menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label= 'entry 1', command= lambda: print('test 1'))
button_sub_menu.add_checkbutton(label= 'check 1')
# menu_button.configure(menu= button_sub_menu)
menu_button['menu']= button_sub_menu

# Run
window.mainloop()