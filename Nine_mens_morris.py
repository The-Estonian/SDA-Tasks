"""
https://unicode-table.com/en/#basic-latin
😀😜🔥🧊

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

a10 = " 1 "
a11 = " 2 "


class Box():

   def __init__(self, box_num, player):
      self.player = player
      self.box_num = box_num
      if self.box_num == 1:
         self.box_1()
    
    # 1st box function to switch
   def box_1(self):
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

def grid_move():
   os.system("cls")
   num = 0
   for _ in range(61):
      num += 1
      print(f"{a3[:num]})
   for _ in range(61):
      num +=1
      print(f"{a2[:num]})
   for _ in range(61):
      num +=1
      print(f"{a1[:num]})



      #   \n{a2[:num]}\n{a1[:num]}\n{a[:num]}\n{b[:num]}\n{c[:num]}\n{d[:num]}\n{e[:num]}\
      #       \n{f[:num]}\n{g[:num]}\n{h[:num]}\n{j[:num]}\n{k[:num]}\n{m[:num]}\n{n[:num]}\n{p[:num]}\
      #       \n{q[:num]}\n{r[:num]}\n{s[:num]}\n{t[:num]}\n{u[:num]}\n{v[:num]}\n{w[:num]}\n{w1[:num]}")


##################################################################################################################

def grid_refresh():
    os.system("cls")
    print(f"{a3}\n{a2}\n{a1}\n{a}\n{b}\n{c}\n{d}\n{e}\
    \n{f}\n{g}\n{h}\n{j}\n{k}\n{m}\n{n}\n{p}\
    \n{q}\n{r}\n{s}\n{t}\n{u}\n{v}\n{w}\n{w1}")

##################################################################################################################
while True:
   os.system("cls")
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

   if game_mode == "X":
      os.system("cls")
      break
   elif game_mode == "1":
      grid_refresh()
      time.sleep(3)
   elif game_mode == "3":
      os.system("cls")
      print(rules)
      into_menu = input("To continue press Enter")
      if into_menu == "":
         continue
      else:
         continue
# def fresh_grid():
#    os.system("cls")
#    print(f"{a3}\n{a2}\n{a1}\n{a}\n{b}\n{c}\n{d}\n{f}\n{e}\n{g}\n{h}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}\n{t}\n{u}\n{v}")

# fresh_grid()