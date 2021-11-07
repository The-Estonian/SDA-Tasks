from tkinter import *
import tkinter as tk
from tkinter import font

box_width = 25
box_height = 10
screen = str(box_width * 22) + "x" + str(box_height * 48)
num_count = 0
o_box = [1, 3, 5, 7]
x_box = [0, 2, 4, 6, 8]



def choice_1():
    global num_count
    if num_count in o_box:
        box_1.set("O")
        num_count += 1
    elif num_count in x_box:
        box_1.set("X")
        num_count += 1

def choice_2():
    global num_count
    if num_count in o_box:
        box_2.set("O")
        num_count += 1
    elif num_count in x_box:
        box_2.set("X")
        num_count += 1

def choice_3():
    global num_count
    if num_count in o_box:
        box_3.set("O")
        num_count += 1
    elif num_count in x_box:
        box_3.set("X")
        num_count += 1

def choice_4():
    global num_count
    if num_count in o_box:
        box_4.set("O")
        num_count += 1
    elif num_count in x_box:
        box_4.set("X")
        num_count += 1

def choice_5():
    global num_count
    if num_count in o_box:
        box_5.set("O")
        num_count += 1
    elif num_count in x_box:
        box_5.set("X")
        num_count += 1

def choice_6():
    global num_count
    if num_count in o_box:
        box_6.set("O")
        num_count += 1
    elif num_count in x_box:
        box_6.set("X")
        num_count += 1

def choice_7():
    global num_count
    if num_count in o_box:
        box_7.set("O")
        num_count += 1
    elif num_count in x_box:
        box_7.set("X")
        num_count += 1

def choice_8():
    global num_count
    if num_count in o_box:
        box_8.set("O")
        num_count += 1
    elif num_count in x_box:
        box_8.set("X")
        num_count += 1


def choice_9():
    global num_count
    if num_count in o_box:
        box_9.set("O")
        num_count += 1
    elif num_count in x_box:
        box_9.set("X")
        num_count += 1


root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(0,0)

box_1 = tk.StringVar(value = " ")
box_2 = tk.StringVar(value = " ")
box_3 = tk.StringVar(value = " ")
box_4 = tk.StringVar(value = " ")
box_5 = tk.StringVar(value = " ")
box_6 = tk.StringVar(value = " ")
box_7 = tk.StringVar(value = " ")
box_8 = tk.StringVar(value = " ")
box_9 = tk.StringVar(value = " ")


btn_top_left = tk.Button(root, textvariable = box_1, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_1)
btn_top_left.grid(row = 0, column = 0)

btn_top_middle = tk.Button(root, textvariable = box_2, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_2)
btn_top_middle.grid(row = 0, column = 1)

btn_top_right = tk.Button(root, textvariable = box_3, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_3)
btn_top_right.grid(row = 0, column = 2)

btn_middle_left = tk.Button(root, textvariable = box_4, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_4)
btn_middle_left.grid(row = 1, column = 0)

btn_middle_middle = tk.Button(root, textvariable = box_5, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_5)
btn_middle_middle.grid(row = 1, column = 1)

btn_middle_right = tk.Button(root, textvariable = box_6, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_6)
btn_middle_right.grid(row = 1, column = 2)

btn_bottom_left = tk.Button(root, textvariable = box_7, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_7)
btn_bottom_left.grid(row = 2, column = 0)

btn_bottom_middle = tk.Button(root, textvariable = box_8, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_8)
btn_bottom_middle.grid(row = 2, column = 1)

btn_bottom_right = tk.Button(root, textvariable = box_9, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_9)
btn_bottom_right.grid(row = 2, column = 2)


root.geometry(screen)
root.mainloop()
