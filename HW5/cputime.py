import subprocess
import ctypes

# must be shell=False
for i in range(10):
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