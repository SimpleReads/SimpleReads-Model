import tkinter as tk
from controller import SentenceController

if __name__ == '__main__':
    root = tk.Tk()
    default_font = ('Arial', 12)
    root.option_add('*Font', default_font)
    root.resizable(True, True)
    root.config(bg='light blue')
    root.geometry("1280x800")
    controller = SentenceController(root)
    root.mainloop()
