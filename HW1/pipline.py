# pipline.py
from distutils.log import ERROR
from gendata import genData
import os
import sys
import shutil
import re
import random
import sympy

project_dir = "D:\\BUAA_study\\OO\homework1\\test"  # java项目目录
lib_dir = "D:\\java_package\\official_1.jar"
ret = 5


def judge(stdAns,myAns):
    x = sympy.Symbol('x')
    myAns = re.sub('(Mode: Normal)|\n',"",myAns)
    # myAns.replace("Mode: Normal","")
    # myAns.replace("\\n","")
    for i in range(10):
        testNum = random.randint(-10,10)
        stdNum = sympy.sympify(stdAns).evalf(subs={x:testNum})
        myNum = sympy.sympify(myAns).evalf(subs={x:testNum})
        if stdNum!=myNum:
            return False
    return True

os.chdir(project_dir+'\\src')
print("begin compliation-------------------------------------")
os.system('javac -encoding UTF-8  -cp .;' + lib_dir +  ' *.java -d ..\\out')
print("complete compilation----------------------------------")
os.chdir(project_dir+'\\out')
print("begin test--------------------------------------------")
OUTTXT = open('out.txt','w')
ERRORTXT = open('error.txt','w')
error = 0
for i in range(ret):
    expr,answer = genData()
    print("standand_answer:"+answer,file=OUTTXT)
    out = os.popen('echo ' + expr + ' | java -cp .;' + lib_dir + ' MainClass').read()
    print("your_answer:"+out,file=OUTTXT)
    if judge(answer,out)==False:
        error = error + 1
        print("standand_answer:"+answer,file=ERRORTXT)
        print("your_answer:"+out,file=ERRORTXT)

OUTTXT.close()
ERRORTXT.close()
shutil.move(project_dir+"\\out\\out.txt",project_dir+"\\out.txt")
shutil.move(project_dir+"\\out\\error.txt",project_dir+"\\error.txt")
print("has " + str(error) + "errors")
print("test_end")