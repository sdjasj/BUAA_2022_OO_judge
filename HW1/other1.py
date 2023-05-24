from sympy import *


def cmp(std, your, x, stdline):
    if(std != your):
        print("When x =",x, "expression is", stdline,": stdout is", std, ", yourout is", your)
        exit(0)
    else:
        return
stdout = open("data.txt", "r+")
yourout = open("output.txt", "r+")
x = Symbol("x")
for stdline in stdout:
    yourline = yourout.readline()
    str1 = "a" + "=" + "x + " + yourline
    str2 = "b" + "=" +  " x +" + stdline
    exec(str1)
    exec(str2)
    zerostd = a.evalf(subs={x:0})
    zeroyour = b.evalf(subs={x:0})
    onestd = a.evalf(subs={x:1})
    oneyour = b.evalf(subs={x:1})
    nonestd = a.evalf(subs={x:-1})
    noneyour = b.evalf(subs={x:-1})
    maxstd = a.evalf(subs={x:2147483647})
    maxyour = b.evalf(subs={x:2147483647})
    minstd = a.evalf(subs={x:-2147483647})
    minyour = b.evalf(subs={x:-2147483647})
    cmp(zerostd, zeroyour, 0, stdline)
    cmp(onestd, oneyour, 1, stdline)
    cmp(nonestd, noneyour, -1, stdline)
    cmp(maxstd, maxyour, 2147483647, stdline)
    cmp(minstd, minyour, -2147483647, stdline)
print("Success!")
