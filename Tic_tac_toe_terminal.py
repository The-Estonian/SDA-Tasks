"""
https://en.wikipedia.org/wiki/Box-drawing_character
https://en.wikipedia.org/wiki/List_of_Unicode_characters
https://www.w3.org/TR/xml-entity-names/025.html

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

"""
grid = """
┌──────────┬──────────┬──────────┐
│   ╲  ╱   │ ┌──────┐ │          │
│    ╲╱    │ │      │ │          │
│    ╱╲    │ │      │ │          │
│   ╱  ╲   │ └──────┘ │          │
├──────────┼──────────┼──────────┤
│          │          │          │
│          │          │          │
│          │          │          │
│          │          │          │
├──────────┼──────────┼──────────┤
│ ████████ │          │          │
│ ████████ │          │          │
│ ████████ │          │          │
│ ████████ │          │          │
└──────────┴──────────┴──────────┘

⌛⏳

   ⏤
      
 ⎛   ⎞
 
 ⎝   ⎠
   ⏤

╭──────╮
│      │
│      │
╰──────╯ 

   ╲  ╱
    ╲╱
    ╱╲
   ╱  ╲
"""
# Game starts here!
# Imports, "cls" in "os" module to increase readability in game by clearing terminal.
import os
from typing import _SpecialForm

# Basic empty backup grid
"""
a = "┌──────────┬──────────┬──────────┐"
b = "│          │          │          │"
c = "│          │          │          │"
d = "│          │          │          │"
f = "│          │          │          │"
g = "├──────────┼──────────┼──────────┤"
h = "│          │          │          │"
i = "│          │          │          │"
j = "│          │          │          │"
k = "│          │          │          │"
m = "├──────────┼──────────┼──────────┤"
n = "│          │          │          │"
p = "│          │          │          │"
q = "│          │          │          │"
r = "│          │          │          │"
s = "└──────────┴──────────┴──────────┘"
"""

# X value 8 spaces, 4 rows
b1 = "  ╲  ╱  "
b2 = "   ╲╱   "
b3 = "   ╱╲   "
b4 = "  ╱  ╲  "

# O value 8 spaces, 4 rows
a1 = "╭──────╮"
a2 = "│      │"
a3 = "│      │"
a4 = "╰──────╯" 

# Class?
class Box():
   def __init__(self, box_num, player):
      self.player = player
      self.box_num = box_num
      if self.box_num == 1:
         box_1()
      if self.box_num == 2:
         box_2()




   # 1st box function to switch value to O or X
   def box_1(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:2] + a1[0:8] + b[10:]
         c = c[:2] + a2[0:8] + c[10:]
         d = d[:2] + a3[0:8] + d[10:]
         f = f[:2] + a4[0:8] + f[10:]
      if self.player == "X":
         b = b[:2] + b1[0:8] + b[10:]
         c = c[:2] + b2[0:8] + c[10:]
         d = d[:2] + b3[0:8] + d[10:]
         f = f[:2] + b4[0:8] + f[10:]

   # 2nd box function to switch value to O or X
   def box_2(var_var2):
      global b, c, d, f
      if var_var2 == "O":
         b = b[:13] + a1[:8] + b[21:]
         c = c[:13] + a2[:8] + c[21:]
         d = d[:13] + a3[:8] + d[21:]
         f = f[:13] + a4[:8] + f[21:]
      if var_var2 == "X":
         b = b[:13] + b1[:8] + b[21:]
         c = c[:13] + b2[:8] + c[21:]
         d = d[:13] + b3[:8] + d[21:]
         f = f[:13] + b4[:8] + f[21:]

   # 3rd box function to switch value to O or X
   def box_3(var_var3):
      global b, c, d, f
      if var_var3 == "O":
         b = b[:24] + a1[:8] + b[32:]
         c = c[:24] + a2[:8] + c[32:]
         d = d[:24] + a3[:8] + d[32:]
         f = f[:24] + a4[:8] + f[32:]
      if var_var3 == "X":
         b = b[:24] + b1[:8] + b[32:]
         c = c[:24] + b2[:8] + c[32:]
         d = d[:24] + b3[:8] + d[32:]
         f = f[:24] + b4[:8] + f[32:]

   # 4th box function to switch value to O or X
   def box_4(var_var4):
      global h, i, j, k
      if var_var4 == "O":
         h = h[:2] + a1[0:8] + h[10:]
         i = i[:2] + a2[0:8] + i[10:]
         j = j[:2] + a3[0:8] + j[10:]
         k = k[:2] + a4[0:8] + k[10:]
      if var_var4 == "X":
         h = h[:2] + b1[0:8] + h[10:]
         i = i[:2] + b2[0:8] + i[10:]
         j = j[:2] + b3[0:8] + j[10:]
         k = k[:2] + b4[0:8] + k[10:]

   # 5th box function to switch value to O or X
   def box_5(var_var5):
      global h, i, j, k
      if var_var5 == "O":
         h = h[:13] + a1[:8] + h[21:]
         i = i[:13] + a2[:8] + i[21:]
         j = j[:13] + a3[:8] + j[21:]
         k = k[:13] + a4[:8] + k[21:]
      if var_var5 == "X":
         h = h[:13] + b1[:8] + h[21:]
         i = i[:13] + b2[:8] + i[21:]
         j = j[:13] + b3[:8] + j[21:]
         k = k[:13] + b4[:8] + k[21:]

   # 6th box function to switch value to O or X
   def box_6(var_var6):
      global h, i, j, k
      if var_var6 == "O":
         h = h[:24] + a1[:8] + h[32:]
         i = i[:24] + a2[:8] + i[32:]
         j = j[:24] + a3[:8] + j[32:]
         k = k[:24] + a4[:8] + k[32:]
      if var_var6 == "X":
         h = h[:24] + b1[:8] + h[32:]
         i = i[:24] + b2[:8] + i[32:]
         j = j[:24] + b3[:8] + j[32:]
         k = k[:24] + b4[:8] + k[32:]

   # 7th box function to switch value to O or X
   def box_7(var_var7):
      global n, p, q, r
      if var_var7 == "O":
         n = n[:2] + a1[0:8] + n[10:]
         p = p[:2] + a2[0:8] + p[10:]
         q = q[:2] + a3[0:8] + q[10:]
         r = r[:2] + a4[0:8] + r[10:]
      if var_var7 == "X":
         n = n[:2] + b1[0:8] + n[10:]
         p = p[:2] + b2[0:8] + p[10:]
         q = q[:2] + b3[0:8] + q[10:]
         r = r[:2] + b4[0:8] + r[10:]

   # 8th box function to switch value to O or X
   def box_8(var_var8):
      global n, p, q, r
      if var_var8 == "O":
         n = n[:13] + a1[:8] + n[21:]
         p = p[:13] + a2[:8] + p[21:]
         q = q[:13] + a3[:8] + q[21:]
         r = r[:13] + a4[:8] + r[21:]
      if var_var8 == "X":
         n = h[:13] + b1[:8] + n[21:]
         p = i[:13] + b2[:8] + p[21:]
         q = j[:13] + b3[:8] + q[21:]
         r = k[:13] + b4[:8] + r[21:]

   # 9th box function to switch value to O or X
   def box_9(var_var9):
      global n, p, q, r
      if var_var9 == "O":
         n = n[:24] + a1[:8] + n[32:]
         p = p[:24] + a2[:8] + p[32:]
         q = q[:24] + a3[:8] + q[32:]
         r = r[:24] + a4[:8] + r[32:]
      if var_var9 == "X":
         n = n[:24] + b1[:8] + n[32:]
         p = p[:24] + b2[:8] + p[32:]
         q = q[:24] + b3[:8] + q[32:]
         r = r[:24] + b4[:8] + r[32:]

      

while True:

   os.system("cls")

   a = "┌──────────┬──────────┬──────────┐"
   b = "│          │          │          │"
   c = "│          │          │          │"
   d = "│          │          │          │"
   f = "│          │          │          │"
   g = "├──────────┼──────────┼──────────┤"
   h = "│          │          │          │"
   i = "│          │          │          │"
   j = "│          │          │          │"
   k = "│          │          │          │"
   m = "├──────────┼──────────┼──────────┤"
   n = "│          │          │          │"
   p = "│          │          │          │"
   q = "│          │          │          │"
   r = "│          │          │          │"
   s = "└──────────┴──────────┴──────────┘"


   print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")

   list_x = []
   list_o = []

   for _ in range(5):
      answer_x = int(input("Player X please choose a box to occupy: "))
      list_x.append(answer_x)
      Box(answer_x, "X")

   for _ in range(4):
      answer_o = int(input("Player O please choose a box to occupy: "))
      list_o.append(answer_o)
      Box(answer_o, "O")
















# for reference.

# Box1 variable activator
#      var1 = input("Box1: ")
#      if var1 == "X":
#         box_1("X")
#      elif var1 == "O":
#         box_1("O")
