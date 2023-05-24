def limit():
    s = ""
    for i in range(1, 2500):
        s += "ap {} {} 200\n".format(i, i)
    for i in range(1, 2499):
        s += "ar {} {} 1000\n".format(i, i + 1)
    s += "qci 1 2499"
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
limit()