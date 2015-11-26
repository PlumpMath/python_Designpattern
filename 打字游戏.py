__author__ = '沅源'
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
import time
import random

root = Tk()
style = ttk.Style()
style.configure('mystyle.TFrame', background='white')


frame = ttk.Frame(root, width=800, height=600, style='mystyle.TFrame')
frame.grid_propagate(0)
frame.grid(row=0,column=0)

canvas = Canvas(frame,width=800, height=600, bg='white')
canvas.grid()

# button = ttk.Button(frame, width=5, text='a')
# button.grid(row=0,column=0)
# button.grid_propagate(0)
class key:


    down_speed = 0.2


    def __init__(self):
        self.posx = random.choice(range(800))
        self.posy = 5
        self.keyvar = random.choice([chr(i) for i in range(ord("A"),ord("Z")+1)])

    def create_key(self, offset):
        self.id = canvas.create_text(self.posx,key.current_posy,text= self.keyvar)
        return self.id

    def walk_down(self, flag = True):
        for i in range(60):
            if flag == False:
                return i
            id = self.create_key()
            canvas.update()
            time.sleep(key.down_speed)
            if i == 59:
                flag = False
                break
            self.delete_key(id)

    def walk_up(self, input_keyvar):
        if self.keyvar == input_keyvar:
            pass
        else:
            pass


    def delete_key(self, id):
        canvas.delete(id)

# time.sleep(1)
root.mainloop()








