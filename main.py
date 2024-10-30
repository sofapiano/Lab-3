import tkinter as tk
import re
from generator import generate


TXT_HEIGHT = 10


def init_gui():
    root = tk.Tk()
    root.title("definitely not a piracy")

    return root


def init_frames(root):
    fr_input_code = tk.Frame(root)
    lbl_greet = tk.Label(text="welcome to the definitely not-piracy app")
    fr_input_code.pack(fill=tk.X, side=tk.BOTTOM)
    lbl_greet.pack(anchor='nw', padx=5, pady=5)
    
    fr_output_key = tk.Frame(root)
    fr_output_key.pack(anchor='c')

    # canvas1.create_window(fill=tk.X, side=tk.BOTTOM, window=fr_input_code)
    # canvas1.create_window(anchor='nw', padx=5, pady=5, window=lbl_greet)
    # canvas1.create_window(anchor='c', window=fr_output_key)

    return fr_input_code, fr_output_key


def init_input(fr_input):
    code_entry = tk.Entry(fr_input)
    label = tk.Label(text="enter the 6-digit code")

    def click(code_entry):
        code = code_entry.get()
        flag = 1
        while flag:
            if is_valid(code):
                flag = 0
                key = generate(code)
        
    
    btn_gen = tk.Button(fr_input, text='generate', command= lambda: click(code_entry))

    code_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    btn_gen.pack(side=tk.LEFT)
    label.pack(side=tk.BOTTOM, anchor='w')


def is_valid(newval):
    if len(newval) != 6:
        tk.errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        tk.errmsg.set("")


if __name__ == '__main__':
    root = init_gui()
    # root.geometry("600x900")
    # bg = tk.PhotoImage(file = "civ-VI.png")
    # canvas1 = tk.Canvas( root, width = 600, height = 900)
    # canvas1.pack(fill = "both", expand = True) 
    # canvas1.create_image( 0, 0, image = bg, anchor = "nw") 
    fr_input_code, fr_output_key = init_frames(root)
    init_input(fr_input_code)
    root.mainloop()