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

noPersonIdList = [i for i in range(1,801)]
personIdList = []
noGroupIdList = [i for i in range(1,301)]
groupIdList = []
personName = ["Mark", "Alice", "Carl", "Kelly"] #can generater same name

addPersonExp = 0.8
addRelationExp = 0.8
queryValueExp = 0.8
isCircleExp = 0.8
addGroupExp = 0.8
addToGroupExp = 0.8

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
    value = random.randint(0,1000)
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
    if noPersonIdList:
        return addPerson()
    p = random.random()
    if p > addToGroupExp:
        id2 = random.choice(groupIdList)
        id1 = random.choice(personIdList)
    else:
        if random.random() > 0.5:
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
        s+='\n'
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
    for i in range(1000):
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
        s+='\n'
    return s
