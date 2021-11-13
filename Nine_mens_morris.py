"""
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
import os
import time

#              0123456789          0123456789
# ===0123456789          0123456789          012345678
a3= "  ┌───────────────────────────────────────────────┐  "
a2= "  │             Welcome to the game of            │  "
a1= "┌─┴─┐                   ┌───┐                   ┌─┴─┐"
a = "│ 1 ├───────────────────┤ 2 ├───────────────────┤ 3 │"
b = "└─┬─┘                   └─┬─┘                   └─┬─┘"
c = "  │     ┌───┐           ┌─┴─┐           ┌───┐     │  "
d = "  │     │ 4 ├───────────┤ 5 ├───────────┤ 6 │     │  "
e = "  │     └─┬─┘           └─┬─┘           └─┬─┘     │  "
f = "  │       │     ┌───┐   ┌─┴─┐   ┌───┐     │       │  "
g = "  │       │     │   ├───┤   ├───┤   │     │       │  "
h = "  │       │     └─┬─┘   └─┬─┘   └─┬─┘     │       │  "
j = "┌─┴─┐   ┌─┴─┐   ┌─┴─┐           ┌─┴─┐   ┌─┴─┐   ┌─┴─┐"
k = "│   ├───┤   ├───┤   │           │   ├───┤   ├───┤   │"
m = "└─┬─┘   └─┬─┘   └─┬─┘           └─┬─┘   └─┬─┘   └─┬─┘  "
n = "  │       │       │               │       │       │  "
p = "  │       │       └───────┬───────┘       │       │  "
q = "  │       │               ┬               │       │  "
r = "  │       │               │               │       │  "
s = "  │       └───────────────┼───────────────┘       │  "
t = "  │                       ┬                       │  "
u = "  │                       │                       │  "
v = "  └───────────────────────┴───────────────────────┘  "
w = "└─┬─┘                                                     "
def grid_move():
    num = 0
    for _ in range(51):
        num += 1
        os.system("cls")
        print(a3[:num])
        print(a2[:num])
        print(a1[:num])
        print(a[:num])
        print(b[:num])
        print(c[:num])
        print(d[:num])
        print(e[:num])
        print(f[:num])
        print(g[:num])
        print(h[:num])
        print(j[:num])
        print(k[:num])
        print(m[:num])
        print(n[:num])
        print(p[:num])
        print(q[:num])
        print(r[:num])
        print(s[:num])
        print(t[:num])
        print(u[:num])
        print(v[:num])
        








grid_move()

# def fresh_grid():
#    os.system("cls")
#    print(f"{a3}\n{a2}\n{a1}\n{a}\n{b}\n{c}\n{d}\n{f}\n{e}\n{g}\n{h}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}\n{t}\n{u}\n{v}")

# fresh_grid()