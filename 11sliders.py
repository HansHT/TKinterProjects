import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Window
window = tk.Tk()
window.title('Template')

# Slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window, 
    command= lambda value: progress.stop(), 
    from_=0, 
    to=25,
    length=300,
    orient='horizontal',
    variable=scale_float)
scale.pack()

# Progress bar
progress = ttk.Progressbar(
    window, 
    variable= scale_float, 
    maximum=25,
    orient='horizontal',
    mode='indeterminate',
    length=400)
progress.pack()

# progress.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

# exercise
# create a progress bar that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar

def stop_func():
    pass

prog_val = tk.IntVar()
exercise_progress = ttk.Progressbar(
    window, 
    variable=prog_val, 
    orient='vertical', 
    length=300,
    )
exercise_progress_label = tk.Label(
    window, 
    textvariable=prog_val
    )
exercise_slider = ttk.Scale(
    window, 
    variable=prog_val, 
    from_ = 0, 
    to = 100
    )

exercise_progress.pack()
exercise_progress_label.pack()
exercise_slider.pack()
exercise_progress.start()

# Run
window.mainloop()