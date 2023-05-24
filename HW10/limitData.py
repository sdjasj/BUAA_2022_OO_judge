import random


def limit():
    s = ""
    for i in range(1, 5000):
        s += "ap {} {} 200\n".format(i, i)
    for i in range(1, 4999):
        s += "ar {} {} 1000\n".format(i, i + 1)
    s += "qci 1 5000"
    with open("input.txt",'w',encoding='utf-8') as f:
        f.write(s)

def data():
    s = ""
    with open("input.txt",'r',encoding='utf-8') as f:
        tmp = f.readline()
        while tmp!="":
            s+=tmp
            tmp=f.readline()
    return s
def limit2():
    s = ''
    for i in range(1,2500):
        s+= 'ap {} {} {}\n'.format(i,i,random.randint(0,200))
    s+='ag 1\n'
    for i in range(1,2500):
        s+='atg {} {}\n'.format(i,1)
        s+='qgav 1\n'
    return s
    with open("input.txt",'w',encoding='utf-8') as f:
        f.write(s)


if __name__ == '__main__':
    limit2()
