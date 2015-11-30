__author__ = '沅源'
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import random
import threading



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

    def getchar(self):
        return self.keyvar

    def getposy(self):
        end_time = time.time()
        self.current_posy = int((end_time - self.start_time) * (1/self.down_speed))
        return self.current_posy

    def start_walk(self):
        while True:
            if self.getposy() not in range(0,595) or self.flag == 'up' :
                break
            self.walk_down(self.getposy())

    def create_key(self, current_posy):
        self.id = self.canvas.create_text(self.posx,current_posy,text= self.keyvar)
        return self.id

    def walk_down(self, current_posy):
        self.id = self.create_key(current_posy)
        self.canvas.update()
        time.sleep(self.down_speed)
        if self.getposy() != 595 and self.flag == 'down':
            self.delete_key(self.id)
        else:
            self.window.unregister(self)



    def walk_up_thread(self):
        t = threading.Thread(target=self.walk_up)
        t.start()

    def walk_up(self):
        self.delete_key(self.id)
        # print(self.canvas)
        while self.current_posy:
            self.id = self.create_key(self.current_posy)
            self.current_posy -= 1
            time.sleep(self.down_speed)
            self.canvas.update()
            self.delete_key(self.id)

    def delete_key(self, id):
        self.canvas.delete(id)



class Window:

    def __init__(self, canvas):
        self.key_list = []

        canvas.bind_all('<Key>',self.getinputfromkeyborad)

    def register(self, key):
        self.key_list.append(key)
        print(self.key_list)
        return self.key_list

    def getinputfromkeyborad(self,event):
        key_one = []
        for key in self.key_list:
            if key.getchar() == event.char:
                key_one.append(key)
        print(key_one)
        if key_one:
            # self.unregister(key_one[0])

            key_one[0].flag = 'up'
            key_one[0].walk_up_thread()

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

    window = Window(canvas)

    for i in range(5):
        t = threading.Thread(target=Key(canvas,window).start_walk)
        t.start()
    root.mainloop()



