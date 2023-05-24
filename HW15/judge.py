import ctypes
import os
import subprocess
import data
import limitData
#  #!/usr/bin/python3.9
#  -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2022 #
#  @Time    : 2022/4
#  @Author  : # @Email   : sdjasjBUAA@gmail.com
#  @File    : $data.py
#  @Author  : BUAA-sdjasj
#

#将你需要评测的jar包放到与judge.py相同目录，并添加jar包名字,不需要加.jar
# example arList = ['my','lbh', 'bhl']
jarList = ['code','cnx']


stdoutList = [] #保存每个jar的输出
cputimeList = []
"""
for jar in jarList:
    stdoutList.append("{}stdout.txt".format(jar))
"""
for times in range(20000):
    stdinData = data.checkR00X()
    stdoutList = []
    cputimeList = []
    for jar in jarList:
        cmd = "java -jar {}".format(jar + '.jar')
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                encoding='ISO-8859-1')
        stdout, stderr = proc.communicate(stdinData)

        handle = proc._handle

        creation_time = ctypes.c_ulonglong()
        exit_time = ctypes.c_ulonglong()
        kernel_time = ctypes.c_ulonglong()
        user_time = ctypes.c_ulonglong()

        rc = ctypes.windll.kernel32.GetProcessTimes(handle,
                                                    ctypes.byref(creation_time),
                                                    ctypes.byref(exit_time),
                                                    ctypes.byref(kernel_time),
                                                    ctypes.byref(user_time),
                                                    )

        #print((exit_time.value - creation_time.value) / 10000000)
        #print((kernel_time.value + user_time.value) / 10000000)
        cputime = (kernel_time.value + user_time.value) / 10000000
        cputimeList.append(cputime)
        out1 = stdout.split("\n")
        out1 = out1[:len(out1) - 1]
        stdoutList.append(out1)
        """
        with open(stdoutList[jarList.index(jar)], 'w', 'utf-8') as f:
            for s in out1:
                f.write(s)
                f.write('\n')
        """
    print(cputimeList)
    #print(stdoutList[0])
    maxCPUTime = max(cputimeList)
    minCPUTime = min(cputimeList)
    if maxCPUTime > 1000 or (maxCPUTime / minCPUTime) > 8:
        with open('errorTime2.txt', 'a', encoding='utf-8') as f:
            f.write("{} cputime is {} longer than {} {}\n".format(jarList[cputimeList.index(maxCPUTime)], maxCPUTime, jarList[cputimeList.index(minCPUTime)], minCPUTime))
            f.write("other cputime is\n")
            for cputime in cputimeList:
                if cputime != maxCPUTime and cputime != minCPUTime:
                    f.write("{} is {}".format(jarList[cputimeList.index(cputime)], cputime))
            f.write("error is\n")
            f.write('stdin is \n')
            f.write(stdinData)
            f.write('\n\n\n\n\n\n\n\n\n\n')
        print("^^^^^^^^^^^^WA^^^^^^^^^^^^^^")
        continue
    flag = False
    """
    for i in range(len(stdoutList)):
        if flag:
            break
        for j in range(len(stdoutList)):
            if i == j:
                continue
            if flag:
                break
            if len(stdoutList[i]) != len(stdoutList[j]):
                with open('error2.txt', 'a', encoding='utf-8') as f:
                    f.write("{} length is no equal with {}\n".format(jarList[i], jarList[j]))
                    f.write("error is\n")
                    f.write("{} or {}\n".format(stdoutList[j], stdoutList[i]))
                    f.write('stdin is \n')
                    f.write(stdinData)
                    f.write('\n\n\n\n\n\n\n\n\n\n')
                flag = True
                print("^^^^^^^^^^^^WA^^^^^^^^^^^^^^")
                break
    if flag:
        continue
    """
    for i in range(len(stdoutList[0])):
        if flag:
            break
        for j in range(len(stdoutList)):
            if flag:
                break
            for k in range(len(stdoutList)):
                if flag:
                    break
                if j == k:
                    continue
                if stdoutList[j][i] != stdoutList[k][i]:
                    with open('error2.txt', 'a', encoding='utf-8') as f:
                        f.write("{} output is not equal with {}\n".format(jarList[j], jarList[k]))
                        f.write("error is in line {}\n".format(i))
                        f.write("error is\n")
                        f.write("{}   :{}\n".format(jarList[j],stdoutList[j][i]))
                        f.write("{}   :{}\n".format(jarList[k],stdoutList[k][i]))
                        f.write('stdin is \n')
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                        f.write(stdinData)
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                        f.write('\n\n\n\n\n\n\n\n\n\n')
                    flag = True
                    print("^^^^^^^^^^^^WA^^^^^^^^^^^^^^")
                    break
    if flag:
        continue
    print("^^^^^^^^^^^^AC{}^^^^^^^^^^^^^^".format(times))

