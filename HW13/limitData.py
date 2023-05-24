import random


def limit():
    s = ""
    for i in range(1, 5001):
        s += "ap {} {} 200\n".format(i, i)
    for i in range(1, 5000):
        s += "ar {} {} 1000\n".format(i, i + 1)
    s += "qci 1 5000"
    return s
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def data():
    s = ""
    with open("input.txt", 'r', encoding='utf-8') as f:
        tmp = f.readline()
        while tmp != "":
            s += tmp
            tmp = f.readline()
    return s


def limit2():
    s = ''
    for i in range(1, 2500):
        s += 'ap {} {} {}\n'.format(i, i, random.randint(111111, 1111111))
    s += 'ag 1\n'
    for i in range(1, 2500):
        s += 'atg {} {}\n'.format(i, 1)
        s += 'qgav 1\n'
    return s
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def limit3():
    s = ""
    for i in range(1, 1112):
        s += "ap {} {} 200\n".format(i, i)
    s += 'ag 1\n'
    for i in range(1, 1112):
        s += "atg {} {} 1000\n".format(i, 1)
    for i in range(2776):
        s += 'qgvs 1\n'
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)
    return s


def limitShortPath():
    s = ""
    for i in range(1, 5001):
        s += "ap {} {} 200\n".format(i, i)
    for i in range(1, 2500):
        s += "ar {} {} 1000\n".format(i, 2 * i + 1)
        s += "ar {} {} 1000\n".format(i, 2 * i)
    for i in range(1000):
        s += "am {} {} 0 {} {}\n".format(i, random.randint(-1000, 1000), 1, 4999)
    for i in range(1000):
        s += 'sim {}\n'.format(i)
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def limitShortPath2():
    s = ""
    for i in range(1, 1001):
        s += "ap {} {} 200\n".format(i, i)
    for i in range(1, 1001):
        s += "ar {} {} 1000\n".format(random.randint(1, 3000), random.randint(1, 3000))
    for i in range(1000):
        s += "am {} {} 0 {} {}\n".format(i, random.randint(-1000, 1000), random.randint(1, 3000),
                                         random.randint(1, 3000))
    for i in range(1000):
        s += 'sim {}\n'.format(i)
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def limitEmo():
    s = ""
    for i in range(1, 10001):
        s += "sei {}\n".format(i)
    for i in range(-10000, 1):
        s += "dce {}\n".format(i)
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def limitData4():
    s = ""
    s += 'ap 1 1 200\n'
    s += 'ap 2 2 200\n'
    s += 'ar 1 2 1000\n'
    s += 'am 1 1 0 1 2\n'
    s += 'sm 1\n'
    s += 'anm 1 fuck 0 1 2\n'
    s += 'sm 1\n'
    s += 'cn 2\n'
    s += 'qrm 2\n'
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write(s)


def limitData5():
    normalType = ['short', 'byte', 'int', 'long', 'char', 'boolean', 'float', 'double', 'String']
    s = ''
    s += '''{{\"_parent\":\"{0}\",\"visibility\":\"{1}\",\"name\":\"{2}\",\"_type\":\"UMLClass\",\"_id\":\"{3}\"}}'''.format(
        '0','public','fuck','10000')
    s += '\n'
    for i in range(10001,10003):
        s += "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLOperation\",\"_id\":\"{}\"}}".format(
        '10000', 'public','oo', str(int(i)))
        s += '\n'
    for i in range(1, 201):
       s +=  "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLParameter\",\"_id\":\"{}\",\"type\":{},\"direction\":\"{}\"}}".format(
            '10001','public', 'oo', str(int(i)), "\"int\"", 'in')
       s += '\n'
    for i in range(201, 401):
       s +=  "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLParameter\",\"_id\":\"{}\",\"type\":{},\"direction\":\"{}\"}}".format(
            '10002','public', 'oo', str(int(i)), "\"int\"", 'in')
       s += '\n'
    s += "END_OF_MODEL\n"
    for i in range(400):
        s += "CLASS_OPERATION_COUPLING_DEGREE {} {}\n".format('fuck','oo')
    return s
if __name__ == '__main__':
    limitData4()
