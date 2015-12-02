__author__ = '沅源'
# -*- coding:utf-8 -*-


# 简单的打字游戏，感觉面向对象这一本部分还用的不是很好
# 其中有用到观察者模式，这个游戏后续还会持续改进

from tkinter import *
from tkinter import ttk
import time
import random
import threading


class Key:

    def __init__(self, canvas, window, down_speed):
        self.posx = random.uniform(5, 595)
        self.posy = 5
        self.keyvar = random.choice([chr(i) for i in range(ord("A"),ord("Z")+1)])
        self.canvas = canvas
        self.down_speed = down_speed
        self.start_time = time.time()
        self.current_posy = 0
        self.id = 0
        self.flag = 'down'
        self.window = window
        self.window.register_key(self)

    def getposx(self):
        return self.posx

    def getchar(self):
        return self.keyvar

    def getposy(self):
        end_time = time.time()
        self.current_posy = int((end_time - self.start_time) * (1/self.down_speed))
        return self.current_posy

    def start_walk(self):
        while True:
            if self.getposy() not in range(0,590) or self.flag == 'up' :
                break
            self.walk_down(self.getposy())

    def create_key(self, current_posy):
        self.id = self.canvas.create_text(self.posx,current_posy,text= self.keyvar, font=('Helvetica', 18, 'normal'))
        return self.id

    def walk_down(self, current_posy):
        self.id = self.create_key(current_posy)
        self.canvas.update()
        time.sleep(self.down_speed)
        if self.getposy() < 590 :
            self.delete_key(self.id)
        else:
            self.window.unregister(self)

    def walk_up_thread(self):
        t = threading.Thread(target=self.walk_up)
        t.start()

    def walk_up(self):
        if self.id != 0:
            time.sleep(self.down_speed)
            self.delete_key(self.id)
        # print(self.canvas)

        while self.current_posy:

            self.id = self.create_key(self.current_posy)
            self.canvas.itemconfigure(self.id, fill='red')
            self.current_posy -= 1
            time.sleep(0.007)
            self.canvas.update()
            self.delete_key(self.id)

    def delete_key(self, id):
        self.canvas.delete(id)



class Window:

    def __init__(self, canvas):
        self.key_list = []
        self.printer_list = []
        self.lost_key = []
        self.canvas = canvas
        canvas.bind_all('<Key>',self.notify_key)

    def register_key(self, key):
        self.key_list.append(key)
        return self.key_list

    def register_printer(self, printer):
        self.printer_list.append(printer)
        return self.printer_list

    def notify_key(self,event):
        key_one = []
        printer = self.printer_list[0]

        for key in self.key_list:
            if key.getchar() == event.char:
                key_one.append(key)

        for key in key_one:
            print(key.getchar())

        if key_one:
            self.unregister((key_one[0]))
            key_one[0].flag = 'up'
            key_one[0].walk_up_thread()
            printer.update_printer(key_one[0].getchar(), True)
        else:
            printer.update_printer(event.char, False)

    def unregister(self, key):
        self.lost_key.append(key)
        # print(self.lost_key)
        self.key_list.remove(key)



class Printer(object):

    value = 0

    def __init__(self, root, window):
        self.root = root
        self.count1 = 0
        self.score = StringVar()
        self.score.set(0)
        self.level = 1
        self.count = StringVar()
        self.character = StringVar()
        self.result=StringVar()
        self.count.set(self.count1)
        self.result.set('输入结果')
        self.stage =StringVar()
        self.stage.set(self.level)
        window.register_printer(self)
        self.create_printer()

    def create_printer(self):
        style = ttk.Style()
        style.configure('mystyle.TFrame', background='white')
        frame = ttk.Frame(self.root, width=200, height=600, relief='solid', style='mystyle.TFrame')
        frame.grid_propagate(0)
        frame.grid(row=0, column=1)
        frame.grid_rowconfigure(0, weight=3)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_rowconfigure(5, weight=1)
        label = ttk.Label(frame, text='游戏说明：本游戏一共有5关，输入正确一个字母加10分，输入错误一个字母扣10分，当分数到达800分的时候会自动晋级到下一关，游戏难度随之增加', background='white', font=('Helvetica', 14, 'normal'), wraplength=180)
        label.grid(row=0, column=0,columnspan=2,padx=5,pady=10, ipadx=5, sticky=W+N )
        label = ttk.Label(frame, text='The Socre is:', background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=1, column=0,padx=5,pady=10, ipadx=5, sticky=W )
        label = ttk.Label(frame, textvariable=self.score, background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=1, column=1,padx=5,pady=10)
        label = ttk.Label(frame, text='输入字母：', background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=2, column=0,padx=5,pady=10, sticky=W)
        label = ttk.Label(frame, textvariable=self.character, background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=2, column=1,padx=5,pady=10)
        label = ttk.Label(frame, text='结果：', background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=3, column=0,padx=5,pady=10, sticky=W)
        label = ttk.Label(frame, textvariable=self.result, background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=3, column=1,padx=5,pady=10)
        label = ttk.Label(frame, text='错误次数：', background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=4, column=0,padx=5,pady=10, sticky=W)
        label = ttk.Label(frame, textvariable=self.count, background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=4, column=1,padx=5,pady=10)
        label = ttk.Label(frame, text='当前游戏难度：', background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=5, column=0,padx=5,pady=10, sticky=W)
        label = ttk.Label(frame, textvariable=self.stage, background='white', font=('Helvetica', 12, 'normal'))
        label.grid(row=5, column=1,padx=5,pady=10)

    def update_printer(self, char,flag=False):

        if flag == False:
            self.result.set('输入错误')
            Printer.value -= 1
            self.count1+=1
            self.count.set(self.count1)
            self.character.set(char)
        else:
            self.result.set('输入正确')
            Printer.value += 1
            self.character.set(char)
        # print(Printer.value)
        self.score.set(Printer.value * 10)

        if self.score.get() == str(800):
            print(self.score.get())
            self.set_level()



    def set_level(self):
        Printer.value = 0
        self.level+=1
        self.stage.set(self.level)





class TypingGame(object):
    def __init__(self, printer):
        self.dict4speed = {
            1: [2, 0.02, 2],
            2: [3, 0.01, 1],
            3: [4, 0.008, 0.8],
            4: [5, 0.005, 0.5],
            5: [7, 0.001, 0.02]
        }
        self.level = printer.level

    def start(self):

        while True:
            self.level = printer.level
            key_threading = []
            for i in range(self.dict4speed[self.level][0]):
                t = threading.Thread(target=Key(canvas, window,self.dict4speed[self.level][1]).start_walk)
                t.start()
                key_threading.append(t)
            for t_key in key_threading:
                t_key.join(self.dict4speed[self.level][2])



if __name__ == '__main__':
    root = Tk()
    root.title('Typing gaming')
    style = ttk.Style()
    style.configure('mystyle.TFrame', background='white',)
    frame = ttk.Frame(root, width=800, height=600, relief='solid',  style='mystyle.TFrame')
    frame.grid_propagate(0)
    frame.grid(row=0,column=0)

    canvas = Canvas(frame,width=800, height=600, bg='white')
    canvas.grid()

    window = Window(canvas)
    printer = Printer(root, window)

    game = TypingGame(printer)


    t = threading.Thread(target=game.start)
    t.start()

    root.mainloop()


