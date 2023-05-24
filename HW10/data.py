import collections
import random

#  #!/usr/bin/python3.9
#  -*- coding: utf-8 -*-
#  #
#  Copyright (C) 2022 #
#  @Time    : 2022/4
#  @Author  : # @Email   : sdjasjBUAA@gmail.com
#  @File    : $data.py
#  @Author  : BUAA-sdjasj
#

noPersonIdList = [i for i in range(1, 8001)]
personIdList = []
noGroupIdList = [i for i in range(1, 3001)]
groupIdList = []
messageIdList = []
noMessageIdList = [i for i in range(4000)]
personLinkedDic = collections.defaultdict(list)
groupLinkedDic = collections.defaultdict(list)
personName = ["Mark", "Alice", "Carl", "Kelly"]  # can generater same name

addPersonExp = 0.2
addRelationExp = 0.2
queryValueExp = 0.2
isCircleExp = 0.2
addGroupExp = 0.2
addToGroupExp = 0.01
queryGroupPeopleSumExp = 0.2
queryGroupValueSumExp = 0.2
queryGroupAgeVarExp = 0.2
addMessageExp = 0.2
messageTypeZero = 0.5
messageTypeOne = 0.5
sendMessageExp = 0.2
querySocialValueExp = 0.2
queryReceivedMessagesExp = 0.2
queryLeastConnectionExp = 0.2


def addPerson():
    p = random.random()
    if p > addPersonExp or personIdList == []:
        id = random.choice(noPersonIdList)
        personIdList.append(id)
        noPersonIdList.remove(id)
    else:
        id = random.choice(personIdList)

    p = random.random()
    if p < 0.9:
        name = random.choice(personName) + str(id)
    else:
        name = random.choice(personName)
    age = random.randint(0, 200)
    return "ap " + str(id) + " " + name + " " + str(age)


def addRelation():
    if len(personIdList) == 0:
        return addPerson()
    p = random.random()
    if p > addRelationExp:
        id1 = random.choice(personIdList)
        id2 = random.choice(personIdList)
    else:
        if random.random() < 0.7:
            if random.random() < 0.5:
                id1 = random.choice(noPersonIdList)
            else:
                id1 = random.choice(personIdList)
            if id1 in noPersonIdList:
                if random.random() < 0.5:
                    id2 = random.choice(noPersonIdList)
                else:
                    id2 = random.choice(personIdList)
            else:
                id2 = random.choice(noPersonIdList)
        else:
            id1 = random.choice(personIdList)
            id2 = id1
    value = random.randint(0, 1000)
    personLinkedDic[id1].append(id2)
    personLinkedDic[id2].append(id1)
    return "ar " + str(id1) + " " + str(id2) + " " + str(value)


def queryValue():
    if len(personIdList) == 0:
        return addPerson()
    p = random.random()
    if p > queryValueExp:
        id1 = random.choice(personIdList)
        id2 = random.choice(personIdList)
    else:
        if random.random() < 0.7:
            if random.random() < 0.5:
                id1 = random.choice(noPersonIdList)
            else:
                id1 = random.choice(personIdList)
            if id1 in noPersonIdList:
                if random.random() < 0.5:
                    id2 = random.choice(noPersonIdList)
                else:
                    id2 = random.choice(personIdList)
            else:
                id2 = random.choice(noPersonIdList)
        else:
            id1 = random.choice(personIdList)
            id2 = id1
    return "qv " + str(id1) + " " + str(id2)


def queryPeopleSum():
    return "qbs"


def queryCircle():
    if len(personIdList) == 0:
        return addPerson()
    p = random.random()
    if p > isCircleExp:
        id1 = random.choice(personIdList)
        id2 = random.choice(personIdList)
    else:
        if random.random() < 0.7:
            if random.random() < 0.5:
                id1 = random.choice(noPersonIdList)
            else:
                id1 = random.choice(personIdList)
            if id1 in noPersonIdList:
                if random.random() < 0.5:
                    id2 = random.choice(noPersonIdList)
                else:
                    id2 = random.choice(personIdList)
            else:
                id2 = random.choice(noPersonIdList)
        else:
            id1 = random.choice(personIdList)
            id2 = id1
    return "qv " + str(id1) + " " + str(id2)


def queryBlockSum():
    return "qbs"


def addGroup():
    p = random.random()
    if p > addGroupExp:
        if not noGroupIdList:
            return addToGroup()
        id = random.choice(noGroupIdList)
        groupIdList.append(id)
        noGroupIdList.remove(id)
    else:
        if not groupIdList:
            id = random.choice(noGroupIdList)
            groupIdList.append(id)
            noGroupIdList.remove(id)
        else:
            id = random.choice(groupIdList)
    return "ag " + str(id)


def addToGroup():
    if not groupIdList:
        return addGroup()
    if not personIdList:
        return addPerson()
    p = random.random()
    if p > addToGroupExp:
        id2 = random.choice(groupIdList)
        id1 = random.choice(personIdList)
        groupLinkedDic[id2].append(id1)
    else:
        if random.random() > 0.5:
            if not noGroupIdList:
                return queryReceivedMessages()
            id2 = random.choice(noGroupIdList)
        else:
            id2 = random.choice(groupIdList)
        if random.random() > 0.5:
            id1 = random.choice(noPersonIdList)
        else:
            id1 = random.choice(personIdList)
    return "atg {} {}".format(id1, id2)


def delFromGroup():
    if not groupIdList:
        return addGroup()
    if noPersonIdList:
        return addPerson()
    p = random.random()
    if p > addToGroupExp:
        id2 = random.choice(groupIdList)
        id1 = random.choice(personIdList)
        groupLinkedDic[id2].remove(id1)
    else:
        if random.random() > 0.5:
            id2 = random.choice(noGroupIdList)
        else:
            id2 = random.choice(groupIdList)
        if random.random() > 0.5:
            id1 = random.choice(noPersonIdList)
        else:
            id1 = random.choice(personIdList)
    return "dfg {} {}".format(id1, id2)


def queryGroupPeopleSum():
    p = random.random()
    if p > queryGroupPeopleSumExp:
        if not groupIdList:
            return addGroup()
        else:
            id1 = random.choice(groupIdList)
    else:
        id1 = random.choice(noGroupIdList)
    return "qgps {}".format(id1)


def queryGroupValueSum():
    p = random.random()
    if p > queryGroupValueSumExp:
        if not groupIdList:
            return addGroup()
        else:
            id1 = random.choice(groupIdList)
    else:
        if not noGroupIdList:
            return addToGroup()
        id1 = random.choice(noGroupIdList)
    return "qgvs {}".format(id1)


def queryGroupAgeVar():
    p = random.random()
    if p > queryGroupAgeVarExp:
        if not groupIdList:
            return addGroup()
        else:
            id1 = random.choice(groupIdList)
    else:
        if not noGroupIdList:
            return addToGroup()
        id1 = random.choice(noGroupIdList)
    return "qgav {}".format(id1)


def addMessage():
    p = random.random()
    if p < addMessageExp:
        p1 = random.random()
        if p1 > 0.5:
            if not messageIdList:
                return addMessage()
            messageId = random.choice(messageIdList)
            if personIdList:
                id1 = random.choice(personIdList)
            else:
                id1 = random.choice(noPersonIdList)
            id2 = id1
        else:
            messageId = random.choice(noMessageIdList)
            noMessageIdList.remove(messageId)
            messageIdList.append(messageId)
            if personIdList:
                id1 = random.choice(personIdList)
            else:
                id1 = random.choice(noPersonIdList)
            id2 = id1
        messageType = random.randint(0, 1)
        socialValue = random.randint(-1000, 1000)
    else:
        p2 = random.random()
        if p2 > messageTypeZero:
            messageType = 0
            messageId = random.choice(noMessageIdList)
            noMessageIdList.remove(messageId)
            messageIdList.append(messageId)
            if len(personIdList) < 3:
                return addPerson()
            p3 = random.random()
            if p3 > sendMessageExp:
                if not personLinkedDic:
                    return addRelation()
                id1 = random.choice(list(personLinkedDic.keys()))
            else:
                id1 = random.choice(personIdList)
            if id1 in list(personLinkedDic.keys()):
                id2 = random.choice(personLinkedDic[id1])
            else:
                id2 = random.choice(personIdList)
            while id2 == id1:
                id2 = random.choice(personIdList)
        else:
            messageType = 1
            messageId = random.choice(noMessageIdList)
            noMessageIdList.remove(messageId)
            messageIdList.append(messageId)
            if len(groupIdList) < 1:
                return addGroup()
            if not personIdList:
                return addPerson()
            if not groupLinkedDic:
                return addToGroup()
            if random.random() > sendMessageExp:
                id2 = random.choice(list(groupLinkedDic.keys()))
                id1 = random.choice(groupLinkedDic[id2])
            else:
                id2 = random.choice(groupIdList)
                id1 = random.choice(personIdList)
        socialValue = random.randint(-1000, 1000)
    return "am {} {} {} {} {}".format(messageId, socialValue, messageType, id1, id2)


def sendMessage():
    if not messageIdList:
        return addMessage()
    id1 = random.choice(messageIdList)
    messageIdList.remove(id1)
    return "sm {}".format(id1)


def queryReceivedMessages():
    p = random.random()
    if p > queryReceivedMessagesExp:
        if not personIdList:
            return addPerson()
        id1 = random.choice(personIdList)
    else:
        id1 = random.choice(noPersonIdList)
    return "qrm {}".format(id1)


def querySocialValue():
    p = random.random()
    if p > querySocialValueExp:
        if not personIdList:
            return addPerson()
        id1 = random.choice(personIdList)
    else:
        id1 = random.choice(noPersonIdList)
    return "qsv {}".format(id1)


def queryLeastConnection():
    p = random.random()
    if p > queryLeastConnectionExp:
        if not personIdList:
            return addPerson()
        id1 = random.choice(personIdList)
    else:
        id1 = random.choice(noPersonIdList)
    return "qlc {}".format(id1)


def generCirData():
    global noPersonIdList
    global personIdList
    global noGroupIdList
    global groupIdList
    noPersonIdList = [i for i in range(1, 801)]
    personIdList = []
    noGroupIdList = [i for i in range(1, 301)]
    groupIdList = []
    s = ""
    for i in range(1000):
        p = random.random()
        if 0.7 < p:
            context = addPerson()
        elif 0.3 < p <= 0.7:
            context = addRelation()
        elif 0.15 < p <= 0.3:
            context = queryCircle()
        else:
            context = queryBlockSum()
        s += context
        s += '\n'
    return s


def gengerData():
    global noPersonIdList
    global personIdList
    global noGroupIdList
    global groupIdList
    noPersonIdList = [i for i in range(1, 801)]
    personIdList = []
    noGroupIdList = [i for i in range(1, 301)]
    groupIdList = []
    s = ""
    for i in range(10000):
        if len(personIdList) <= 25:
            p = random.random()
            if 0.85 < p:
                context = addPerson()
            elif 0.55 < p <= 0.85:
                context = addRelation()
            elif 0.45 < p <= 0.55:
                context = addGroup()
            elif 0.35 < p <= 0.45:
                context = queryValue()
            elif 0.3 < p <= 0.35:
                context = addToGroup()
            elif 0.25 < p <= 0.3:
                context = delFromGroup()
            elif 0.15 < p <= 0.25:
                context = queryCircle()
            elif 0.05 < p <= 0.15:
                context = queryBlockSum()
            else:
                context = queryPeopleSum()
        else:
            p = random.random()
            if 0.65 < p:
                context = addRelation()
            elif 0.45 < p <= 0.65:
                context = queryBlockSum()
            elif 0.20 < p <= 0.45:
                context = queryCircle()
            elif 0.15 < p <= 0.20:
                context = addToGroup()
            elif 0.10 < p <= 0.15:
                context = delFromGroup()
            elif 0.05 < p <= 0.10:
                context = queryValue()
            else:
                context = addGroup()
        s += context
        s += '\n'
    return s


def gengerData2():
    global noPersonIdList
    global personIdList
    global noGroupIdList
    global groupIdList
    global messageIdList
    global noMessageIdList
    global groupLinkedDic
    global personLinkedDic
    noPersonIdList = [i for i in range(1, 10001)]
    personIdList = []
    noGroupIdList = [i for i in range(1, 10001)]
    groupIdList = []
    messageIdList = []
    noMessageIdList = [i for i in range(10000)]
    personLinkedDic = collections.defaultdict(list)
    groupLinkedDic = collections.defaultdict(list)

    s = ""
    for i in range(10000):
        if len(personIdList) <= 1500:
            p = random.random()
            if 0.95 < p:
                context = addPerson()
            elif 0.90 < p <= 0.95:
                context = addRelation()
            elif 0.80 < p <= 0.85:
                context = addGroup()
            elif 0.75 < p <= 0.80:
                context = queryValue()
            elif 0.70 < p <= 0.75:
                context = addToGroup()
            elif 0.65 < p <= 0.70:
                context = delFromGroup()
            elif 0.60 < p <= 0.65:
                context = queryCircle()
            elif 0.55 < p <= 0.60:
                context = queryBlockSum()
            elif 0.50 < p <= 0.55:
                context = queryPeopleSum()
            elif 0.45 < p <= 0.5:
                context = queryGroupValueSum()
            elif 0.4 < p <= 0.45:
                context = queryGroupAgeVar()
            elif 0.35 < p <= 0.4:
                context = addMessage()
            elif 0.3 < p <= 0.35:
                context = sendMessage()
            elif 0.25 < p <= 0.3:
                context = querySocialValue()
            elif 0.2 < p <= 0.25:
                context = queryReceivedMessages()
            elif 0.15 < p <= 0.20:
                context = queryLeastConnection()
            elif 0.1 < p <= 0.15:
                context = addMessage()
            elif 0.05 < p <= 0.1:
                context = sendMessage()
            else:
                context = queryLeastConnection()
        else:
            p = random.random()
            if 0.65 < p:
                context = addMessage()
            elif 0.35 < p:
                context = sendMessage()
            else:
                context = addGroup()
        s += context
        s += '\n'
    return s


def gengerData3():
    global noPersonIdList
    global personIdList
    global noGroupIdList
    global groupIdList
    global messageIdList
    global noMessageIdList
    global groupLinkedDic
    global personLinkedDic
    noPersonIdList = [i for i in range(1, 2501)]
    personIdList = []
    noGroupIdList = [i for i in range(1, 2)]
    groupIdList = []
    messageIdList = []
    noMessageIdList = [i for i in range(5000)]
    personLinkedDic = collections.defaultdict(list)
    groupLinkedDic = collections.defaultdict(list)

    s = ""
    for i in range(20000):
        if i > 1000:
            context = queryLeastConnection()
        elif len(personIdList) <= 2500:
            p = random.random()
            if 0.95 < p:
                context = addPerson()
            elif 0.90 < p <= 0.95:
                context = addRelation()
            elif 0.80 < p <= 0.85:
                context = addGroup()
            elif 0.75 < p <= 0.80:
                context = queryValue()
            elif 0.70 < p <= 0.75:
                context = addToGroup()
            elif 0.65 < p <= 0.70:
                context = delFromGroup()
            elif 0.60 < p <= 0.65:
                context = queryCircle()
            elif 0.55 < p <= 0.60:
                context = queryBlockSum()
            elif 0.50 < p <= 0.55:
                context = queryPeopleSum()
            elif 0.45 < p <= 0.5:
                context = queryGroupValueSum()
            elif 0.4 < p <= 0.45:
                context = queryGroupAgeVar()
            elif 0.35 < p <= 0.4:
                context = addMessage()
            elif 0.3 < p <= 0.35:
                context = sendMessage()
            elif 0.25 < p <= 0.3:
                context = querySocialValue()
            elif 0.2 < p <= 0.25:
                context = queryReceivedMessages()
            elif 0.15 < p <= 0.20:
                context = queryLeastConnection()
            elif 0.1 < p <= 0.15:
                context = addMessage()
            elif 0.05 < p <= 0.1:
                context = sendMessage()
            else:
                context = queryLeastConnection()
        else:
            p = random.random()
            if 0.65 < p:
                context = addMessage()
            elif 0.35 < p:
                context = sendMessage()
            else:
                context = queryLeastConnection()
        s += context
        s += '\n'
    return s


def gengerData4():
    global noPersonIdList
    global personIdList
    global noGroupIdList
    global groupIdList
    global messageIdList
    global noMessageIdList
    global groupLinkedDic
    global personLinkedDic
    noPersonIdList = [i for i in range(1, 100001)]
    personIdList = []
    noGroupIdList = [i for i in range(1, 100001)]
    groupIdList = []
    messageIdList = []
    noMessageIdList = [i for i in range(100000)]
    personLinkedDic = collections.defaultdict(list)
    groupLinkedDic = collections.defaultdict(list)

    s = ""
    for i in range(50000):
        if len(personIdList) <= 30000:
            p = random.random()
            if 0.9 < p:
                context = addPerson()
            elif 0.80 < p <= 0.9:
                context = addRelation()
            elif 0.70 < p <= 0.8:
                context = addGroup()
            elif 0.4 < p <= 0.7:
                context = addToGroup()
            elif 0.35 < p <= 0.4:
                context = delFromGroup()
            elif 0.3 < p <= 0.35:
                context = queryGroupValueSum()
            elif 0.1 < p <= 0.3:
                context = queryGroupAgeVar()
            elif 0.07 < p <= 0.1:
                context = addMessage()
            elif 0.04 < p <= 0.07:
                context = sendMessage()
            elif 0.02 < p <= 0.04:
                context = querySocialValue()
            else:
                context = queryReceivedMessages()
        else:
            p = random.random()
            if 0.65 < p:
                context = addToGroup()
            elif 0.35 < p:
                context = queryGroupAgeVar()
            else:
                context = queryLeastConnection()
        s += context
        s += '\n'
    return s