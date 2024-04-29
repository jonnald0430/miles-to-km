import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# functionality / conversion
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# window / styling
window = ttk.Window(themename = "journal")
window.title("Demo")
window.geometry("300x150")

# title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font= "calibri 24 bold") # child to window
title_label.pack()

# input field / widgets basics
input_frame = ttk.Frame(master = window) # child to window
entry_int = tk.IntVar() # stores int
entry = ttk.Entry(master = input_frame, textvariable=entry_int) # child to input_frame

button = ttk.Button(master = input_frame, text = "convert", command = convert) # child to input_frame, only pass functions, don't call

# layouts basics
input_frame.pack(pady = 10)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")

# output
output_string = tk.StringVar() # stores string
output_label = ttk.Label(master = window, 
                         text = "output", 
                         font = "Calibri 24 bold", 
                         textvariable=output_string)
output_label.pack(pady = 5)

# run/main loop
window.mainloop()
