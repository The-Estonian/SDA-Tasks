import os
import time
import random as rand


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
#    3:61
##################################################################################################################

def grid_move():
    os.system("cls")
    grid_index = {
        "key_a3" : 61,
        "key_a2" : 66,
        "key_a1" : 71,
        "key_a"  : 76,
        "key_b"  : 81,
        "key_c"  : 86,
        "key_d"  : 91,
        "key_e"  : 96,
        "key_f"  : 101,
        "key_g"  : 106,
        "key_h"  : 111,
        "key_j"  : 116,
        "key_k"  : 121,
        "key_m"  : 126,
        "key_n"  : 131,
        "key_p"  : 136,
        "key_q"  : 141,
        "key_r"  : 146,
        "key_s"  : 151,
        "key_t"  : 156,
        "key_u"  : 161,
        "key_v"  : 166,
        "key_w"  : 171,
        "key_w1" : 176}

    for _ in range(37):
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
        
        
grid_move()
