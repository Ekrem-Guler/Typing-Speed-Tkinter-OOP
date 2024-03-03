import os
import sys
from tkinter import *
from words import Func
from tkinter import ttk
f = Func()  # Function for words

# High Point checking
with open("high_point.txt") as file:
    high = file.read()


class UI:
    def __init__(self, window):
        self.ui_color = "grey12"
        self.text_color = "white"
        self.REMAIN = IntVar(value=60)
        self.pass_time = 0
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.config(bg=self.ui_color)
        self.window.minsize(800, 500)
        self.high_p = high

        self.entry_inputs = StringVar()
        self.font_var = StringVar()
        self.word_p = -1  # It is equal -1 because when points function start then it will increase 1
        self.letter_p = -9  # It is equal -9 because when points function start then it will increase 9
        self.word_num = 0
        # This part needed to provide convenience
        self.letter_point_part = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.time_part = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.time_text = ""

        # All words in here
        self.text_part = Text(width=20, height=5, font=("", 20), highlightthickness=0, borderwidth=11, spacing1=4,
                              background="grey33", foreground="white")
        self.text_part.grid(row=2, column=2, pady=30, rowspan=3)
        for i in range(len(f.words)):
            self.text_part.insert("end", f"{f.words[i]}\n")

        self.input_part = Entry(width=20, textvariable=self.entry_inputs, font=("", 18), background="grey",
                                foreground="white")
        self.input_part.focus()
        self.input_part.grid(row=5, column=2, pady=16)
        self.font_name = ttk.Combobox(textvariable=self.font_var, foreground="grey10", font=("", 9))
        self.font_name.insert("end", "Arial")
        self.font_name["values"] = ["Arial", "Ms Serif", "Modern", "Roman", "Small Fonts", "System", "Courier New",
                                    "Times New Roman", "Calibri", "Cambria", "Verdana", "Consolas", "Trebuchet MS",
                                    "Harlow Solid Italic"]
        self.font_name.grid(row=0, column=4)

        self.canvas1 = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.canvas1_text = self.canvas1.create_text(39, 50, text="Word Score", fill=self.text_color, font=("", 11))
        self.canvas1.grid(row=1, column=1, columnspan=1)

        self.canvas2 = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.canvas2_text = self.canvas2.create_text(39, 50, text="Letter Score", fill=self.text_color, font=("", 11))
        self.canvas2.grid(row=3, column=1, columnspan=1)

        self.canvas3 = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.canvas3_text = self.canvas3.create_text(38, 50, text="High Score", fill=self.text_color, font=("", 11))
        self.canvas3.grid(row=2, column=4, columnspan=1)
        self.button_restart = Button(Button(text="Restart", command=self.restart_program, background="grey",
                                            foreground="white", border=3).grid(row=7, column=2))

    def points(self, *args):  # Function to check scores and time
        n = 7
        self.move_points()
        self.move_word_num()
        self.word_point_part = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.word_point_part.create_oval(1*n, 1*n, 8*n, 8*n,
                                         outline="midnight blue", fill="grey", width=2)
        self.word_point_part.create_text(30, 30, text=self.word_p, font=("", 15))
        self.word_point_part.grid(row=2, column=1, padx=90)

        self.letter_point_part.create_oval(1 * n, 1 * n, 8 * n, 8 * n,
                                           outline="midnight blue", fill="grey", width=2)
        self.letter_point_part.create_text(30, 30, text=self.letter_p, font=("", 15))
        self.letter_point_part.grid(row=4, column=1)

        self.high_point_part = Canvas(width=80, height=60, background=self.ui_color, highlightthickness=0)
        self.high_point_part.create_oval(1 * n, 1 * n, 8 * n, 8 * n,
                                         outline="midnight blue", fill="grey",
                                         width=2)
        self.high_point_part.create_text(30, 30, text=self.high_p, font=("", 15))
        self.high_point_part.grid(row=3, column=4)

        self.time_part.create_oval(1 * n, 1 * n, 8 * n, 8 * n,
                                   outline="midnight blue", fill="grey", width=2)

        self.time_text = self.time_part.create_text(30, 30, text=":)", font=("", 15))
        self.time_part.grid(row=1, column=5)

    def neew(self, *args):  # Changing the font
        font1 = self.font_var.get()
        self.text_part.config(font=(font1, 20))
        self.font_name.config(font=(font1, 9))
        self.canvas1.itemconfig(font=(font1, 11), tagOrId=self.canvas1_text)
        self.canvas2.itemconfig(font=(font1, 11), tagOrId=self.canvas2_text)
        self.canvas3.itemconfig(font=(font1, 11), tagOrId=self.canvas2_text)

        print(self.font_var.get())

    def timer(self, *args):  # Time checking
        if self.REMAIN.get() > 0:
            self.REMAIN.set(60-self.pass_time)
            self.window.after(1000, self.timer)
            self.pass_time += 1
            self.time_part.itemconfig(text=self.REMAIN.get(), tagOrId=self.time_text)
        else:
            if int(self.high_p) < self.word_p:
                self.high_p = self.word_p
                with open("high_point.txt", "w") as file1:
                    file1.write(str(self.word_p))
            self.clear_frame()
            self.game_over()
            self.button_restart = Button(Button(text="Restart", command=self.restart_program,
                                                width=30, height=2).pack(pady=10))
            self.button_restart = Button(Button(text="Exit", command=self.exit_program, width=30, height=2,
                                                background="midnight blue").pack())

    def move_word_num(self, *args):  # Passing the word
        self.word_num += 1

    def move_points(self):  # Adding the points
        letter_len = len(f.words[self.word_num - 1])
        self.letter_p += letter_len
        self.word_p = int(self.letter_p/5)

    def clear_frame(self):  # Clear all widgets
        for widgets in self.window.winfo_children():
            widgets.destroy()

    def game_over(self):  # Game over UI
        self.window.config(bg="seashell2")
        self.canvas_over = Canvas(width=300, height=300, background="seashell2", highlightthickness=0)
        self.canvas_over.create_text(100, 100, text=f"  Letter Score: {self.letter_p}\n\n  "
                                                    f"Word Score: {self.word_p}\n\n  "
                                                    f"High Score: {self.high_p}",
                                     font=("", 15), fill="midnight blue")
        self.canvas_over.pack()

    def restart_program(self):
        python = sys.executable
        os.startfile("main.py")
        os.execl(python, python, *sys.argv)

    def exit_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
