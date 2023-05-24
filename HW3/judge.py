import subprocess
from math import *
import os
import data


def getinput():
    s = data.generdata()
    while len(s) > 200:
        s = data.generdata()
    return s


cmd_my = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=58765:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\OO仓库\HW3\homework_2022_20231204_hw_3\out\production\homework_2022_20231204_hw_3;D:\计算机\OO\OO仓库\HW3GUIDE\homework_3\面向对象表达式系列第三次官方包\official_3.jar" Main'

cmd2 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59192:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Saber\out\production\Saber;D:\计算机\OO\HACK\HW3\official_3.jar" MainClass'

cmd3 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59205:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Rider\out\production\Rider;D:\计算机\OO\HACK\HW3\official_3.jar" Main'

cmd4 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59214:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Lancer\out\production\Lancer;D:\计算机\OO\HACK\HW3\official_3.jar" MainClass'

cmd5 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59218:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Caster\out\production\Caster;D:\计算机\OO\HACK\HW3\official_3.jar" MainClass'

cmd6 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59237:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Assassin\out\production\Assassin;D:\计算机\OO\HACK\HW3\official_3.jar" mainpack.MainClass'

cmd7 = r'"C:\Program Files (x86)\Java\jdk1.8.0_321\bin\java.exe" "-javaagent:D:\IntelliJ IDEA Community Edition 2021.2.3\lib\idea_rt.jar=59248:D:\IntelliJ IDEA Community Edition 2021.2.3\bin" -Dfile.encoding=UTF-8 -classpath "C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\charsets.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\deploy.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\access-bridge-32.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\cldrdata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\dnsns.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jaccess.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\jfxrt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\localedata.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\nashorn.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunec.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunjce_provider.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunmscapi.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\sunpkcs11.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\ext\zipfs.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\javaws.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jce.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfr.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jfxswt.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\jsse.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\management-agent.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\plugin.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\resources.jar;C:\Program Files (x86)\Java\jdk1.8.0_321\jre\lib\rt.jar;D:\计算机\OO\HACK\HW3\Archer\out\production\Archer;D:\计算机\OO\HACK\HW3\official_3.jar" MainClass'

cmd8 = r''

testcmd2 = cmd2
testcmd3 = cmd3
testcmd4 = cmd4
testcmd5 = cmd5
testcmd6 = cmd6
testcmd7 = cmd7
testcmd8 = cmd8
for i in range(60000):
    java_input = getinput()
    print("----input----")
    print(java_input)
    print("-----------")

    proc = subprocess.Popen(cmd_my, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out1 = stdout.split("\n")[1]
    print(out1)

    proc = subprocess.Popen(testcmd2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out2 = stdout.split("\n")[1]
    print(out2)

    proc = subprocess.Popen(testcmd3, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out3 = stdout.split("\n")[1]
    print(out3)

    proc = subprocess.Popen(testcmd4, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out4 = stdout.split("\n")[1]
    print(out4)

    proc = subprocess.Popen(testcmd5, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out5 = stdout.split("\n")[1]
    print(out5)

    proc = subprocess.Popen(testcmd6, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out6 = stdout.split("\n")[1]
    print(out6)

    proc = subprocess.Popen(testcmd7, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out7 = stdout.split("\n")[1]
    print(out7)

    proc = subprocess.Popen(testcmd8, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='gb2312')
    stdout, stderr = proc.communicate(java_input)
    out8 = stdout.split("\n")[1]
    print(out8)

    x = 2.25
    r1 = eval(out1)
    r2 = eval(out2)
    r3 = eval(out3)
    r4 = eval(out4)
    r5 = eval(out5)
    r6 = eval(out6)
    r7 = eval(out7)
    r8 = eval(out8)
    print("my_out :", r1)
    print("saber  :", r2)
    print("rider  :", r3)
    print("lancer  :", r4)
    print("caster  :", r5)
    print("Assassin  :", r6)
    print("Archer  :", r7)
    print("8_out  :", r8)
    eps = 0.00000000001
    if r1 == 0 and r2 == 0 and r3 == 0 and r5 == 0:
        print("-------AC---------")
    elif r1 == 0 and (r2 != 0 or r3 != 0 or r5 != 0):
        print("-------WA---------")
    else:
        if abs((r1 - r2) / r1) < eps and abs((r1 - r3) / r1) < eps and abs(
                (r1 - r5) / r1) < eps:
            print("-------AC---------")
        else:
            print("-------WA---------")
            with open("hackerror2.txt", 'a', encoding='utf-8') as f:
                f.write(java_input)
                f.write("\n")
                f.write(out1)
                f.write("\n")
                f.write(out2)
                f.write("\n")
                f.write(out3)
                f.write("\n")
                f.write(out5)
                f.write("\n")
                f.write("my_out :" + str(r1))
                f.write("\n")
                f.write("saber  :" + str(r2))
                f.write("\n")
                f.write("rider   :" + str(r3))
                f.write("\n")
                f.write("caster   :" + str(r5))
                f.write("\n\n\n")
    print("\n\n")
