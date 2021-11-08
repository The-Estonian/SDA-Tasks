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

# Box3 variable activator
      var3 = input("Box3: ")
      if var3 == ("X"):
         box_3("X")
      elif var3 == ("O"):
         box_3("O")

# Box4 variable activator
      var4 = input("Box4: ")
      if var4 == ("X"):
         box_4("X")
      elif var4 == ("O"):
         box_4("O")

# Box5 variable activator
      var5 = input("Box5: ")
      if var5 == ("X"):
         box_5("X")
      elif var5 == ("O"):
         box_5("O")

# Box6 variable activator
      var6 = input("Box6: ")
      if var6 == ("X"):
         box_6("X")
      elif var6 == ("O"):
         box_6("O")

# Box7 variable activator
      var7 = input("Box7: ")
      if var7 == ("X"):
         box_7("X")
      elif var7 == ("O"):
         box_7("O")

# Box8 variable activator
      var8 = input("Box8: ")
      if var8 == ("X"):
         box_8("X")
      elif var8 == ("O"):
         box_8("O")

# Box9 variable activator
      var9 = input("Box9: ")
      if var9 == ("X"):
         box_9("X")
      elif var9 == ("O"):
         box_9("O")





      os.system("cls")


      print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
      continue
