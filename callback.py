from tkinter import *


class Call:
    def __init__(self, text_part, input_part, f, entry_inputs, timer, window):
        self.word_num = 0  # Checking which word we are
        self.word_point = IntVar()
        self.letter_point = IntVar() 
        self.control_word = IntVar()  # Just checking the change
        
        self.entry_inputs = entry_inputs
        self.text_part = text_part
        self.input_part = input_part
        self.timer = timer
        self.window = window
        self.f = f
        
        self.flag = 0

    def callback(self, *args):
        
        # Timer starts when first letter writes
        if self.entry_inputs.get() != "" and self.flag == 0:
            self.timer(self.window)
            self.flag += 1
        
        # Checking the input between actual word
        if len(self.entry_inputs.get()) > len(self.f.words[self.word_num]):
            self.text_part.tag_config(f"nextline{self.word_num + 1}", foreground="red")
        else:
            self.text_part.tag_config(f"nextline{self.word_num + 1}", foreground="blue")


        # Passing new word
        if " " in self.entry_inputs.get():
            if self.entry_inputs.get() == f"{self.f.words[self.word_num]} ":
                self.word_point.set(0)
                self.letter_point.set(len(self.f.words[self.word_num]))
                
            # Check the change for colors.py file
            else:
                self.control_word.set(2)

            self.text_part.see(f"{self.word_num+6}.0")
            self.text_part.tag_config(f"nextline", background="white", foreground="black")
            self.input_part.delete(first=0, last=100)
            self.word_num += 1
            self.text_part.tag_config(f"nextline{self.word_num}", background="white", foreground="black")
            self.text_color(self.word_num + 1)
            # Passed the new word

    def text_color(self, line):
        self.text_part.tag_add(f"nextline{line}", f"{line}.0", f"{line}.20")
        self.text_part.tag_config(f"nextline{line}", background="grey15", foreground="blue")
