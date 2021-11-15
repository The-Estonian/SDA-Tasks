"""
https://unicode-table.com/en/#basic-latin
 🔴 🔵 🟠 🟡 🟢 🟣 🟤 

┌───────────────────────────┐
│     Nine men's morris     │ 
│───────────────────────────│
│ 1 = Player vs Player      │
├───────────────────────────┤
│ 2 = Player vs Bot         │
├───────────────────────────┤
│ 3 = Rule set              │
├───────────────────────────┤
│ X = Exit game             │
├───────────────────────────┤
│                           │
└───────────────────────────┘
                  , end='\033[F\033[A   │ Pick your morris: '
"""

rules = """
# Rules
##############################################################################################################
# The board consists of a grid with twenty-four intersections or points. Each player has nine pieces,        #
# or "men", usually coloured black and white. Players try to form 'mills'—three of their own men lined       #
# horizontally or vertically—allowing a player to remove an opponent's man from the game.                    #
# A player wins by reducing the opponent to two pieces (where they could no longer form mills                #
# and thus be unable to win), or by leaving them without a legal move.                                       #
##############################################################################################################
# The game proceeds in three phases:                                                                         #
#                                                                                                            #
#    Placing men on vacant points                                                                            #
#    Moving men to adjacent points                                                                           #
#    (optional phase) Moving men to any vacant point when the player has been reduced to three men           #
##############################################################################################################
# Phase 1: Placing pieces                                                                                    #
#                                                                                                            #
# Nine men's morris starts on an empty board.                                                                #
# The game begins with an empty board. The players determine who plays first, then take turns placing their  #
# men one per play on empty points. If a player is able to place three of their pieces on contiguous points  #
# in a straight line, vertically or horizontally, they have formed a mill and may remove one of their        #
# opponent's pieces from the board and the game, with the caveat that a piece in an opponent's mill can      #
# only be removed if no other pieces are available. After all men have been placed, phase two begins.        #
##############################################################################################################
# Phase 2: Moving pieces                                                                                     #
#                                                                                                            #
# Players continue to alternate moves, this time moving a man to an adjacent point.                          #
# A piece may not "jump" another piece. Players continue to try to form mills and remove their               #
# opponent's pieces as in phase one. A player can "break" a mill by moving one of his pieces                 #
# out of an existing mill, then moving it back to form the same mill a second time (or any number of times), #
# each time removing one of his opponent's men.                                                              #
# The act of removing an opponent's man is sometimes called "pounding" the opponent.                         #
# When one player has been reduced to three men, phase three begins.                                         #
##############################################################################################################
# Phase 3: "Flying"                                                                                          #
#                                                                                                            #
# When a player is reduced to three pieces, there is no longer a limitation on that player of moving to      #
# only adjacent points: The player's men may "fly" (or "hop" or "jump") from any point to any vacant point.  #
##############################################################################################################
"""
import os
import time

icon_1 = "🔴"
icon_2 = "🟡"
icon_3 = "🟠" 
icon_4 = "🟢"
icon_5 = "🟣"
icon_6 = "🟤"
icon_7 = "🔵"

player_1_icon = "🔴"
player_2_icon = "🟡"

class Box():

   def __init__(self, box_num, player):
      self.player = player
      self.box_num = box_num
      if self.box_num == 1:
         self.box_1()
      elif self.box_num == 2:
         self.box_2()
      elif self.box_num == 3:
         self.box_3()
      elif self.box_num == 4:
         self.box_4()
      elif self.box_num == 5:
         self.box_5()
      elif self.box_num == 6:
         self.box_6()
      elif self.box_num == 7:
         self.box_7()
      elif self.box_num == 8:
         self.box_8()
      elif self.box_num == 9:
         self.box_9()
      elif self.box_num == 10:
         self.box_10()
      elif self.box_num == 11:
         self.box_11()
      elif self.box_num == 12:
         self.box_12()
      elif self.box_num == 13:
         self.box_13()
      elif self.box_num == 14:
         self.box_14()
      elif self.box_num == 15:
         self.box_15()
      elif self.box_num == 16:
         self.box_16()
      elif self.box_num == 17:
         self.box_17()
      elif self.box_num == 18:
         self.box_18()
      elif self.box_num == 19:
         self.box_19()
      elif self.box_num == 20:
         self.box_20()
      elif self.box_num == 21:
         self.box_21()
      elif self.box_num == 22:
         self.box_22()
      elif self.box_num == 23:
         self.box_23()
      elif self.box_num == 24:
         self.box_24()          

   # 1st box function to switch - done
   def box_1(self):
      global a
      empty = " 1 "
      reserv_spot = "1"
      if self.player == "1":
         reserv_spot = player_1_icon
      elif self.player == "2":
         reserv_spot = player_2_icon
      elif self.player == "empty":
         reserv_spot = empty
      a = a[0:5] + reserv_spot + a[7:]


   # 2nd box function to switch
   def box_2(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 3rd box function to switch
   def box_3(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 4th box function to switch
   def box_4(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 5th box function to switch
   def box_5(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 6th box function to switch
   def box_6(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 7th box function to switch
   def box_7(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 8th box function to switch
   def box_8(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 9th box function to switch
   def box_9(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 10th box function to switch
   def box_10(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 11th box function to switch
   def box_11(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 12th box function to switch
   def box_12(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 13th box function to switch
   def box_13(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 14th box function to switch
   def box_14(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 15th box function to switch
   def box_15(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 16th box function to switch
   def box_16(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 17 box function to switch
   def box_17(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 18th box function to switch
   def box_18(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 19th box function to switch
   def box_19(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 20th box function to switch
   def box_20(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 21st box function to switch
   def box_21(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 22nd box function to switch
   def box_22(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 23rd box function to switch
   def box_23(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]
   # 24th box function to switch
   def box_24(self):
      global a
      if self.player == "1":
         a = a[0:5] + a10 + a[8:]
      if self.player == "2":
         a = a[0:5] + a11 + a[8:]


#              0123456789          0123456789          0123456789
# ===0123456789          0123456789          0123456789          1
a3= "┌───────────────────────────────────────────────────────────┐"
a2= "│         Welcome to the game of Nine men's Morris          │"
a1= "│   ┌───┐                   ┌───┐                   ┌───┐   │"
a = "│   │ 1 ├───────────────────┤ 2 ├───────────────────┤ 3 │   │"
b = "│   └─┬─┘                   └─┬─┘                   └─┬─┘   │"
c = "│     │     ┌───┐           ┌─┴─┐           ┌───┐     │     │"
d = "│     │     │ 4 ├───────────┤ 5 ├───────────┤ 6 │     │     │"
e = "│     │     └─┬─┘           └─┬─┘           └─┬─┘     │     │"
f = "│     │       │     ┌───┐   ┌─┴─┐   ┌───┐     │       │     │"
g = "│     │       │     │ 7 ├───┤ 8 ├───┤ 9 │     │       │     │"
h = "│     │       │     └─┬─┘   └───┘   └─┬─┘     │       │     │"
j = "│   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐           ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   │"
k = "│   │ 10├───┤ 11├───┤ 12│           │ 13├───┤ 14├───┤ 15│   │"
m = "│   └─┬─┘   └─┬─┘   └─┬─┘           └─┬─┘   └─┬─┘   └─┬─┘   │"
n = "│     │       │     ┌─┴─┐   ┌───┐   ┌─┴─┐     │       │     │"
p = "│     │       │     │ 16├───┤ 17├───┤ 18│     │       │     │"
q = "│     │       │     └───┘   └─┬─┘   └───┘     │       │     │"
r = "│     │     ┌─┴─┐           ┌─┴─┐           ┌─┴─┐     │     │"
s = "│     │     │ 19├───────────┤ 20├───────────┤ 21│     │     │"
t = "│     │     └───┘           └─┬─┘           └───┘     │     │"
u = "│   ┌─┴─┐                   ┌─┴─┐                   ┌─┴─┐   │"
v = "│   │ 22├───────────────────┤ 23├───────────────────┤ 24│   │"
w = "│   └───┘                   └───┘                   └───┘   │"
w1= "└───────────────────────────────────────────────────────────┘"

##################################################################################################################

class Grid:
   def __init__(self, var):
      self.var = var
      if self.var == "on":
         self.grid_on()
      elif self.var == "off":
         self.grid_off()
      elif self.var == "both":
         self.grid_off()
         time.sleep(1)
         self.grid_on()

   def grid_on(self):
      grid_index = {
         "key_a3" : 60,
         "key_a2" : 65,
         "key_a1" : 70,
         "key_a"  : 75,
         "key_b"  : 80,
         "key_c"  : 85,
         "key_d"  : 90,
         "key_e"  : 95,
         "key_f"  : 100,
         "key_g"  : 105,
         "key_h"  : 110,
         "key_j"  : 115,
         "key_k"  : 120,
         "key_m"  : 125,
         "key_n"  : 130,
         "key_p"  : 135,
         "key_q"  : 140,
         "key_r"  : 145,
         "key_s"  : 150,
         "key_t"  : 155,
         "key_u"  : 160,
         "key_v"  : 165,
         "key_w"  : 170,
         "key_w1" : 175}
      for _ in range(35):
         for key, value in grid_index.items():
               if value > 0:
                  grid_index[key] -= 5
               elif value <0:
                  grid_index[key] = 0
         os.system("cls")  
         print(f"""{a3[grid_index["key_a3"]:]}\n{a2[grid_index["key_a2"]:]}\n{a1[grid_index["key_a1"]:]}\n{a[grid_index["key_a"]:]}\
               \n{b[grid_index["key_b"]:]}\n{c[grid_index["key_c"]:]}\n{d[grid_index["key_d"]:]}\n{e[grid_index["key_e"]:]}\
               \n{f[grid_index["key_f"]:]}\n{g[grid_index["key_g"]:]}\n{h[grid_index["key_h"]:]}\n{j[grid_index["key_j"]:]}\
               \n{k[grid_index["key_k"]:]}\n{m[grid_index["key_m"]:]}\n{n[grid_index["key_n"]:]}\n{p[grid_index["key_p"]:]}\
               \n{q[grid_index["key_q"]:]}\n{r[grid_index["key_r"]:]}\n{s[grid_index["key_s"]:]}\n{t[grid_index["key_t"]:]}\
               \n{u[grid_index["key_u"]:]}\n{v[grid_index["key_v"]:]}\n{w[grid_index["key_w"]:]}\n{w1[grid_index["key_w1"]:]}""")
         time.sleep(0.02)

   def grid_off(self):
      grid_index = {
         "key_a3" : 0,
         "key_a2" : 0,
         "key_a1" : 0,
         "key_a"  : 0,
         "key_b"  : 0,
         "key_c"  : 0,
         "key_d"  : 0,
         "key_e"  : 0,
         "key_f"  : 0,
         "key_g"  : 0,
         "key_h"  : 0,
         "key_j"  : 0,
         "key_k"  : 0,
         "key_m"  : 0,
         "key_n"  : 0,
         "key_p"  : 0,
         "key_q"  : 0,
         "key_r"  : 0,
         "key_s"  : 0,
         "key_t"  : 0,
         "key_u"  : 0,
         "key_v"  : 0,
         "key_w"  : 0,
         "key_w1" : 0}

      for _ in range(1):
         for key, value in grid_index.items():
               grid_index[key] += 61
         
               os.system("cls")  
               print(f"""{a3[grid_index["key_a3"]:]}\n{a2[grid_index["key_a2"]:]}\n{a1[grid_index["key_a1"]:]}\n{a[grid_index["key_a"]:]}\
                  \n{b[grid_index["key_b"]:]}\n{c[grid_index["key_c"]:]}\n{d[grid_index["key_d"]:]}\n{e[grid_index["key_e"]:]}\
                  \n{f[grid_index["key_f"]:]}\n{g[grid_index["key_g"]:]}\n{h[grid_index["key_h"]:]}\n{j[grid_index["key_j"]:]}\
                  \n{k[grid_index["key_k"]:]}\n{m[grid_index["key_m"]:]}\n{n[grid_index["key_n"]:]}\n{p[grid_index["key_p"]:]}\
                  \n{q[grid_index["key_q"]:]}\n{r[grid_index["key_r"]:]}\n{s[grid_index["key_s"]:]}\n{t[grid_index["key_t"]:]}\
                  \n{u[grid_index["key_u"]:]}\n{v[grid_index["key_v"]:]}\n{w[grid_index["key_w"]:]}\n{w1[grid_index["key_w1"]:]}""")
               time.sleep(0.02)

##################################################################################################################

def grid_refresh():
    os.system("cls")
    print(f"{a3}\n{a2}\n{a1}\n{a}\n{b}\n{c}\n{d}\n{e}\
    \n{f}\n{g}\n{h}\n{j}\n{k}\n{m}\n{n}\n{p}\
    \n{q}\n{r}\n{s}\n{t}\n{u}\n{v}\n{w}\n{w1}")

##################################################################################################################
allocatable_numbers = ["1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9", "10", "11", "12",\
                      "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
player_1 = []
player_2 = []

while True:
   os.system("cls")

   # Game options
   print("""
   ┌───────────────────────────┐
   │     Nine men's morris     │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   ├───────────────────────────┤
   │ 3 = Rule set              │
   ├───────────────────────────┤
   │ X = Exit game             │
   ├───────────────────────────┤
   │                           │
   └───────────────────────────┘
                     """, end='\033[F\033[A   │ Pick your morris: ')
   game_mode = input()

   # Option X - Exit game
   if game_mode == "X":
      os.system("cls")
      break
   # Option 1 - Player vs Player
   elif game_mode == "1":
      Grid("on")
      while len(allocatable_numbers) > 0: 
         picking_variable = str(input("Please pick a box: "))
         if picking_variable in allocatable_numbers:
            if picking_variable == "1":
               Box(1, "1")
               player_1.append(picking_variable)
               grid_refresh()
            elif picking_variable == "2":
               Box(1, "2")
               player_2.append(picking_variable)
               grid_refresh()
            elif picking_variable == "3":
               Box(1, "empty")
               grid_refresh()
            time.sleep(1)
         else:
            print("Number already taken!")
   # Option 2 - Player vs Bot - In To-Do list
   elif game_mode == "2":
      os.system("cls")
      print("Player vs bot - in To-Do list")
      into_menu = input("To continue press Enter")
      if into_menu == "":
         continue
      else:
         continue
   # Option 3 - Game Rules
   elif game_mode == "3":
         os.system("cls")
         print(rules)
         into_menu = input("To continue press Enter")
         if into_menu == "":
            continue
         else:
            continue
   # Random text warning
   else:
      print("\n     Please enter a valid mode")
      time.sleep(0.5)



