from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def main():
    """Главная функция запуска программы."""
    root = Tk()
    frame = ApplicationFrame(root)
    menu = ApplicationMenu(root, frame.text)
    root.mainloop()



class ApplicationMenu:
    """Класс Меню. Создаёт строку с кнопками меню разных видов."""
    def __init__(self, master, text):
        self.text = text
        master = self.master = master
        mainmenu = self.mainmenu = Menu(master)
        master.config(menu=mainmenu)
        filemenu = self.filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Новый", command=lambda: self.create_file())
        filemenu.add_command(label="Открыть", command=lambda: self.open_file())
        filemenu.add_command(label="Сохранить", command=lambda: self.save_file())
        filemenu.add_command(label="Очистить", command=lambda: self.clear_file())
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=lambda: self.exit_widget(master))
        
        helpmenu = self.helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Справка", command=lambda: self.help())
        helpmenu.add_command(label="О программе", command=lambda: self.info())
        
        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Помощь", menu=helpmenu)
    
    def open_file(self):
        """ Метод открытия файла."""
        filename = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                      ("PYTHON files", "*.py"),
                                      ("ALL files", "*.*")))
        try:
            f = open(filename, 'r')
            s = f.read()
            self.text.insert(1.0, s)
            f.close()
        except FileNotFoundError:
            mb.showinfo("Внимание", "Файл не был открыт.")
            
    def save_file(self):
        """ Метод сохранения файла."""
        filename = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                   ("PYTHON files", "*.py"),
                                                   ("ALL files", "*.*")))
        try:
            f = open(filename, 'w')
            s = self.text.get(1.0, END)
            f.write(s)
            f.close()
        except FileNotFoundError:
            mb.showinfo("Внимание", "Файл не был сохранён.")
            
    def clear_file(self):
        """Метод очистки текста поля ApplicationFrame.text"""
        answer = mb.askyesno("Сообщение", "Очистить файл?")
        if answer:
            self.text.delete(1.0, END)
            
    def create_file(self):
        """Метод создания файла."""
        s = self.text.get(1.0, END)
        filename = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("PYTHON files", "*.py"), 
                                        ("ALL files", "*.*")))
        try:
            f = open(filename, "w+")
            f.write(s)
            f.close()
        except FileNotFoundError:
            mb.showinfo("Внимание", "Новый файл не был создан.")
            
    def exit_widget(self, master):
        """Метод кнопки Выхода в меню."""
        master.destroy()
        
    def help(self):
        """Метод справки."""
        mb.showinfo("Помощь", """Создание файла: Файл --> Новый.
    Открытие файла: Файл --> Открыть.
    Сохранение файла: Файл --> Сохранить.
    Очистить текстовое поле: Файл --> Очистить.
    Выйти из приложения: --> Файл --> Выход.
    Открыть справку: Помощь --> Справка.
    Открыть информацию о программе: Помощь --> О программе.
                             """)

    def info(self):
        """Метод кнопки 'О программе'"""
        mb.showinfo("Справка", "Данная программа представляет собой базовый текстовый редактор файлов.")    
        



class ApplicationFrame:
    """Определяет текстовое поле, скролл и фрейм, на котором они лежат."""
    def __init__(self, master):
        self.master = master
        self.MainFrame = Frame(self.master)
        self.MainFrame.pack()
        
        self.text = Text(self.MainFrame, width=50, height=25)
        self.text.pack(side=LEFT)
        
        self.scroll = Scrollbar(self.MainFrame, command=self.text.yview)
        self.scroll.pack(side=LEFT, fill=Y)
        self.text.config(yscrollcommand=self.scroll.set)
        

if __name__ == "__main__":
    main()