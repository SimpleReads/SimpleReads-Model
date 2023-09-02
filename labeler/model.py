import difflib
import os
import random
import nltk
from tkinter import filedialog
import difflib

class SentenceModel:
    def __init__(self):
        nltk.download('wordnet')
        self.wordnet = nltk.corpus.wordnet
        self.original_sentences = None
        self.lexical_sentences = None
        self.syntactic_sentences = None
        self.index = 0

    def load_default(self):
        original_path = "../datasets/simpa-master/ss-original.txt"
        lexical_path = "../datasets/simpa-master/ss-ls-simplified.txt"
        syntactic_path = "../datasets/simpa-master/ss-simplified.txt"

        with open(original_path, 'r', encoding='utf-8') as f:
                self.original_sentences = [line.strip() for line in f]
        with open(lexical_path, 'r', encoding='utf-8') as f:
            self.lexical_sentences = [line.strip() for line in f]
        with open(syntactic_path, 'r', encoding='utf-8') as f:
            self.syntactic_sentences = [line.strip() for line in f]

        if len(self.original_sentences) == len(self.lexical_sentences) == len(self.syntactic_sentences):
            self.index = 0
            self.update_sentence()
        else:
            print("The lengths of the files do not match!")

    def load_file(self):
        current_directory = os.getcwd()  # Get current directory
        parent_directory = os.path.dirname(current_directory)  # Get parent directory
        original_path = filedialog.askopenfilename(
            initialdir=parent_directory,
            title="Load original sentences", 
            filetypes=[("TXT files", "*.txt")]
            )
        lexical_path = filedialog.askopenfilename(
            initialdir=parent_directory, 
            title="Load lexical simplifications", 
            filetypes=[("TXT files", "*.txt")]
            )
        syntactic_path = filedialog.askopenfilename(
            initialdir=parent_directory, 
            title="Load syntactic simplifications", 
            filetypes=[("TXT files", "*.txt")]
            )
        
        if original_path and lexical_path and syntactic_path:
            with open(original_path, 'r', encoding='utf-8') as f:
                self.original_sentences = [line.strip() for line in f]
            with open(lexical_path, 'r', encoding='utf-8') as f:
                self.lexical_sentences = [line.strip() for line in f]
            with open(syntactic_path, 'r', encoding='utf-8') as f:
                self.syntactic_sentences = [line.strip() for line in f]

            if len(self.original_sentences) == len(self.lexical_sentences) == len(self.syntactic_sentences):
                self.index = 0
                self.update_sentence()
            else:
                print("The lengths of the files do not match!")

    def show_next_sentence(self):
        self.modify_sentence(self.get_current_sentences())
        self.index += 1
        if self.index >= len(self.original_sentences):
            self.index = 0

    def switch_sentence(self, sentence_number):
        # Switch to the sentence number
        self.index = sentence_number - 1

    def write_to_file(self):
        # Create 'output' folder if it doesn't exist
        if not os.path.exists('output'):
            os.makedirs('output')
            
        index = self.index  # Current index
        
        with open("output/original-output.txt", 'a', encoding='utf-8') as f:
            f.write(self.original_sentences[index] + '\n')
            
        with open("output/lexical-output.txt", 'a', encoding='utf-8') as f:
            f.write(self.lexical_sentences[index] + '\n')
            
        with open("output/syntactic-output.txt", 'a', encoding='utf-8') as f:
            f.write(self.syntactic_sentences[index] + '\n')


    def modify_sentence(self, sentences):
        original, lexical, syntactic = sentences
        if original is not None:
            self.original_sentences[self.index] = original
        if lexical is not None:
            self.lexical_sentences[self.index] = lexical
        if syntactic is not None:
            self.syntactic_sentences[self.index] = syntactic
        
        # Write all the sentences to the file
        self.write_to_file()

    def get_current_sentences(self):
        original = self.original_sentences[self.index]
        lexical = self.lexical_sentences[self.index]
        syntactic = self.syntactic_sentences[self.index]
        return original, lexical, syntactic

    def update_sentence(self):
        if self.original_sentences and self.lexical_sentences and self.syntactic_sentences:
            original = self.original_sentences[self.index]
            lexical = self.lexical_sentences[self.index]
            syntactic = self.syntactic_sentences[self.index]

            return original, lexical, syntactic
        else:
            return None, None, None


    def get_synonyms(self, word):
        synonyms = []
        for syn in self.wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name().replace('_', ' '))
            for hypernym in syn.hypernyms():
                for lemma in hypernym.lemmas():
                    synonyms.append(lemma.name().replace('_', ' '))
        return list(set(synonyms))


