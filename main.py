import tkinter as tk
from generator import generate
from pygame import mixer
from PIL import Image, ImageTk


MSG_HEIGHT = 4
WELCOME_TEXT = 'welcome to the definitely not-piracy keygen'
keys_lbls = []


def init_gui():
    root = tk.Tk()

    bg = tk.PhotoImage(file='civ-VI.png')
    canvas1 = tk.Canvas(root, width=600,
                        height=900)
    canvas1.pack(fill='both', expand=True)
    canvas1.create_image(0, 0, image=bg,
                         anchor='nw')

    mixer.init() 
    mixer.music.load("megalovania.mp3") 
    mixer.music.play(999)
    return root


def init_frames(root):
    fr_code_input = tk.Frame(root)
    fr_key_output = tk.Frame(root)
    fr_code_input.pack(fill=tk.X, side=tk.BOTTOM)
    fr_key_output.pack(fill=tk.BOTH, expand=True)

    lbl_greet = tk.Label(fr_key_output, text=WELCOME_TEXT, height=MSG_HEIGHT)
    lbl_greet.pack(side=tk.TOP)

    lbl_key = output_key(fr_key_output)

    return fr_code_input, fr_key_output, lbl_key


def init_input(fr_input, label):
    code_entry = tk.Entry(fr_input)
    lbl_input = tk.Label(text="input 6-digit decimal number", 
                         height=MSG_HEIGHT)

    def click(code_entry):
        code = code_entry.get()
        key = generate(code)
        label['text'] = key


    btn_generate = tk.Button(fr_input, 
                             text="get key", 
                             command=lambda:click(code_entry))
    
    code_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    btn_generate.pack(side=tk.LEFT)
    lbl_input.pack(side=tk.LEFT)


def output_key(fr_key_output):
    lbl_key = tk.Label(fr_key_output, 
                       text='XXXXX-XXXXX XXXX',
                       height=MSG_HEIGHT, 
                       background='#85Baa1')
    lbl_key.pack(side=tk.TOP, 
                 anchor="center",
                 padx=4,
                 pady=4)

    return lbl_key  


if __name__ == '__main__':
    root = init_gui()
    # fr_code_input, fr_key_output, key_lbl = init_frames(root)

    # init_input(fr_code_input, key_lbl)
    root.mainloop()