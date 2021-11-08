"""
https://en.wikipedia.org/wiki/Box-drawing_character
https://en.wikipedia.org/wiki/List_of_Unicode_characters
https://www.w3.org/TR/xml-entity-names/025.html



"""

#this is the speical char list
#symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
#print(symbols)

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


   ⏤
      
 ⎛   ⎞
 
 ⎝   ⎠
   ⏤




⌛⏳

"""

"""
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
# Imports
import os

# Basic empty grid
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

# 1st box function to switch value to O or X
def box_1(var_var1):
   global b, c, d, f
   if var_var1 == "O":
      b = b[:2] + a1[0:8] + b[10:]
      c = c[:2] + a2[0:8] + c[10:]
      d = d[:2] + a3[0:8] + d[10:]
      f = f[:2] + a4[0:8] + f[10:]
   if var_var1 == "X":
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
      b = b[:3] + b1[:8] + b[10:]
      c = c[:3] + b2[:8] + c[10:]
      d = d[:3] + b3[:8] + d[10:]
      f = f[:3] + b4[:8] + f[10:]
      

while True:

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

    
# Continuous terminal clear/print new table loop
   while True:
      os.system("cls")
      print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")

# Box1 variable activator
      var1 = input("Box1: ")
      if var1 == "X":
         box_1("X")
      elif var1 == "O":
         box_1("O")

# Box2 variable activator
      var2 = input("Box2: ")
      if var2 == ("X"):
         box_2("X")
      elif var2 == ("O"):
         box_2("O")






      os.system("cls")


      print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
      continue
