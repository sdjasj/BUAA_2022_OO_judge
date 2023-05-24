import subprocess
import ctypes
import data

# must be shell=False
for i in range(1000):
    data.gengerData()
    input_process = subprocess.Popen(['datainput_student_win64.exe'], shell=False, stdout=subprocess.PIPE)
    process = subprocess.Popen(['java', '-jar', 'code.jar'], shell=False, stdin=input_process.stdout)
    input_process.wait()
    process.wait()

    handle = process._handle

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

    print((exit_time.value - creation_time.value) / 10000000)
    print((kernel_time.value + user_time.value) / 10000000)
    cputime = (kernel_time.value + user_time.value) / 10000000
    with open('stdin.txt', 'r', encoding='utf-8') as f:
        with open('stdtime.txt', 'a', encoding='utf-8') as t:
            t.write(str((exit_time.value - creation_time.value) / 10000000))
            t.write('\n')
            t.write(str((kernel_time.value + user_time.value) / 10000000))
            t.write('\n\n')
            while True:
                output = f.readline()
                if output == '\n' or output == "":
                    break
                t.write(output)
            t.write('\n\n')
    with open('time.txt', 'a', encoding='utf-8') as tt:
        tt.write(str((exit_time.value - creation_time.value) / 10000000))
        tt.write('\n')
        tt.write(str((kernel_time.value + user_time.value) / 10000000))
        tt.write('\n\n')
    if cputime > 5.0:
        with open('error.txt', 'a', encoding='utf-8') as ff:
            ff.write(str(cputime))
            ff.write('\n')
            with open('stdin.txt', 'r', encoding='utf-8') as f:
                while True:
                    output = f.readline()
                    if output == '\n' or output == "":
                        break
                    t.write(output)
                t.write('\n\n')
