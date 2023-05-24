import random

def average(alist:list):
    ans = 0
    for ele in alist:
        ans += ele
    return ans / len(alist)

def var1(alist:list):
    aver = average(alist)
    ans = 0
    for ele in alist:
        ans += (ele - aver) * (ele - aver)
    return int(ans / len(alist))

def var2(alist:list):
    aver = average(alist)
    ans = 0
    for ele in alist:
        ans += ele*ele
    ans = ans / len(alist)
    ans = ans - aver * aver
    return int(ans)

def average2(alist:list):
    ans = 0
    for ele in alist:
        ans += ele
    return ans // len(alist)

def var21(alist:list):
    aver = average2(alist)
    ans = 0
    for ele in alist:
        ans += (ele - aver) * (ele - aver)
    return ans // len(alist)

def var22(alist:list):
    aver = average2(alist)
    ans = 0
    for ele in alist:
        ans += ele*ele
    ans = ans // len(alist)
    ans = ans - aver * aver
    return ans

def varD(alist:list):
    aver = average2(alist)
    anspow = 0
    anssum = 0
    for ele in alist:
        anspow += ele * ele
        anssum += ele
    return (anspow - 2 * aver * anssum + len(alist) * aver * aver) // len(alist)


for _ in range(100000):
    alist = []
    for i in range(10):
        alist.append(random.randint(1, 200))
    Dx1 = var1(alist)
    Dx21 = var21(alist)
    print(var21(alist))
    DxDDD = varD(alist)
    print(DxDDD)
    if (Dx21 != DxDDD):
        print("WA")
        break