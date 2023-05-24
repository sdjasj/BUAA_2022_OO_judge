
"""
 *                             _ooOoo_
 *                            o8888888o
 *                            88" . "88
 *                            (| -_- |)
 *                            O\  =  /O
 *                         ____/`---'\____
 *                       .'  \\|     |//  `.
 *                      /  \\|||  :  |||//  \
 *                     /  _||||| -:- |||||-  \
 *                     |   | \\\  -  /// |   |
 *                     | \_|  ''\---/''  |   |
 *                     \  .-\__  `-`  ___/-. /
 *                   ___`. .'  /--.--\  `. . __
 *                ."" '<  `.___\_<|>_/___.'  >'"".
 *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *               \  \ `-.   \_ __\ /__ _/   .-` /  /
 *          ======`-.____`-.___\_____/___.-`____.-'======
 *                             `=---='
 *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
import random

MAX_BUILDING_ELEVATOR_NUM = 3
MAX_FLOOR_ELEVATOR_NUM = 3
MAX_ELEVATOR_NUM = 20
curElevatorNum = 6
Building = ['A', 'B', 'C', 'D', 'E']
idList = []
elevatorIdList = [1, 2, 3, 4, 5, 6]
curTime = 0
floorElevatorTime = {}
buildingElevatorNum = {'A': 1, 'B':1, 'C':1, 'D':1, 'E':1}
floorElevatorNum = {}
personReq = 0
elevatorCapacity = [4, 6, 8]
elevatorSpeed = [0.2, 0.4, 0.6]
arrivedPassengerInfo = {}
ElevatorMsg = {}
passengerList = []
for i in range(1,5):
    ElevatorMsg[i] = [8, 0.6]
ElevatorMsg[6] = [8, 0.6, 31]
for i in range(1,11):
    floorElevatorNum[i] = 0
floorElevatorNum[1] = 1
for i in range(1,11):
    floorElevatorTime[i] = 0


def getPersonId():
    passengerId = random.randint(1, 1000)
    while passengerId in idList:
        passengerId = random.randint(1, 1000)
    idList.append(passengerId)
    return passengerId


def getElevatorId():
    elevatorId = random.randint(7, 1000)
    while elevatorId in elevatorIdList:
        elevatorId = random.randint(7, 1000)
    elevatorIdList.append(elevatorId)
    return elevatorId

'''
def getBuildingInput():
    global curTime
    global personReq
    beginBuilding = random.choice(Building)
    passengerId = getPersonId()
    endBuilding = beginBuilding
    beginFloor = random.randint(1, 10)
    endFloor = random.randint(1, 10)
    while endFloor == beginFloor:
        endFloor = random.randint(1, 10)
    if random.random() < 0.5:
        curTime += random.uniform(0, 1)
    curTime = round(curTime, 1)
    personReq+=1
    return '[' + str(curTime) + ']' + str(passengerId) + '-FROM-' \
           + str(beginBuilding) + '-' + str(beginFloor) + '-TO-' + str(endBuilding) + '-' + str(endFloor)

def getFloorInput():
    global curTime
    global personReq
    beginBuilding = random.choice(Building)
    passengerId = getPersonId()
    endBuilding = random.choice(Building)
    while endBuilding == beginBuilding:
        endBuilding = random.choice(Building)
    beginFloor = random.randint(1,10)
    endFloor = beginFloor
    if floorElevatorNum[beginFloor] == 0:
        return addFloorElevator()
    if floorElevatorTime[beginFloor] != 0 and curTime < floorElevatorTime[beginFloor] + 1:
        curTime = floorElevatorTime[beginFloor] + 1.1
    elif random.random() < 0.5:
        curTime += random.uniform(0, 1)
    curTime = round(curTime, 1)
    personReq+=1
    return '[' + str(curTime) + ']' + str(passengerId) + '-FROM-' \
           + str(beginBuilding) + '-' + str(beginFloor) + '-TO-' + str(endBuilding) + '-' + str(endFloor)
'''


def getPersonRequest():
    global curTime
    global personReq
    global arrivedPassengerInfo
    global passengerList
    beginBuilding = random.choice(Building)
    passengerId = getPersonId()
    endBuilding = random.choice(Building)
    beginFloor = random.randint(1, 6)
    endFloor = random.randint(1,6)
    while beginBuilding == endBuilding and beginFloor == endFloor:
        beginBuilding = random.choice(Building)
        endBuilding = random.choice(Building)
        beginFloor = random.randint(1, 6)
        endFloor = random.randint(1, 6)
    if random.random() < 0.5:
        curTime += random.uniform(0, 1)
    curTime = round(curTime, 1)
    personReq += 1
    arrivedPassengerInfo[passengerId] = [endBuilding, endFloor]
    passengerList.append(passengerId)
    return '[' + str(curTime) + ']' + str(passengerId) + '-FROM-' \
           + str(beginBuilding) + '-' + str(beginFloor) + '-TO-' + str(endBuilding) + '-' + str(endFloor)

def addBuildingElevator(specBuild=None):
    global curElevatorNum
    global ElevatorMsg
    if specBuild is None:
        beginBuilding = random.choice(Building)
    else:
        beginBuilding = specBuild
    if buildingElevatorNum[beginBuilding] == MAX_BUILDING_ELEVATOR_NUM or curElevatorNum >= MAX_ELEVATOR_NUM:
        return getPersonRequest()
    buildingElevatorNum[beginBuilding] += 1
    curElevatorNum += 1
    elevatorId = getElevatorId()
    capacity = random.choice(elevatorCapacity)
    speed = random.choice(elevatorSpeed)
    ElevatorMsg[elevatorId] = [capacity, speed]
    return '[' + str(curTime) + ']' + 'ADD-building-' + str(elevatorId) + '-' + str(beginBuilding) + '-' + str(capacity) + '-' + str(speed)



def addFloorElevator():
    global curTime
    global curElevatorNum
    global ElevatorMsg
    beginFloor = random.randint(1, 3)
    if floorElevatorNum[beginFloor] == MAX_FLOOR_ELEVATOR_NUM or curElevatorNum >= MAX_ELEVATOR_NUM:
        return getPersonRequest()
    floorElevatorNum[beginFloor] += 1
    curElevatorNum += 1
    elevatorId = getElevatorId()
    capacity = random.choice(elevatorCapacity)
    speed = random.choice(elevatorSpeed)
    switchInfo = random.randint(1,31)
    while switchInfo == 1 or switchInfo % 2 == 0:
        switchInfo = random.randint(1, 31)
    ElevatorMsg[elevatorId] = [capacity, speed, switchInfo]
    return '[' + str(curTime) + ']' + 'ADD-floor-' + str(elevatorId) + '-' + str(beginFloor) + '-' + str(capacity) + '-' + str(speed) + '-' + str(switchInfo)


def gengerData():
    global curTime
    global personReq
    global idList
    global elevatorIdList
    global floorElevatorNum
    global buildingElevatorNum
    global floorElevatorTime
    global curElevatorNum
    global arrivedPassengerInfo
    global ElevatorMsg
    global passengerList
    idList = []
    elevatorIdList = [1, 2, 3, 4, 5]
    curTime = 1.1
    floorElevatorTime = {}
    buildingElevatorNum = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
    floorElevatorNum = {}
    arrivedPassengerInfo = {}
    ElevatorMsg = {}
    personReq = 0
    curElevatorNum = 5
    arrivedPassengerInfo = {}
    ElevatorMsg = {}
    passengerList = []
    for i in range(1, 6):
        ElevatorMsg[i] = [8, 0.6]
    ElevatorMsg[6] = [8, 0.6, 31]
    for i in range(1, 11):
        floorElevatorNum[i] = 0
    floorElevatorNum[1] = 1
    for i in range(1, 11):
        floorElevatorTime[i] = 0
    randomNum = random.randint(50, 50)
    with open("stdin.txt", 'w', encoding='utf-8') as f1:
        for _ in range(randomNum):
            randomP = random.random()
            if 0.3 <= randomP:
                input = getPersonRequest()
            elif 0.15 <= randomP < 0.3:
                input = addBuildingElevator()
            else:
                input = addFloorElevator()
            f1.write(input)
            print(input)
            f1.write('\n')
        print(personReq)
        print()
        print()
    print(curElevatorNum)
    return [personReq,arrivedPassengerInfo, ElevatorMsg, passengerList]