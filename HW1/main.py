from xeger import Xeger
import random

powFun = 'x( ){0}(\*\*( ){0}\+0{0}[0-4])?'
const = '(\+|-)0{0}[1-9]{1}'

x = Xeger(limit=100)
x._cases['any'] = lambda x: '.'
x._alphabets['whitespace'] = ' '

def generTermNotExp(x,notpre):
    n = random.randint(1,1)
    m = random.randint(1,3)
    s = ""
    if not notpre:
        if m==1:
            s+="+"
        elif m==2:
            s+='-'
    for i in range(n):
        if random.random()>0.5:
            s+=x.xeger(powFun)
        else:
            s+=x.xeger(const)
        if i < n - 1:
            s+="*"
    return s


def generExpNotBrac(x,notpre):
    n = random.randint(1,1)
    m = random.randint(1,3)
    s = ""
    if not notpre:
        if m==1:
            s+="+"
        elif m==2:
            s+='-'
    s+=generTermNotExp(x, False)
    for i in range(n):
        if random.random()>0.5:
            s+="+"
        else:
            s+="-"
        s+=generTermNotExp(x,True)
    return s

def generTermWithBracket(x, notpre):
    n = random.randint(2,3)
    m = random.randint(1,3)
    s = ""
    if notpre:
        if m==1:
            s+="+"
        elif m==2:
            s+='-'
    for i in range(n):
        tmp = random.random()
        if tmp > 0.80:
            s+=x.xeger(powFun)
        elif 0.60 < tmp <= 0.80:
            s+=x.xeger(const)
        elif tmp<=0.60:
            s+="("+generExpNotBrac(x,False)+")"
            s+="**"+"+"+str(random.randint(1,2))
        if i < n - 1:
            s+="*"
    return s

def generExpWithBracket(x):
    n = random.randint(2,2)
    m = random.randint(1,3)
    s = ""
    if m==1:
        s+="+"
    elif m==2:
        s+='-'
    for i in range(n):
        s+=generTermWithBracket(x,True)
        if i < n - 1:
            if random.random()>0.9:
                s+="+"
            else:
                s+="-"
    return s

for i in range(100):
    s = generExpWithBracket(x)
    print(s)