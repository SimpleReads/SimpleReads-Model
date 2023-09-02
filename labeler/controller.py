from model import SentenceModel
from view import SentenceView
import tkinter as tk
from tkinter import Menu

class SentenceController:
    def __init__(self, root):
        self.model = SentenceModel()
        self.view = SentenceView(root, self)
        
        self.view.file_menu.add_command(label="Load Files", command=self.load_file)
        
        # Move the creation of the "Next" button here.
        self.next_button = tk.Button(root, text="Next", command=self.show_next_sentence)
        self.next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        # Button for switching to sentence
        self.switch_sentence_button = tk.Button(self.view.sentence_info_frame, text="Switch", command=self.switch_sentence)
        self.switch_sentence_button.grid(row=1, column=2, padx=10, pady=10)

        self.init()

    def init(self):
        self.model.load_default()
        self.update_sentence()
        self.update_sentence_number()

    def switch_sentence(self):
        sentence_number = int(self.view.switch_sentence_text.get("1.0", tk.END))
        self.model.switch_sentence(sentence_number)
        self.update_sentence()
        self.update_sentence_number()

    def show_next_sentence(self):
        self.model.show_next_sentence()
        self.update_sentence()
        self.update_sentence_number()

    def load_file(self):
        self.model.load_file()
        
    def update_sentence(self):
        original, lexical, syntactic = self.model.update_sentence()

        # Update original_sentence
        self.view.original_sentence.delete("1.0", tk.END)
        self.view.original_sentence.insert(tk.END, original)

        # Update lexical_sentence
        self.view.lexical_sentence.delete("1.0", tk.END)
        self.view.lexical_sentence.insert(tk.END, lexical)

        # Update syntactic_sentence
        self.view.syntactic_sentence.delete("1.0", tk.END)
        self.view.syntactic_sentence.insert(tk.END, syntactic)

    def update_sentence_number(self):
        self.view.sentence_number.config(text=str(self.model.index + 1))

    def on_right_click(self, event):
        widget = event.widget  # This will give you the widget that triggered the event
        index = widget.index(f"@{event.x},{event.y} wordstart")
        last_index = widget.index(f"@{event.x},{event.y} wordend")
        clicked_word = widget.get(index, last_index)

        synonyms = self.model.get_synonyms(clicked_word)  # Assuming get_synonyms is defined in your model

        # Create a popup menu
        popup = Menu(self.view.root, tearoff=0)
        
        if synonyms:
            for synonym in synonyms:
                popup.add_command(label=synonym, command=lambda s=synonym: self.replace_word(widget, index, last_index, s))
        else:
            popup.add_command(label="No synonyms found")

        # Position menu at the event location
        popup.tk_popup(event.x_root, event.y_root)

    def replace_word(self, widget, start_index, end_index, new_word):
        widget.delete(start_index, end_index)
        widget.insert(start_index, new_word)

