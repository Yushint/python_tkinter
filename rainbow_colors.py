from tkinter import *
"""При нажатии на ту или иную кнопку в текстовое поле должен вставляться код
   цвета, а в метку – название цвета.
"""

#def main():
    #global root
    #root = Tk()
    #pack()
    #root.mainloop()

root = Tk()
    
def set_color_red():
    color_lab['text'] = "красный"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#ff0000')

def set_color_orange():
    color_lab['text'] = "оранжевый"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#ff7d00')

def set_color_yellow():
    color_lab['text'] = "жёлтый"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#ffff00')

def set_color_green():
    color_lab['text'] = "зелёный"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#00ff00')

def set_color_light_blue():
    color_lab['text'] = "голубой"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#007dff')

def set_color_blue():
    color_lab['text'] = "синий"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#0000ff')

def set_color_violet():
    color_lab['text'] = "фиолетовый"
    entry_widget.delete(0, END)
    entry_widget.insert(0, '#7d00ff')
    
    
color_lab = Label(text="Цвет", font=("Arial 32", 10))
entry_widget = Entry(width=15, justify=CENTER)

red_button = Button(bg="#ff0000", activebackground="#ff0000",
                    width=10, height=1)
red_button.config(command=set_color_red)

orange_button = Button(bg="#ff7d00", activebackground="#ff7d00",
                    width=10, height=1)
orange_button.config(command=set_color_orange)

yellow_button = Button(bg="#ffff00", activebackground="#ffff00",
                    width=10, height=1)
yellow_button.config(command=set_color_yellow)

green_button = Button(bg="#00ff00", activebackground="#00ff00",
                    width=10, height=1)
green_button.config(command=set_color_green)

light_blue_button = Button(bg="#007dff", activebackground="#007dff",
                    width=10, height=1)
light_blue_button.config(command=set_color_light_blue)

blue_button = Button(bg="#0000ff", activebackground="#0000ff",
                    width=10, height=1)
blue_button.config(command=set_color_blue)

violet_button = Button(bg="#7d00ff", activebackground="#7d00ff",
                    width=10, height=1)
violet_button.config(command=set_color_violet)

def pack():
    color_lab.pack()
    entry_widget.pack()
    red_button.pack()
    orange_button.pack()
    yellow_button.pack()
    green_button.pack()
    light_blue_button.pack()
    blue_button.pack()
    violet_button.pack()

pack()
root.mainloop()

#if __name__ == "__main__":
    #main()

