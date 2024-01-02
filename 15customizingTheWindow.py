import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400+100+200')
window.title('More on the window')
window.iconbitmap('logos/possum.ico')

# exercise:
# start window in the middle of the screen
xwin = 600; ywin = 400
xdis = window.winfo_screenwidth(); ydis = window.winfo_screenheight()
xstart = int((xdis - xwin)/2); ystart = int((ydis - ywin)/2)
window.geometry(f'{xwin}x{ywin}+{xstart}+{ystart}')

# Window sizes
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True, False)

# Screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window attributes
window.attributes('-alpha', 1)
# window.attributes('-topmost', True)

# Security event
window.bind('<Escape>', lambda event: window.quit())
# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)


# Title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')

# Run
window.mainloop()