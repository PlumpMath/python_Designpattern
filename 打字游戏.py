__author__ = '沅源'
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import random



# button = ttk.Button(frame, width=5, text='a')
# button.grid(row=0,column=0)
# button.grid_propagate(0)
class Key:

    def __init__(self, canvas, window, down_speed = 0.01):
        self.posx = random.choice(range(5,795))
        self.posy = 5
        self.keyvar = random.choice([chr(i) for i in range(ord("A"),ord("Z")+1)])
        self.canvas = canvas
        self.down_speed = down_speed
        self.start_time = time.time()
        self.current_posy = 0
        self.id = 0
        self.flag = 'down'
        self.window = window
        self.window.register(self)

        # window().register(self)

    def getchar(self):
        return self.keyvar

    def getposy(self):
        return self.current_posy

    def start_walk(self):
        end_time = time.time()
        self.current_posy = int((end_time - self.start_time) * (1/self.down_speed))
        self.walk_down(self.current_posy)

    def create_key(self, current_posy):
        self.id = self.canvas.create_text(self.posx,current_posy,text= self.keyvar)
        return self.id

    def walk_down(self, current_posy):
        # for i in range(60):
        self.id = self.create_key(current_posy)
        self.canvas.update()
        time.sleep(self.down_speed)
        # if self.getposy()
        if key.getposy() != 595 and key.flag == 'down':
            self.delete_key(self.id)
        else:
            self.window.unregister(self)

    def walk_up(self, current_posy):
        if self.id != 0:
            self.delete_key(self.id)

        while current_posy >= 0:
            print(current_posy)
            id = self.create_key(current_posy)
            current_posy -= 1
            time.sleep(self.down_speed)
            self.canvas.update()
            self.delete_key(id)


    def delete_key(self, id):
        self.canvas.delete(id)



class Window:

    def __init__(self):
        self.key_list = []


    def register(self, key):
        self.key_list.append(key)
        print(self.key_list)
        return self.key_list

    def getinputfromkeyborad(self,event):
        for key in self.key_list:
            if key.getchar() == event.char:
                key.flag = 'up'
                key_temp = key
                # self.unregister(key)
                key_temp.walk_up(key.getposy())

    def unregister(self, key):
        self.key_list.remove(key)


if __name__ == '__main__':
    root = Tk()
    style = ttk.Style()
    style.configure('mystyle.TFrame', background='white')


    frame = ttk.Frame(root, width=800, height=600, style='mystyle.TFrame')
    frame.grid_propagate(0)
    frame.grid(row=0,column=0)


    canvas = Canvas(frame,width=800, height=600, bg='white')
    canvas.grid()

    L = range(595)

    window = Window()
    canvas.bind_all('<Key>',window.getinputfromkeyborad)

    key = Key(canvas, window)

    while True:
        if key.getposy() not in L or key.flag == 'up' :
            break
        key.start_walk()



    root.mainloop()


