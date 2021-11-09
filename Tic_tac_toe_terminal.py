"""
https://en.wikipedia.org/wiki/Box-drawing_character
https://en.wikipedia.org/wiki/List_of_Unicode_characters

https://www.w3schools.com/python/python_ref_set.asp
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/module_random.asp

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

# Empty grid and X, O icons.
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
# Imports, Random: "cls" in "os" module to increase readability in game by clearing terminal. Randint for Bot.
import os
import random as rand
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

# Class Box() to fill the grid based on answers
class Box():
   """
   Class Box(integer, string) takes 2 variables:
   integer with value 1-9 to choose a box from the grid
   string with value X or O to insert the value to choosen box
   
   """

   def __init__(self, box_num, player):
      self.player = player
      self.box_num = box_num
      if self.box_num == 1:
         self.box_1()
      if self.box_num == 2:
         self.box_2()
      if self.box_num == 3:
         self.box_3()
      if self.box_num == 4:
         self.box_4()
      if self.box_num == 5:
         self.box_5()
      if self.box_num == 6:
         self.box_6()
      if self.box_num == 7:
         self.box_7()
      if self.box_num == 8:
         self.box_8()
      if self.box_num == 9:
         self.box_9()

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
   def box_2(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:13] + a1[:8] + b[21:]
         c = c[:13] + a2[:8] + c[21:]
         d = d[:13] + a3[:8] + d[21:]
         f = f[:13] + a4[:8] + f[21:]
      if self.player == "X":
         b = b[:13] + b1[:8] + b[21:]
         c = c[:13] + b2[:8] + c[21:]
         d = d[:13] + b3[:8] + d[21:]
         f = f[:13] + b4[:8] + f[21:]

   # 3rd box function to switch value to O or X
   def box_3(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:24] + a1[:8] + b[32:]
         c = c[:24] + a2[:8] + c[32:]
         d = d[:24] + a3[:8] + d[32:]
         f = f[:24] + a4[:8] + f[32:]
      if self.player == "X":
         b = b[:24] + b1[:8] + b[32:]
         c = c[:24] + b2[:8] + c[32:]
         d = d[:24] + b3[:8] + d[32:]
         f = f[:24] + b4[:8] + f[32:]

   # 4th box function to switch value to O or X
   def box_4(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:2] + a1[0:8] + h[10:]
         i = i[:2] + a2[0:8] + i[10:]
         j = j[:2] + a3[0:8] + j[10:]
         k = k[:2] + a4[0:8] + k[10:]
      if self.player == "X":
         h = h[:2] + b1[0:8] + h[10:]
         i = i[:2] + b2[0:8] + i[10:]
         j = j[:2] + b3[0:8] + j[10:]
         k = k[:2] + b4[0:8] + k[10:]

   # 5th box function to switch value to O or X
   def box_5(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:13] + a1[:8] + h[21:]
         i = i[:13] + a2[:8] + i[21:]
         j = j[:13] + a3[:8] + j[21:]
         k = k[:13] + a4[:8] + k[21:]
      if self.player == "X":
         h = h[:13] + b1[:8] + h[21:]
         i = i[:13] + b2[:8] + i[21:]
         j = j[:13] + b3[:8] + j[21:]
         k = k[:13] + b4[:8] + k[21:]

   # 6th box function to switch value to O or X
   def box_6(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:24] + a1[:8] + h[32:]
         i = i[:24] + a2[:8] + i[32:]
         j = j[:24] + a3[:8] + j[32:]
         k = k[:24] + a4[:8] + k[32:]
      if self.player == "X":
         h = h[:24] + b1[:8] + h[32:]
         i = i[:24] + b2[:8] + i[32:]
         j = j[:24] + b3[:8] + j[32:]
         k = k[:24] + b4[:8] + k[32:]

   # 7th box function to switch value to O or X
   def box_7(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:2] + a1[0:8] + n[10:]
         p = p[:2] + a2[0:8] + p[10:]
         q = q[:2] + a3[0:8] + q[10:]
         r = r[:2] + a4[0:8] + r[10:]
      if self.player == "X":
         n = n[:2] + b1[0:8] + n[10:]
         p = p[:2] + b2[0:8] + p[10:]
         q = q[:2] + b3[0:8] + q[10:]
         r = r[:2] + b4[0:8] + r[10:]

   # 8th box function to switch value to O or X
   def box_8(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:13] + a1[:8] + n[21:]
         p = p[:13] + a2[:8] + p[21:]
         q = q[:13] + a3[:8] + q[21:]
         r = r[:13] + a4[:8] + r[21:]
      if self.player == "X":
         n = n[:13] + b1[:8] + n[21:]
         p = p[:13] + b2[:8] + p[21:]
         q = q[:13] + b3[:8] + q[21:]
         r = r[:13] + b4[:8] + r[21:]

   # 9th box function to switch value to O or X
   def box_9(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:24] + a1[:8] + n[32:]
         p = p[:24] + a2[:8] + p[32:]
         q = q[:24] + a3[:8] + q[32:]
         r = r[:24] + a4[:8] + r[32:]
      if self.player == "X":
         n = n[:24] + b1[:8] + n[32:]
         p = p[:24] + b2[:8] + p[32:]
         q = q[:24] + b3[:8] + q[32:]
         r = r[:24] + b4[:8] + r[32:]

      

while True:

   os.system("cls")
   
   a = "┌──────────┬──────────┬──────────┐"
   b = "│          │          │          │"
   c = "│          │          │          │"
   d = "│    1     │    2     │    3     │"
   f = "│          │          │          │"
   g = "├──────────┼──────────┼──────────┤"
   h = "│          │          │          │"
   i = "│          │          │          │"
   j = "│    4     │    5     │    6     │"
   k = "│          │          │          │"
   m = "├──────────┼──────────┼──────────┤"
   n = "│          │          │          │"
   p = "│          │          │          │"
   q = "│    7     │    8     │    9     │"
   r = "│          │          │          │"
   s = "└──────────┴──────────┴──────────┘"
   

   #print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
# Winning combinations
   winners = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [1, 4, 7],
              [2, 5, 8],
              [3, 6, 9],
              [1, 5, 9],
              [3, 5, 7]]

# Available numbers to pick
   positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Player reserved numbers
   player_x = []
   player_o = []

# Game loop
   game_mode = input("1 or 2 players?: ")
   os.system("cls")
   print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
   if game_mode == "2":
      while len(positions) > 0:
      # X player picking
         if len(player_x) <= len(player_o):
            answer = int(input("Player X please choose a box to occupy: "))
            if answer in positions:
               positions.remove(answer)
               player_x.append(answer)
               Box(answer, "X")
               os.system("cls")
               print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
            else:
               print("Number has already been taken: ")

         # Score keeper checking X players winning combinations vs score.
            set_x = set(player_x)
            for lists in winners:
               value = set(lists)
               if value.issubset(set_x):
                  print("Player X has won!")
                  positions.clear()

      # O player picking
         elif len(player_x) > len(player_o):
            answer = int(input("Player O please choose a box to occupy: "))
            
            if answer in positions:
               positions.remove(answer)
               player_o.append(answer)
               Box(answer, "O")
               os.system("cls")
               print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
            else:
               print("Number has already been taken: ")

         # Score keeper checking O players winning combinations vs score.
            set_o = set(player_o)
            for lists in winners:
               value = set(lists)
               if value.issubset(set_o):
                  print("Player O has won!")
                  positions.clear()

      quit = input("Press Enter to restart the game, else input X:  ")  
      if quit == "X":
         break
      else:
         continue
   else:
      while len(positions) > 0:
      # X player picking
         if len(player_x) <= len(player_o):
            answer = int(input("Player X please choose a box to occupy: "))
            if answer in positions:
               positions.remove(answer)
               player_x.append(answer)
               Box(answer, "X")
               os.system("cls")
               print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
            else:
               print("Number has already been taken: ")

         # Score keeper checking X players winning combinations vs score.
            set_x = set(player_x)
            for lists in winners:
               value = set(lists)
               if value.issubset(set_x):
                  print("Player X has won!")
                  positions.clear()  

      # Bot picking
         elif len(player_x) > len(player_o):
            answer = rand.randint(1, 9)
            
            if answer in positions:
               positions.remove(answer)
               player_o.append(answer)
               Box(answer, "O")
               os.system("cls")
               print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")
            else:
               print("Number has already been taken: ")

         # Score keeper checking O players winning combinations vs score.
            set_o = set(player_o)
            for lists in winners:
               value = set(lists)
               if value.issubset(set_o):
                  print("Player O has won!")
                  positions.clear()    

      quit = input("Press Enter to restart the game, else input X:  ")  
      if quit == "X":
         break
      else:
         continue
