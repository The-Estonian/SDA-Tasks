from tkinter import *
import tkinter as tk

box_width = 25
box_height = 10
screen = str(box_width * 22) + "x" + str(box_height * 48)


















def choice_name():
    box_value.set("X")



root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(0,0)
box_value = tk.StringVar()


btn_top_left = tk.Button(root, textvariable = box_value, width = box_width, height = box_height, fg = "red", bg = "white", command = choice_name())
btn_top_left.grid(row = 0, column = 0)

btn_top_middle = tk.Button(root, text = "Top Middle", width = box_width, height = box_height, fg = "red", bg = "white")
btn_top_middle.grid(row = 0, column = 1)

btn_top_right = tk.Button(root, text = "Top Right", width = box_width, height = box_height, fg = "red", bg = "white")
btn_top_right.grid(row = 0, column = 2)

btn_middle_left = tk.Button(root, text = "Middle Left", width = box_width, height = box_height, fg = "red", bg = "white")
btn_middle_left.grid(row = 1, column = 0)

btn_middle_middle = tk.Button(root, text = "Middle Middle", width = box_width, height = box_height, fg = "red", bg = "white")
btn_middle_middle.grid(row = 1, column = 1)

btn_middle_right = tk.Button(root, text = "Middle Right", width = box_width, height = box_height, fg = "red", bg = "white")
btn_middle_right.grid(row = 1, column = 2)

btn_bottom_left = tk.Button(root, text = "Bottom Left", width = box_width, height = box_height, fg = "red", bg = "white")
btn_bottom_left.grid(row = 2, column = 0)

btn_bottom_middle = tk.Button(root, text = "Bottom Middle", width = box_width, height = box_height, fg = "red", bg = "white")
btn_bottom_middle.grid(row = 2, column = 1)

btn_bottom_right = tk.Button(root, text = "Bottom Right", width = box_width, height = box_height, fg = "red", bg = "white")
btn_bottom_right.grid(row = 2, column = 2)

root.geometry(screen)
root.mainloop()
