"""Изучение композиции в Python3 (вызов класса и его полей/методов из другого
   класса. Разработка интерфеса программы.
"""
from math import ceil


width = int(input("Введите ширину помещения: "))
lenght = int(input("Введите длину помещения: "))
height = int(input("Введите высоту помещения: "))
roll_lenght = float(input("Введите длину рулона обоев: "))
roll_width = float(input("Введите длину рулона обоев: "))


class WinDoor:
    def __init__(self, x, y):
        """ Вычисляет площадь объекта дверь/окно."""
        self.square = x * y


class Room:
    def __init__(self):
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
    
    def return_wallpaper_roll(self):
        """ Возвращает кол-во рулонов обоев, необходимых для
            оклеивания комнаты.
        """
        roll_square = roll_lenght * roll_width
        roll_number = ceil(self.opt_square / roll_square)
        return roll_number
    
    
r1 = Room()
square = r1.count_main_square()
r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)
square = r1.count_main_square()
print(square)
opt_square = r1.count_optimal_square()
print(opt_square)
num = r1.return_wallpaper_roll()
print(num)


