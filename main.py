from tkinter import *
from words import Func
from callback import Call
from colors import UI
f = Func()  # Function for words

window = Tk()

ui = UI(window)
back = Call(input_part=ui.input_part, text_part=ui.text_part, entry_inputs=ui.entry_inputs, f=f, timer=ui.timer,
            window=window)  # Controller function

back.text_color(1)

ui.points(0)
ui.entry_inputs.trace("w", back.callback)
ui.font_var.trace("w", ui.neew)
back.word_point.trace("w", ui.points)
back.control_word.trace("w", ui.move_word_num)

# Unalterable parts
ui.text_part["state"] = "disabled"
ui.high_point_part["state"] = "disabled"
ui.letter_point_part["state"] = "disabled"
ui.word_point_part["state"] = "disabled"
ui.font_name["state"] = "readonly"

window.mainloop()
