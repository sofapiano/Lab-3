import tkinter as tk
from generator import generate
from pygame import mixer


WELCOME_TEXT = 'welcome to the definitely not-piracy keygen'

def init_gui():
    root = tk.Tk()
    root.geometry("639x361")
    root.title("definitely not a piracy app")

    mixer.init() 
    mixer.music.load("megalovania.mp3") 
    mixer.music.play(999)
    return root


def init_canvas(root):
    bg_image = tk.PhotoImage(file="image.png")
    canvas = tk.Canvas(root, width=639, height=361)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.bg_image = bg_image
    return canvas


def init_frames(canvas):
    lbl_greet = tk.Label(canvas, 
                        text=WELCOME_TEXT,
                        font= ("Roboto", 12), 
                        bg="#85Baa1")
    canvas.create_window(165, 25, window=lbl_greet)

    lbl_key = output_key(canvas)

    return lbl_key


def init_input(label, canvas):
    code_entry = tk.Entry(canvas,
                          font=("Roboto", 12))
    lbl_input = tk.Label(text="input 6-digit decimal number",
                         font= ("Roboto", 12),
                         background='#85Baa1')

    def click(code_entry):
        code = code_entry.get()
        key = generate(code)
        label['text'] = key


    btn_generate = tk.Button(canvas, 
                             text="get key", 
                             command=lambda:click(code_entry),
                             font=("Roboto", 12),
                             background='#85Baa1')
    
    code_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    canvas.create_window(110, 315, window=lbl_input)
    canvas.create_window(100, 340, window=code_entry)
    canvas.create_window(250, 340, window=btn_generate)


def output_key(canvas):
    lbl_key = tk.Label(canvas, 
                       text='XXXXX-XXXXX XXXX', 
                       background='#85Baa1',
                       font= ("Roboto", 20))
    canvas.create_window(250, 250, window=lbl_key)

    return lbl_key  


if __name__ == '__main__':
    root = init_gui()
    canvas = init_canvas(root)

    key_lbl = init_frames(canvas)

    init_input(key_lbl, canvas)

    

    root.mainloop()