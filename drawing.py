from tkinter import *


def add_window():
    global var, entry_x1, entry_x2, entry_y1, entry_y2, window
    window = Toplevel()
    window.geometry("+834+235")
    window.title("Фигура")
    
    top_frame = LabelFrame(window, text="Coords 1")
    middle_frame = LabelFrame(window, text="Coords 2")
    bottom_frame = LabelFrame(window, text="Выбор фигуры")

    top_frame.pack()
    middle_frame.pack()
    bottom_frame.pack()
    
    lab_x1 = Label(top_frame, text="x1")
    lab_x1.pack(side=LEFT)
    
    entry_x1 = Entry(top_frame, width=3)
    entry_x1.pack(side=LEFT)
    
    lab_y1 = Label(top_frame, text="y1")
    lab_y1.pack(side=LEFT)
    
    entry_y1 = Entry(top_frame, width=3)
    entry_y1.pack(side=LEFT)
    
    lab_x2 = Label(middle_frame, text="x2")
    lab_x2.pack(side=LEFT)
    
    entry_x2 = Entry(middle_frame, width=3)
    entry_x2.pack(side=LEFT) 
    
    lab_y2 = Label(middle_frame, text="y2")
    lab_y2.pack(side=LEFT)
    
    entry_y2 = Entry(middle_frame, width=3)
    entry_y2.pack(side=LEFT)
    
    var = IntVar()
    var.set(0)
    
    Radiobutton(bottom_frame, text="Прямоугольник", variable=var, value=1).pack()
    Radiobutton(bottom_frame, text="Овал", variable=var, value=2).pack(side=LEFT)
    
    button = Button(window, text="Нарисовать", command=draw_figure)
    button.pack()
    
    window.resizable(False, False)
    return draw_figure
    
    
def draw_figure():
    value = var.get()
    x1, x2 = entry_x1.get(), entry_x2.get()
    y1, y2 = entry_y1.get(), entry_y2.get()
    if value == 1:
        c.create_rectangle(x1, y1, x2, y2)
        window.after(1000, lambda: window.destroy())
    else:
        c.create_oval(x1, y1, x2, y2)
        window.after(1000, lambda: window.destroy())

root = Tk()

root.title("Прямовал")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w -= 150
h -= 150
root.geometry("300x350+{}+{}".format(w, h))

c = Canvas(root, width=300, height=300)
c['bg'] = "white"
c.pack()
btn = Button(text="Добавить фигуру", command=add_window)
btn.pack(pady=5)

root.resizable(False, False)
root.update_idletasks()

root.mainloop()