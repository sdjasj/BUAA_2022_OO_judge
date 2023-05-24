from xeger import Xeger
import random

# powFun = 'x( ){0}(\*\*( ){0}\+0{0}[0-4])?'
powFun = 'x'
const = '(\+|-)0{0}[0-9]{1}'
power = '( ){0}(\*\*( ){0}\+0{0,1}[2-3])?'

# fun1,fun2,fun3分别是函数参数为1个，2个，3个的函数，而且函数名分别为f，g，h
list_fun1 = ["f(x)=x", "f(y)=sin(y)", "f(z)=z*z", "f(y)=y*y", "f(z)=sin(cos(z))"]
list_fun2 = ["g(x,y)=x+y", "g(y,z)=sin(y)*cos(z)", "g(x,z)=x*z+x-z", "g(z,y)=y*y-z+2", "g(z,x)=cos((z*x))"]
list_fun3 = ["h(x,y,z)=x+y-z", "h(x,z,y)=sin(x)+y+cos(z)", "h(x,z,y)=x+y*(z-1)", "h(x,y,z)=y*y*x*(4-z)",
             "h(z,x,y)=sin(x)*y+x"]
list_fun = [list_fun1, list_fun2, list_fun3]

# 用于替换函数参数的变量，即若函数为f(y)=sin(y)，则从list_var中随机一个当作y填入函数
list_var = ["1", "2", "x", "x**2", "x**0", "f(g(x**1,cos(x)))", "g(f(0),g(x,1))", "h(1,1,1)", "0", "cos(-0)", "sin(-0)",
            "sum(i, -2, 1, i*cos(x))","sin(sin(sin(0)))","cos(sin(0))","cos(cos(0))","sum(i, 0, 2, i)","g(h(sum(i,-2,-1, i), f(cos(sin(x**1))),sum(i,2,2,(i*cos(i))) ),sum(i,-2,2,sin(i)) )"]

fun_java = []  # 随机出了哪些函数，记录一下，java输入时要用到
fun_record = []  # 函数名不能重复，也记录一下

x = Xeger(limit=100)
x._cases['any'] = lambda x: '.'
x._alphabets['whitespace'] = ' '


def generate_function():
    std_java = ""
    p = random.randint(1, len(list_fun1))  # 类型（每个函数列表中的第几个）
    num = random.randint(1, 3)  # 参数个数/函数名
    while num in fun_record:
        # 不能重复
        num = random.randint(1, 3)
        if len(fun_record) >= 3:
            break
    fun_record.append(num)  # 记录用过的函数名

    fun_java.append((num, p))  # 记录随机出的函数
    std_java += list_fun[num - 1][p - 1].split("=")[0][0:2]
    # 假如函数为 g(x,y)=x+y ，按等于符号split，第0项是g(x,y)，取 g(

    arr = []  # 记录实际表达式中的参数列表
    for i in range(0, num):
        arr.append(list_var[random.randint(0, len(list_var) - 1)])  # 从参数列表随机
        std_java += arr[i]
        if i < num - 1:
            std_java += ","
    std_java += ")"
    return std_java


def generSin(x):
    return "sin" + " " * random.randint(0, 0) + "(" + gengerFactor(x) + ")" + x.xeger(power)


def generCos(x):
    return "cos" + " " * random.randint(0, 0) + "(" + gengerFactor(x) + ")" + x.xeger(power)


def generSinNotSumAndDefined(x):
    return "sin" + " " * random.randint(0, 0) + "(" + generFactorNotSumAndDefined(x) + ")" + x.xeger(power)


def generCosNotSumAndDefined(x):
    return "cos" + " " * random.randint(0, 0) + "(" + generFactorNotSumAndDefined(x) + ")" + x.xeger(power)


def generSum(x):
    begin = random.randint(-5, 5)
    end = begin + random.randint(-2, 2)
    s = "sum" + "(" + "i" + "," + str(begin) + "," + str(end) + ","
    factor = "(" + generExpFactorNotDefinedFuncAndSum(x, False) + ")"
    factor = factor.replace("x", "i")
    s += factor + ")"
    return s

def generExpFactorNotDefinedFuncAndSum(x, notpre):
    n = random.randint(1, 2)
    m = random.randint(1, 3)
    s = ""
    if not notpre:
        if m == 1:
            s += "+"
        elif m == 2:
            s += '-'
    s += generTermNotExpDefinedFuncAndSum(x, False)
    for i in range(n):
        if random.random() > 0.5:
            s += "+"
        else:
            s += "-"
        s += generTermNotExpDefinedFuncAndSum(x, True)
    return s


def generTermNotExpDefinedFuncAndSum(x, notpre):
    n = random.randint(1, 2)
    m = random.randint(1, 3)
    s = ""
    if not notpre:
        if m == 1:
            s += "+"
        elif m == 2:
            s += '-'
    for i in range(n):
        if random.random() > 0.8:
            s += x.xeger(powFun)
        elif 0.6 < random.random() <= 0.8:
            s += x.xeger(const)
        elif 0.3 < random.random() <= 0.6:
            s += generSinNotSumAndDefined(x)
        else:
            s += generCosNotSumAndDefined(x)
        if i < n - 1:
            s += "*"
    return s


def gengerFactor(x):
    s = ""
    ran = random.random()
    if ran > 0.8:
        s += x.xeger(powFun)
    elif 0.7 < ran <= 0.8:
        s += x.xeger(const)
    elif 0.5 < ran <= 0.7:
        s += generSin(x)
    elif 0.3 < ran <= 0.5:
        s += generCos(x)
    else:
        s += generSum(x)
    return s


def generFactorNotSumAndDefined(x):
    s = ""
    ran = random.random()
    if ran > 0.8:
        s += x.xeger(powFun)
    elif 0.6 < ran <= 0.8:
        s += x.xeger(const)
    elif 0.3 < ran <= 0.6:
        s += generSinNotSumAndDefined(x)
    else:
        s += generCosNotSumAndDefined(x)
    return s


def generTermNotExp(x, notpre):
    n = random.randint(1, 3)
    m = random.randint(1, 3)
    s = ""
    if not notpre:
        if m == 1:
            s += "+"
        elif m == 2:
            s += '-'
    for i in range(n):
        ran = random.random()
        if ran > 0.8:
            s += x.xeger(powFun)
        elif 0.7 < ran <= 0.8:
            s += x.xeger(const)
        elif 0.45 < ran <= 0.7:
            s += generSin(x)
        elif 0.2 < ran <= 0.45:
            s += generCos(x)
        else:
            s += generSum(x)
        if i < n - 1:
            s += "*"
    return s


def generExpNotBrac(x, notpre):
    n = random.randint(2, 3)
    m = random.randint(1, 3)
    s = ""
    if not notpre:
        if m == 1:
            s += "+"
        elif m == 2:
            s += '-'
    s += generTermNotExp(x, False)
    for i in range(n):
        bracket = random.random()
        if bracket > 0.0:
            s = "(" + s + ")"
        if random.random() > 0.5:
            s += "+"
        else:
            s += "-"
        s += generTermNotExp(x, True)
    return s


def generTermWithBracket(x, notpre):
    n = random.randint(1, 3)
    m = random.randint(1, 3)
    s = ""
    if notpre:
        if m == 1:
            s += "+"
        elif m == 2:
            s += '-'
    for i in range(n):
        tmp = random.random()
        if tmp > 0.85:
            s += x.xeger(powFun)
        elif 0.80 < tmp <= 0.85:
            s += x.xeger(const)
        elif 0.6 < tmp <= 0.8:
            s += generSin(x)
        elif 0.4 < tmp <= 0.6:
            s += generCos(x)
        elif tmp <= 0.4:
            s += "(" + generExpNotBrac(x, False) + ")"
            s += "**" + "+" + str(random.randint(1, 2))
        if i < n - 1:
            s += "*"
    return s


def generExpWithBracket(x):
    n = random.randint(2, 3)
    m = random.randint(1, 3)
    s = ""
    if m == 1:
        s += "+"
    elif m == 2:
        s += '-'
    for i in range(n):
        s += generTermWithBracket(x, True)
        if i < n - 1:
            if random.random() > 0.5:
                s += "+"
            else:
                s += "-"
    return s


"""
print(3)
print(random.choice(list_fun1))
print(random.choice(list_fun2))
print(random.choice(list_fun3))
s = generExpWithBracket(x)
print(s)
"""


def generdata():
    global x
    s = "0\n" + generExpWithBracket(x)
    return s