import os
import data
import re

elevator = [[] for _ in range(5)]
elevatorState = ["ARRIVE", "ARRIVE", "ARRIVE", "ARRIVE", "ARRIVE"]
elevatorCurFloor = [1, 1, 1, 1, 1]
elevatorOpenTime = [0, 0, 0, 0, 0]
elevatorCloseTime = [0, 0, 0, 0, 0]
elevatorArriveTime = [0, 0, 0, 0, 0]
arrivedPassengerNum = 0
timeMsg = 0


def judgeOutput(output: str):
    global timeMsg
    idxTimeRight = output.index(']')
    idxFirstarg = output.index('-')
    actionType = output[idxTimeRight + 1: idxFirstarg]
    timeMsg = float(output[1:idxTimeRight])
    waMessage = ''
    if actionType == 'ARRIVE':
        inform = output[idxFirstarg + 1:].split('-')
        waMessage = judgeARRIVE(inform[0], int(inform[1]), int(inform[2]), timeMsg)
    elif actionType == 'OPEN':
        inform = output[idxFirstarg + 1:].split('-')
        waMessage = judgeOPEN(inform[0], int(inform[1]), int(inform[2]), timeMsg)
    elif actionType == 'CLOSE':
        inform = output[idxFirstarg + 1:].split('-')
        waMessage = judgeCLOSE(inform[0], int(inform[1]), int(inform[2]), timeMsg)
    elif actionType == 'IN':
        inform = output[idxFirstarg + 1:].split('-')
        waMessage = judgeIN(int(inform[0]), inform[1], int(inform[2]), int(inform[3]), timeMsg)
    elif actionType == 'OUT':
        inform = output[idxFirstarg + 1:].split('-')
        waMessage = judgeOUT(int(inform[0]), inform[1], int(inform[2]), int(inform[3]), timeMsg)
    return waMessage


def judgeARRIVE(building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId - 1]
    if state == 'OPEN' or state == 'IN' or state == 'OUT':
        return state + " before open or not close door in " + building + '   [' + str(timeMsg) + ']'
    if abs(floor - elevatorCurFloor[elevatorId - 1]) != 1:
        return str(elevatorId) + " skip the floor" + '   [' + str(timeMsg) + ']'
    if elevatorArriveTime[elevatorId - 1] == 0:
        elevatorArriveTime[elevatorId - 1] = timeMsg
    elif timeMsg - elevatorArriveTime[elevatorId - 1] < 0.4 - 0.00001:
        return str(elevatorId) + " move too fast !!!" + '   [' + str(timeMsg) + ']'
    elevatorCurFloor[elevatorId - 1] = floor
    elevatorState[elevatorId - 1] = 'ARRIVE'
    elevatorArriveTime[elevatorId - 1] = timeMsg
    return ""


def judgeOPEN(building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId - 1]
    if state == 'IN' or state == 'OUT':
        return state + " before OPEN in " + building + '   [' + str(timeMsg) + ']'
    if state == 'OPEN':
        return "cannot open again" + '   [' + str(timeMsg) + ']'
    elevatorOpenTime[elevatorId - 1] = timeMsg
    elevatorState[elevatorId - 1] = 'OPEN'
    return ""


def judgeCLOSE(building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId - 1]
    if state == 'CLOSE':
        return "cannot CLOSE again" + '   [' + str(timeMsg) + ']'
    if state == 'ARRIVE':
        return "CLOSE before OPEN" + '   [' + str(timeMsg) + ']'
    if timeMsg - elevatorOpenTime[elevatorId - 1] < 0.4-0.00001:
        return "elevator " + str(elevatorId) + " close door to fast" + '   [' + str(timeMsg) + ']'
    elevatorCloseTime[elevatorId - 1] = timeMsg
    elevatorState[elevatorId - 1] = 'CLOSE'
    return ""


def judgeIN(passengerId, building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId - 1]
    if state != 'OPEN' and state != 'IN' and state != 'OUT':
        return "passenger IN before OPEN" + " and state is " + state + '   [' + str(timeMsg) + ']'
    if passengerId in elevator[elevatorId - 1]:
        return "The same passenger cannot enter into the elevator again" + '   [' + str(timeMsg) + ']'
    if len(elevator[elevatorId - 1]) >= 6:
        return "more than 6 passenger in the elevator" + str(elevatorId) + '   [' + str(timeMsg) + ']'
    elevator[elevatorId - 1].append(passengerId)
    elevatorState[elevatorId - 1] = "IN"
    return ""


def judgeOUT(passengerId, building, floor, elevatorId, timeMsg):
    global arrivedPassengerNum
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId - 1]
    if state != 'OPEN' and state != 'IN' and state != 'OUT':
        return "passenger OUT before OPEN" + '   [' + str(timeMsg) + ']'
    if passengerId not in elevator[elevatorId - 1]:
        return "not passenger named " + str(passengerId) + "in elevator" + '   [' + str(timeMsg) + ']'
    if len(elevator[elevatorId - 1]) == 0:
        return "elevator is empty" + '   [' + str(timeMsg) + ']'
    elevator[elevatorId - 1].remove(passengerId)
    elevatorState[elevatorId - 1] = "OUT"
    arrivedPassengerNum += 1
    return ""


def judgeEND(requets):
    if requets != arrivedPassengerNum:
        return str(requets - arrivedPassengerNum) + " people were eaten by elevator"
    for s in elevator:
        if len(s) > 0:
            return "passenger wait in elevator"
    for i in range(len(elevatorState)):
        if elevatorState[i] == "ARRIVE" or elevatorState[i] == "CLOSE":
            continue
        else:
            return "elevator " + str(i + 1) + " is " + elevatorState[i] + " finally"
    return ""


def judgeTime():
    global timeMsg
    os.system('.\datacheck1.exe > stdtime.txt')
    with open('stdtime.txt', 'r', encoding='utf-8') as stdtime:
        offTime = stdtime.readline()
        r = re.match(r'Your input is valid,base time is (.*),max time is (.*)', offTime)
        baseTime = float(r.group(1))
        maxTime = float(r.group(2))
        if timeMsg > maxTime:
            return "your time is " + str(timeMsg) + " greater than maxtime " + str(maxTime)
        print("baseTime is " + str(baseTime))
        print("yourTime is " + str(timeMsg))
        print("yourTime/baseTime is " + str(timeMsg / baseTime))
        with open("timeCompare.txt", 'a', encoding='utf-8') as f:
            f.write("baseTime is " + str(baseTime))
            f.write('\n')
            f.write("yourTime is " + str(timeMsg))
            f.write('\n')
            f.write("yourTime/baseTime is " + str(timeMsg / baseTime))
            f.write('\n\n\n')
        return ""


for i in range(1000):
    requestNum = data.gengerData()
    os.system('.\datainput_student_win64.exe | java -jar code.jar > stdout.txt')
    elevator = [[] for _ in range(5)]
    elevatorState = ["ARRIVE", "ARRIVE", "ARRIVE", "ARRIVE", "ARRIVE"]
    elevatorCurFloor = [1, 1, 1, 1, 1]
    elevatorOpenTime = [0, 0, 0, 0, 0]
    elevatorCloseTime = [0, 0, 0, 0, 0]
    elevatorArriveTime = [0, 0, 0, 0, 0]
    arrivedPassengerNum = 0
    flag = True
    with open("stdout.txt", 'r', encoding='utf-8') as f:
        while True:
            output = f.readline()
            if output == '\n' or output == "":
                break
            waMessage = judgeOutput(output)
            if waMessage != "":
                flag = False
                with open("error.txt", 'a', encoding='utf-8') as err:
                    err.write(waMessage)
                    err.write('\n')
                print(waMessage)
        waMessage = judgeEND(requets=requestNum)
        if waMessage != "":
            flag = False
            with open("error.txt", 'a', encoding='utf-8') as err:
                err.write(waMessage)
                err.write('\n')
            print(waMessage)
        waMessage = judgeTime()
        if waMessage != "":
            flag = False
            with open("error.txt", 'a', encoding='utf-8') as err:
                err.write(waMessage)
                err.write('\n')
            print(waMessage)
    if flag == False:
        with open("error.txt", 'a', encoding='utf-8') as err:
            err.write('\nstdin:\n')
            with open("stdin.txt", 'r', encoding='utf-8') as stdin:
                while True:
                    stdintext = stdin.readline()
                    if len(stdintext) < 4:
                        break
                    err.write(stdintext)
            with open("stdout.txt", 'r', encoding='utf-8') as out:
                err.write('\nstdout:\n')
                while True:
                    stdouttext = out.readline()
                    if len(stdouttext) < 4:
                        break
                    err.write(stdouttext)
            err.write('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print("------------WA---------------")
    else:
        print("------------AC---------------")
