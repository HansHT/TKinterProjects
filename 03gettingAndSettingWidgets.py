import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
    # label.configure(text="some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"
    print(label.configure())

# Window
window = tk.Tk()
window.title("Getting and setting variables")

# Widgets
label = ttk.Label(master=window, text="lorem ipsum")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that enables entry
def exc_button_func():
    label['text'] = 'lorem ipsum'
    entry['state'] = 'enabled'
    
exercise_button = ttk.Button(master=window, text="Undo", command= exc_button_func)
exercise_button.pack()

# Run
window.mainloop()