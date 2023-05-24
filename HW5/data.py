import random

def getId(idList):
    passengerId = random.randint(1,1000)
    while passengerId in idList:
        passengerId = random.randint(1,1000)
    idList.append(passengerId)
    return passengerId

def getInput(curTime, passengerId, beginBuilding, beginFloor, endBuilding, endFloor):
    return '['+str(curTime)+']'+ str(passengerId) + '-FROM-'\
           +str(beginBuilding)+'-'+str(beginFloor)+'-TO-'+ str(endBuilding)+'-'+str(endFloor)


def gengerData():
    randomNum = random.randint(40,70)
    curTime = 0
    Building = ['A', 'B', 'C', 'D', 'E']
    idList = []
    with open("stdin.txt",'w',encoding='utf-8') as f1:
        for i in range(randomNum):
            beginBuilding = random.choice(Building)
            passengerId = getId(idList=idList)
            endBuilding = beginBuilding
            beginFloor = random.randint(1,10)
            endFloor = random.randint(1,10)
            while endFloor == beginFloor:
                endFloor = random.randint(1,10)
            if random.random() < 0.3:
                curTime += random.uniform(0,0.8)
            curTime = round(curTime, 1)
            input = getInput(curTime, passengerId, beginBuilding, beginFloor, endBuilding, endFloor)
            f1.write(input)
            print(input)
            f1.write('\n')
        print(len(idList))
        print()
        print()
    return randomNum