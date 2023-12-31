import tkinter as tk
from tkinter import ttk

# Setup
window =tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# Canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# canvas.create_rectangle((50,20,100,200), fill='red', width=10, dash=(4,2,1,1), outline= 'green') # Left, Top, Right, Bottom
# canvas.create_oval((200,0,300,100), fill='green')
# canvas.create_arc(
#     (200,0,300,100), 
#     fill = 'red', 
#     start = 45, 
#     extent = 140, 
#     style = tk.CHORD, 
#     outline = 'red', 
#     width = 1)

# canvas.create_line((0,0,100,150), fill='blue')
# canvas.create_polygon((0,0, 100,200, 300,50), fill='gold') # x1,y1, x2,y2, x3,y3

# canvas.create_text((100,200), text = 'This is some text', fill='green', width=30)

# canvas.create_window((150,100), window= ttk.Button(window, text= ' This is text in a canvas'))

# Exercise
# user event binding to create a basic paint app

def paint(event):
    # size   = 1
    left   = event.x - size
    top    = event.y - size
    right  = event.x + size 
    bottom = event.y + size

    canvas.create_oval((left, top, right, bottom), fill= 'black')
    # print(f'x: {event.x} y: {event.y}')

def brush_size_adjust(event):
    global size
    if event.delta > 0:
        size += 1
    else:
        size -= 1
    
    size = max(0,min(size, 50))

size = 2

canvas.bind('<B1-Motion>', paint)
canvas.bind('<MouseWheel>', brush_size_adjust)

# Run
window.mainloop()