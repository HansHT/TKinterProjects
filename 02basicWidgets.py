import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button was pressed")

def hello_button():
    print("hello")

# Create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk widgets
label = ttk.Label(master=window, text="this is a test")
label.pack()

# Create widgets
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# exercise
exercise_label = ttk.Label(master=window, text="my Label")
#exercise_button = ttk.Button(master=window, command=hello_button)
exercise_button = ttk.Button(master=window, command=lambda: print("hello"))
exercise_label.pack()
exercise_button.pack()

# ttk button
button = ttk.Button(master=window, text="Enter", command= button_func)
button.pack()


# Run
window.mainloop()
print("GUI shutdown")