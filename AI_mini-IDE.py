# is made by Abramov Ilya (@evoriath)
from tkinter import *


access = False
is_opened = False

def open_file():
    global access, is_opened
    access = False
    try:
        access = True
        is_opened = True
        filename = entry_widget.get()
        f = open(filename, encoding='utf-8')
        s = f.read()
        text.delete(1.0, END)
        text.insert(1.0, s)
        f.close()
        save_button['text'] = 'Сохранить'
        save_button['background'] = 'white'
    except Exception:
        access = False
        is_opened = False
        text.delete(1.0, END)
        text.insert(1.0, "Внимание! Ошибка.\n")
        text.insert(2.0, "Указанный файл не обнаружен в локальной директории.\n")
        text.insert(3.0, "Укажите нужный файл заново.")
        save_button['text'] = "ERROR"
        save_button['background'] = 'red'

def save_file():
    global access, opened
    filecode = text.get(1.0, END)
    filename = entry_widget.get()
    if len(filename) > 0:
        access = True
    if access and is_opened:
        save_button['text'] = 'Сохранено'
        save_button['background'] = "lightgreen"
        filename = 'new_' + filename
        my_file = open(filename, "w+")
        my_file.write(filecode)
        my_file.close()
        text.delete(1.0, END)
        text.insert(1.0, f"Файл {filename} был успешно сохранён.\n")
        text.insert(2.0, "Он находится в локальной директории.")
    else:
        save_button['text'] = "ERROR"
        save_button['background'] = 'red'        
        text.delete(1.0, END)
        text.insert(1.0, "Было задано пустое имя файла.\n")
        text.insert(2.0, "Сохранение невозможно.\n")
        text.insert(3.0, "Попробуйте снова.")
    

root = Tk()
top_frame = LabelFrame(root, text="Опции")
bottom_frame = LabelFrame(root, text="Текст файла / код программы.")

top_frame.pack()
bottom_frame.pack()

copyright_label = Label(top_frame, text="mini-IDE by Abramov Ilya ©")
copyright_label.pack(side=LEFT)
entry_widget = Entry(top_frame, width=20)
entry_widget.pack(side=LEFT, padx=2)
open_button = Button(top_frame, text="Открыть", command=open_file)
open_button.pack(side=LEFT)

save_button = Button(top_frame, text="Сохранить", command=save_file)
save_button.pack(side=LEFT, padx=1)

text = Text(bottom_frame)
y_scroll = Scrollbar(bottom_frame, command=text.yview)

text.pack(side=LEFT, expand=1)
text.config(yscrollcommand = y_scroll.set)

y_scroll.pack(side=LEFT, fill=Y)
root.mainloop()

