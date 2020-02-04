from tkinter import *

window = Tk()
window.title("Kg to gram, pound, ounce")

def kg_to_others():
    val = float(entry_value.get())
    gram = val * 1000
    pound = val * 2.20462
    ounce = val * 35.274
    gram_text.delete(CURRENT, END)
    pound_text.delete(CURRENT, END)
    ounce_text.delete(CURRENT, END)
    gram_text.insert(CURRENT, gram)
    pound_text.insert(CURRENT, pound)
    ounce_text.insert(CURRENT, ounce)

kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0, padx=20)

entry_value = StringVar()
entry_input = Entry(window, textvariable=entry_value)
entry_input.grid(row=0, column=1, padx=20)

convert_button = Button(window, text="convert", command=kg_to_others)
convert_button.grid(row=0, column=2, padx=20)

gram_text = Text(window, width=20, height=1)
gram_text.grid(row=1, column=0)

pound_text = Text(window, width=20, height=1)
pound_text.grid(row=1, column=1)

ounce_text = Text(window, width=20, height=1)
ounce_text.grid(row=1, column=2)

window.mainloop()