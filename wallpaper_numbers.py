""" Задача - создать GUI для соотв. задания из файла practice_6_main.py."""
from math import ceil
from tkinter import *


class WinDoor:
    def __init__(self, x, y):
        """ Вычисляет площадь объекта дверь/окно."""
        self.square = x * y


class Room:
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []
    
    def count_main_square(self):
        """ Вычисляет общую площадь стен комнаты."""
        self.square = 2 * self.height * (self.lenght + self.width)
        return self.square
    
    def add_wd(self, width, lenght):
        """ Добавляет объекты класса WinDoor в список self.wd."""
        self.wd.append(WinDoor(width, lenght)) # пример работы композиции
        
    def count_optimal_square(self):
        """ Вычисляет площадь комнаты, которую необходимо покрасить.
            Данная площадь равна разности между общей площадью стен
            комнаты и площадьми объектов окно/дверь.
        """
        self.opt_square = 2 * self.height * (self.lenght + self.width)
        for i in self.wd:
            self.opt_square -= i.square
        return self.opt_square
    
    def return_wallpaper_roll(self, roll_lenght, roll_width):
        """ Возвращает кол-во рулонов обоев, необходимых для
            оклеивания комнаты.
        """
        roll_square = roll_lenght * roll_width
        roll_number = ceil(self.opt_square / roll_square)
        return roll_number
    
    
class EntryWidget():
    def __init__(self, master, command):
        self.master = master
        self.command = getattr(self, command)
        self.numbers = []
        self.ent_w = Entry(self.master, text="Ширина", width=10)
        self.ent_l = Entry(self.master, text="Длина", width=10)
        self.ent_h = Entry(self.master, text="Высота", width=10)
        self.ent_rl = Entry(self.master, text="Длина рулона", width=10)
        self.ent_rw = Entry(self.master, text="Ширина рулона", width=10)
        self.btn = Button(self.master, text="Посчитать", width=15)
        self.lab = Label(self.master, text="Итог:", width=10, height=10)
        self.pack()
    
    def pack(self):
        Label(self.master, text="Ширина:", width=10).pack(side=TOP)
        self.ent_w.pack()
        Label(self.master, text="Длина:", width=10).pack(side=TOP)
        self.ent_l.pack()
        Label(self.master, text="Высота:", width=10).pack(side=TOP)
        self.ent_h.pack()
        Label(self.master, text="Длина рулона:", width=12).pack(side=TOP)
        self.ent_rl.pack()
        Label(self.master, text="Ширина рулона:", width=12).pack(side=TOP)
        self.ent_rw.pack()
        self.btn.pack()
        self.lab.pack(side=LEFT)
        self.btn.bind('<Button-1>', self.command)
    
    def take_numbers(self, event):
        try:
            self.lab['text'] = "Итог: "
            self.numbers = []
            self.numbers.append(int(self.ent_w.get()))
            self.numbers.append(int(self.ent_l.get()))
            self.numbers.append(int(self.ent_h.get()))
            self.numbers.append(float(self.ent_rl.get()))
            self.numbers.append(float(self.ent_rw.get()))
            return self.calculate()
        except Exception:
            return self.take_numbers
        
    def calculate(self):
        roll_lenght = self.numbers[3]
        roll_width = self.numbers[4]
        room = Room(self.numbers[0], self.numbers[1], self.numbers[2])
        room.add_wd(1, 1) # MAKE DYNAMIC
        room.add_wd(1, 2) #
        room.add_wd(1, 1) #
        room.count_optimal_square()
        result = room.return_wallpaper_roll(roll_lenght, roll_width)
        self.lab['text'] = "Итог: " + str(result)
        return self.take_numbers
        
    
root = Tk()
block = EntryWidget(root, 'take_numbers')
root.mainloop()
        
    


