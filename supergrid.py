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
#                                                                   60:0
##################################################################################################################

def grid_on():
    os.system("cls")
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
    
def grid_off():
    os.system("cls")
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
            #time.sleep(0.05)
grid_on()
time.sleep(0.5)
grid_off()

