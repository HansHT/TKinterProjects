import tkinter as tk
from tkinter import ttk

# List of events
# pythontutorial.net/tkinter/tkinter-event-binding/
# stackoverflow.com/questions/32289175/list-of-all-tkinter-events

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# Window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

# Widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A button')
button.pack()

# Events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'A button was pressed ({event.char})'))

# window.bind('<Motion>', get_pos)

# entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

# exercise:
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print("Mousewheel"))

# Run
window.mainloop()