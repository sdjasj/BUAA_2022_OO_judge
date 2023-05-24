
import os
import data

buildingElevator = {}
for i in range(1, 6):
    buildingElevator[i] = []

floorElevator = {}

elevatorState = {}
for i in range(1, 6):
    elevatorState[i] = "ARRIVE"

elevatorCurFloor = {}
for i in range(1, 6):
    elevatorCurFloor[i] = 1

elevatorCurBuilding = {}
for i in range(1, 6):
    elevatorCurBuilding[i] = chr(ord('A') + i - 1)

elevatorOpenTime = {}
for i in range(1, 6):
    elevatorOpenTime[i] = 0

elevatorCloseTime = {}
for i in range(1, 6):
    elevatorCloseTime[i] = 0

elevatorArriveTime = {}
for i in range(6):
    elevatorArriveTime[i] = 0

arrivedPassengerNum = 0
inPassengerNum = 0
timeMsg = 0


def addElevator(addArgList: list):
    addType = addArgList[1]
    if addType == 'building':
        elevatorId = int(addArgList[2])
        buildingElevator[elevatorId] = []
        elevatorState[elevatorId] = "ARRIVE"
        elevatorCurFloor[elevatorId] = 1
        elevatorCurBuilding[elevatorId] = addArgList[3]
        elevatorOpenTime[elevatorId] = 0
        elevatorCloseTime[elevatorId] = 0
        elevatorArriveTime[elevatorId] = 0
    elif addType == 'floor':
        elevatorId = int(addArgList[2])
        floorElevator[elevatorId] = []
        elevatorState[elevatorId] = "ARRIVE"
        elevatorCurFloor[elevatorId] = int(addArgList[3])
        elevatorCurBuilding[elevatorId] = "A"
        elevatorOpenTime[elevatorId] = 0
        elevatorCloseTime[elevatorId] = 0
        elevatorArriveTime[elevatorId] = 0


def judgeOutput(output: str):
    global timeMsg
    idxTimeRight = output.index(']')
    idxFirstarg = output.index('-')
    actionType = output[idxTimeRight + 1: idxFirstarg]
    if timeMsg > float(output[1:idxTimeRight]):
        timeMsg = float(output[1:idxTimeRight])
        return "is not incremental time " + '   [' + str(timeMsg) + ']'
    else:
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
    if elevatorId in buildingElevator.keys():
        state = elevatorState[elevatorId]
        if state == 'OPEN' or state == 'IN' or state == 'OUT':
            return state + " before open or not close door in " + building + '   [' + str(timeMsg) + ']'
        if abs(floor - elevatorCurFloor[elevatorId]) != 1:
            return str(elevatorId) + " skip the floor" + '   [' + str(timeMsg) + ']'
        if elevatorArriveTime[elevatorId] == 0:
            elevatorArriveTime[elevatorId] = timeMsg
        elif timeMsg - elevatorArriveTime[elevatorId] < 0.4 - 0.00001:
            return str(elevatorId) + " move too fast !!!" + '   [' + str(timeMsg) + ']'
        elevatorCurFloor[elevatorId] = floor
        elevatorState[elevatorId] = 'ARRIVE'
        elevatorArriveTime[elevatorId] = timeMsg
        return ""
    elif elevatorId in floorElevator.keys():
        state = elevatorState[elevatorId]
        if state == 'OPEN' or state == 'IN' or state == 'OUT':
            return state + " before open or not close door in " + building + '   [' + str(timeMsg) + ']'
        oldBuilding = ord(elevatorCurBuilding[elevatorId])
        curBuilding = ord(building)
        if (abs(oldBuilding - curBuilding)) != 1 and abs(oldBuilding - curBuilding) != 4:
            return str(elevatorId) + " skip the building" + '   [' + str(timeMsg) + ']'
        if elevatorArriveTime[elevatorId] == 0:
            elevatorArriveTime[elevatorId] = timeMsg
        elif timeMsg - elevatorArriveTime[elevatorId] < 0.2 - 0.00001:
            return str(elevatorId) + " move too fast !!!" + '   [' + str(timeMsg) + ']'
        elevatorCurBuilding[elevatorId] = building
        elevatorState[elevatorId] = 'ARRIVE'
        elevatorArriveTime[elevatorId] = timeMsg
        return ""
    else:
        return "no elevator " + str(elevatorId)


def judgeOPEN(building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId]
    if state == 'IN' or state == 'OUT':
        return state + " before OPEN in " + building + '   [' + str(timeMsg) + ']'
    if state == 'OPEN':
        return "cannot open again" + '   [' + str(timeMsg) + ']'
    elevatorOpenTime[elevatorId] = timeMsg
    elevatorState[elevatorId] = 'OPEN'
    return ""


def judgeCLOSE(building, floor, elevatorId, timeMsg):
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    state = elevatorState[elevatorId]
    if state == 'CLOSE':
        return "cannot CLOSE again" + '   [' + str(timeMsg) + ']'
    if state == 'ARRIVE':
        return "CLOSE before OPEN" + '   [' + str(timeMsg) + ']'
    if timeMsg - elevatorOpenTime[elevatorId] < 0.4 - 0.00001:
        return "elevator " + str(elevatorId) + " close door to fast" + '   [' + str(timeMsg) + ']'
    elevatorCloseTime[elevatorId] = timeMsg
    elevatorState[elevatorId] = 'CLOSE'
    return ""


def judgeIN(passengerId, building, floor, elevatorId, timeMsg):
    global inPassengerNum
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    inPassengerNum+=1
    if elevatorId in buildingElevator.keys():
        state = elevatorState[elevatorId]
        if state != 'OPEN' and state != 'IN' and state != 'OUT':
            return "passenger IN before OPEN" + " and state is " + state + '   [' + str(timeMsg) + ']'
        if passengerId in buildingElevator[elevatorId]:
            return "The same passenger cannot enter into the elevator again" + '   [' + str(timeMsg) + ']'
        if len(buildingElevator[elevatorId]) >= 6:
            return "more than 6 passenger in the elevator" + str(elevatorId) + '   [' + str(timeMsg) + ']'
        buildingElevator[elevatorId].append(passengerId)
        elevatorState[elevatorId] = "IN"
        return ""
    elif elevatorId in floorElevator.keys():
        state = elevatorState[elevatorId]
        if state != 'OPEN' and state != 'IN' and state != 'OUT':
            return "passenger IN before OPEN" + " and state is " + state + '   [' + str(timeMsg) + ']'
        if passengerId in floorElevator[elevatorId]:
            return "The same passenger cannot enter into the elevator again" + '   [' + str(timeMsg) + ']'
        if len(floorElevator[elevatorId]) >= 6:
            return "more than 6 passenger in the elevator" + str(elevatorId) + '   [' + str(timeMsg) + ']'
        floorElevator[elevatorId].append(passengerId)
        elevatorState[elevatorId] = "IN"
        return ""
    else:
        return "no elevator " + str(elevatorId)


def judgeOUT(passengerId, building, floor, elevatorId, timeMsg):
    global arrivedPassengerNum
    if floor >= 11:
        return "floor > 10"
    if floor <= 0:
        return "floor < 1"
    if elevatorId in buildingElevator.keys():
        state = elevatorState[elevatorId]
        if state != 'OPEN' and state != 'IN' and state != 'OUT':
            return "passenger OUT before OPEN" + '   [' + str(timeMsg) + ']'
        if passengerId not in buildingElevator[elevatorId]:
            return "not passenger named " + str(passengerId) + "in elevator" + '   [' + str(timeMsg) + ']'
        if len(buildingElevator[elevatorId]) == 0:
            return "elevator is empty" + '   [' + str(timeMsg) + ']'
        buildingElevator[elevatorId].remove(passengerId)
        elevatorState[elevatorId] = "OUT"
        arrivedPassengerNum += 1
        return ""
    elif elevatorId in floorElevator.keys():
        state = elevatorState[elevatorId]
        if state != 'OPEN' and state != 'IN' and state != 'OUT':
            return "passenger OUT before OPEN" + '   [' + str(timeMsg) + ']'
        if passengerId not in floorElevator[elevatorId]:
            return "not passenger named " + str(passengerId) + "in elevator" + '   [' + str(timeMsg) + ']'
        if len(floorElevator[elevatorId]) == 0:
            return "elevator is empty" + '   [' + str(timeMsg) + ']'
        floorElevator[elevatorId].remove(passengerId)
        elevatorState[elevatorId] = "OUT"
        arrivedPassengerNum += 1
        return ""
    else:
        return "no elevator " + str(elevatorId)


def judgeEND(requets):
    if requets != arrivedPassengerNum or requets != inPassengerNum:
        return str(requets - arrivedPassengerNum) + " people were eaten by elevator"
    for i in elevatorState.keys():
        if elevatorState[i] == "ARRIVE" or elevatorState[i] == "CLOSE":
            continue
        else:
            return "elevator " + str(i) + " is " + elevatorState[i] + " finally"
    return ""


def judgeTime():
    global timeMsg
    print(timeMsg)


for i in range(1000):
    requestNum = data.gengerData()
    os.system('.\datainput_student_win64.exe | java -jar code.jar > stdout.txt')
    buildingElevator = {}
    for i in range(1, 6):
        buildingElevator[i] = []

    floorElevator = {}

    elevatorState = {}
    for i in range(1, 6):
        elevatorState[i] = "ARRIVE"

    elevatorCurFloor = {}
    for i in range(1, 6):
        elevatorCurFloor[i] = 1

    elevatorCurBuilding = {}
    for i in range(1, 6):
        elevatorCurBuilding[i] = chr(ord('A') + i - 1)

    elevatorOpenTime = {}
    for i in range(1, 6):
        elevatorOpenTime[i] = 0

    elevatorCloseTime = {}
    for i in range(1, 6):
        elevatorCloseTime[i] = 0

    elevatorArriveTime = {}
    for i in range(6):
        elevatorArriveTime[i] = 0

    arrivedPassengerNum = 0
    inPassengerNum = 0
    timeMsg = 0
    flag = True
    with open('stdin.txt', 'r', encoding='utf-8') as f:
        while True:
            stdinStr = f.readline()
            if stdinStr == '\n' or stdinStr == "":
                break
            idxTimeRight = stdinStr.index(']')
            alist = stdinStr[idxTimeRight + 1:].split('-')
            if alist[0] == 'ADD':
                addElevator(alist)
    with open("stdout.txt", 'r', encoding='utf-8') as f:
        while True:
            output = f.readline()
            if output == '\n' or output == "":
                break
            waMessage = judgeOutput(output)
            if waMessage != "":
                flag = False
                with open("error3.txt", 'a', encoding='utf-8') as err:
                    err.write(waMessage)
                    err.write('\n')
                print(waMessage)
        waMessage = judgeEND(requets=requestNum)
        if waMessage != "":
            flag = False
            with open("error3.txt", 'a', encoding='utf-8') as err:
                err.write(waMessage)
                err.write('\n')
            print(waMessage)
        judgeTime()
    if not flag:
        with open("error3.txt", 'a', encoding='utf-8') as err:
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
