
import random

MAX_BUILDING_ELEVATOR_NUM = 5
MAX_FLOOR_ELEVATOR_NUM = 3
Building = ['A', 'B', 'C', 'D', 'E']
idList = []
elevatorIdList = [1, 2, 3, 4, 5]
curTime = 0
floorElevatorTime = {}
buildingElevatorNum = {'A': 1, 'B':1, 'C':1, 'D':1, 'E':1}
floorElevatorNum = {}
personReq = 0
for i in range(1,11):
    floorElevatorNum[i] = 0
for i in range(1,11):
    floorElevatorTime[i] = 0


def getPersonId():
    passengerId = random.randint(1, 1000)
    while passengerId in idList:
        passengerId = random.randint(1, 1000)
    idList.append(passengerId)
    return passengerId


def getElevatorId():
    elevatorId = random.randint(6, 1000)
    while elevatorId in elevatorIdList:
        elevatorId = random.randint(6, 1000)
    elevatorIdList.append(elevatorId)
    return elevatorId


def getBuildingInput():
    global curTime
    global personReq
    beginBuilding = random.choice(Building)
    passengerId = getPersonId()
    endBuilding = beginBuilding
    beginFloor = random.randint(1, 3)
    endFloor = random.randint(1, 10)
    while endFloor == beginFloor:
        endFloor = random.randint(1, 10)
    if random.random() < 0.2:
        curTime += random.uniform(0, 0.4)
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
    beginFloor = random.randint(1,2)
    endFloor = beginFloor
    if floorElevatorNum[beginFloor] == 0:
        return addFloorElevator()
    if floorElevatorTime[beginFloor] != 0 and curTime < floorElevatorTime[beginFloor] + 1:
        curTime = floorElevatorTime[beginFloor] + 1.1
    elif random.random() < 0.2:
        curTime += random.uniform(0, 0.4)
    curTime = round(curTime, 1)
    personReq+=1
    return '[' + str(curTime) + ']' + str(passengerId) + '-FROM-' \
           + str(beginBuilding) + '-' + str(beginFloor) + '-TO-' + str(endBuilding) + '-' + str(endFloor)

def addBuildingElevator(specBuild=None):
    if specBuild is None:
        beginBuilding = random.choice(Building)
    else:
        beginBuilding = specBuild
    if buildingElevatorNum[beginBuilding] == MAX_BUILDING_ELEVATOR_NUM:
        return getFloorInput()
    buildingElevatorNum[beginBuilding] += 1
    elevatorId = getElevatorId()
    return '[' + str(curTime) + ']' + 'ADD-building-' + str(elevatorId) + '-' + str(beginBuilding)


def addFloorElevator():
    global curTime
    beginFloor = random.randint(1, 3)
    if floorElevatorNum[beginFloor] == MAX_FLOOR_ELEVATOR_NUM:
        return getFloorInput()
    floorElevatorNum[beginFloor] += 1
    elevatorId = getElevatorId()
    if floorElevatorTime[beginFloor] == 0:
        if curTime == 0:
            curTime = 0.1
        floorElevatorTime[beginFloor] = curTime
    return '[' + str(curTime) + ']' + 'ADD-floor-' + str(elevatorId) + '-' + str(beginFloor)


def gengerData():
    global curTime
    global personReq
    global idList
    global elevatorIdList
    global floorElevatorNum
    global buildingElevatorNum
    global floorElevatorTime
    idList = []
    elevatorIdList = [1, 2, 3, 4, 5]
    curTime = 1.1
    floorElevatorTime = {}
    buildingElevatorNum = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
    floorElevatorNum = {}
    personReq = 0
    for i in range(1, 11):
        floorElevatorNum[i] = 0
    for i in range(1, 11):
        floorElevatorTime[i] = 0
    randomNum = random.randint(80, 90)
    with open("stdin.txt", 'w', encoding='utf-8') as f1:
        for _ in range(randomNum):
            randomP = random.random()
            if 0.9 <= randomP:
                input = getBuildingInput()
            elif 0.2 <= randomP < 0.9:
                input = getFloorInput()
            elif 0.1 <= randomP < 0.2:
                input = addBuildingElevator()
            else:
                input = addFloorElevator()
            f1.write(input)
            print(input)
            f1.write('\n')
        print(personReq)
        print()
        print()
    return personReq