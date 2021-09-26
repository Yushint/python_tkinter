from tkinter import *


root = Tk()
entry_line_one = Entry(root, width=10)
entry_line_two = Entry(root, width=10)


def plus_func(event):
    try:
        num1, num2 = float(entry_line_one.get()), float(entry_line_two.get())
    except Exception:
        answer_lab["text"] = "Ошибка. Исправьте значения чисел."
        return plus_func
    total_num = str("{:.2f}".format(num1 + num2))
    answer_lab['text'] = 'Answer: '
    answer_lab['text'] += ' ' + total_num


def minus_func(event):
    try:
        num1, num2 = float(entry_line_one.get()), float(entry_line_two.get())
    except Exception:
        answer_lab["text"] = "Ошибка. Исправьте значения чисел."
        return minus_func
    total_num = str("{:.2f}".format(num1 - num2))
    answer_lab['text'] = 'Answer: '
    answer_lab['text'] += ' ' + total_num


def times_func(event):
    try:
        num1, num2 = float(entry_line_one.get()), float(entry_line_two.get())
    except Exception:
        answer_lab["text"] = "Ошибка. Исправьте значения чисел."
        return times_func
    total_num = str("{:.2f}".format(num1 * num2))
    answer_lab['text'] = 'Answer: '
    answer_lab['text'] += ' ' + total_num


def divide_func(event):
    try:
        num1, num2 = float(entry_line_one.get()), float(entry_line_two.get())
    except Exception:
        answer_lab["text"] = "Ошибка. Исправьте значения чисел."
        return divide_func
    total_num = str("{:.2f}".format(num1 / num2))
    answer_lab['text'] = 'Answer: '
    answer_lab['text'] += ' ' + total_num
    
def pack_labels():
    entry_line_one.pack()
    entry_line_two.pack()
    plus_but.pack()
    minus_but.pack()
    times_but.pack()
    divide_but.pack()
    answer_lab.pack()
    info_lab.pack()
    copyright_lab.pack()    


plus_but = Button(root, width=10, text="+")
minus_but = Button(root, width=10, text="-")
times_but = Button(root, width=10, text="*")
divide_but = Button(root, width=10, text="/")
answer_lab = Label(root, width=40)
copyright_lab = Label(root, width=40)
info_lab = Label(root, width=40)

plus_but.bind("<Button-1>", plus_func)
minus_but.bind("<Button-1>", minus_func)
times_but.bind("<Button-1>", times_func)
divide_but.bind("<Button-1>", divide_func)

info_lab['text'] = "Числа вводить в формате 0.0"
copyright_lab['text'] = 'Calculator by Hemisaki'
answer_lab['text'] = "Answer:"

if __name__ == "__main__":
    pack_labels()
    root.mainloop()