import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames & Parenting')

# Frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=10, relief= tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# Parenting / master setting
label = ttk.Label(frame, text='label in frame')
label.pack()

button = ttk.Button(frame, text='button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text='Label outside frame')
label2.pack(side='left')

# exercise
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets

exrc_frame = ttk.Frame(window, relief=tk.GROOVE)
exrc_frame.pack(side='right')

exrc_label = ttk.Label(exrc_frame, text='Exercise label')
exrc_label.pack()

exrc_button = ttk.Button(exrc_frame, text='Exercise button')
exrc_button.pack()

exrc_entry = ttk.Entry(exrc_frame)
exrc_entry.pack()

# Run
window.mainloop()