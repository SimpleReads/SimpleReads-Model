import tkinter as tk
from tkinter import Menu, filedialog
from tkinter import ttk
from tkinter import font as tkfont

class SentenceView:
    def __init__(self, root, controller):
        self.root = root

        # Font settings
        bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

        # Main Frames
        original_frame = tk.Frame(root, bg="light blue")
        original_frame.pack(pady=20)
        lexical_frame = tk.Frame(root, bg="light blue")
        lexical_frame.pack(pady=20)
        syntactic_frame = tk.Frame(root, bg="light blue")
        syntactic_frame.pack(pady=20)
        self.sentence_info_frame = tk.Frame(root, bg="light blue")
        self.sentence_info_frame.pack(pady=20)

        # Original Sentence Section
        self.original_label = tk.Label(original_frame, text="Original Sentence:", bg="light blue", font=bold_font)
        self.original_label.grid(row=0, column=0, sticky="w")
        self.original_sentence = tk.Text(original_frame, height=3, wrap=tk.WORD, width=120, undo=True)
        self.original_sentence.grid(row=1, column=0)

        # Lexical Sentence Section
        self.lexical_label = tk.Label(lexical_frame, text="Lexical Simplifications:", bg="light blue", font=bold_font)
        self.lexical_label.grid(row=0, column=0, sticky="w")
        self.lexical_sentence = tk.Text(lexical_frame, height=3, wrap=tk.WORD, width=120, undo=True)
        self.lexical_sentence.grid(row=1, column=0)

        # Syntactic Sentence Section
        self.syntactic_label = tk.Label(syntactic_frame, text="Syntactic Simplification:", bg="light blue", font=bold_font)
        self.syntactic_label.grid(row=0, column=0, sticky="w")
        self.syntactic_sentence = tk.Text(syntactic_frame, height=3, wrap=tk.WORD, width=120, undo=True)
        self.syntactic_sentence.grid(row=1, column=0)

        # Current and Switch Sentence Section
        line_num_label = tk.Label(self.sentence_info_frame, text="Current Sentence:", bg="light blue", font=bold_font)
        line_num_label.grid(row=0, column=0, sticky="w")
        self.sentence_number = tk.Label(self.sentence_info_frame, text="1", bg="light blue", font=bold_font)
        self.sentence_number.grid(row=0, column=1)

        self.switch_sentence_label = tk.Label(self.sentence_info_frame, text="Switch Sentence:", bg="light blue", font=bold_font)
        self.switch_sentence_label.grid(row=1, column=0, sticky="w")
        self.switch_sentence_text = tk.Text(self.sentence_info_frame, height=1, width=3)
        self.switch_sentence_text.grid(row=1, column=1)

        # Bind right-click event to text widgets
        self.original_sentence.bind("<Button-3>", controller.on_right_click)
        self.lexical_sentence.bind("<Button-3>", controller.on_right_click)
        self.syntactic_sentence.bind("<Button-3>", controller.on_right_click)


        # Menu
        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)

    def highlight_diff(self, diff):
        # Delete all tags from both widgets
        self.original_sentence.tag_delete("highlight")
        self.lexical_sentence.tag_delete("highlight")

        # Configure the highlight tag for both sentences
        self.original_sentence.tag_configure("highlight", background="yellow")
        self.lexical_sentence.tag_configure("highlight", background="yellow")

        # Add new tags to both sentences
        for tag, start, end in diff:
            self.original_sentence.tag_add(tag, start, end)
            self.lexical_sentence.tag_add(tag, start, end)

