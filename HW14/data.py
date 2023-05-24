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

##########Class Diagram###########
totalParentId = "ooooooo"
visibilities = ['public', 'private', 'protected', 'package']
NamesNoId = ['lab', 'oo', 'os', 'co', 'gpa']
# NamesNoId = ['lab']
normalType = ['short', 'byte', 'int', 'long', 'char', 'boolean', 'float', 'double', 'String']
# normalType = ['String']
operationType = normalType + ['void']
parameterDirection = ['return', 'in']
operationIdList = []
classNameList = []
classIdList = []
interfaceIdList = []
classHasSuperClassList = []
classOfSuperClassDic = collections.defaultdict(list)
interfaceExtendDic = collections.defaultdict(list)
classRealizeInterfaceDic = collections.defaultdict(list)
operationIdMapClassId = {}
operationHasReturnParameterList = []
totalId = 0
classNameIsSameP = 0.05
attributeIsNormal = 0.4
attributeIsClass = 0.5
attributeTypeIsError = 0.3
attributeTypeIsParentClass = 0.8
parameterIsNoraml = 0.7
parameterIsError = 0
##########state diagram################
stateMachineIdToNameDic = {}
statedMachineNameList = []
statedMachineIdList = []
stateMachineToRegionDic = {}
regionIdList = []
regionToStateDic = collections.defaultdict(list)
regionToStateNameDic = collections.defaultdict(list)
regionToStartStateDic = collections.defaultdict(str)
regionToFinalStateDic = collections.defaultdict(list)
transitionIdList = []
statedMachineNameIsSame = 0.05
stateNameIsSame = 0.05
transitionFromBegin = 0.2
##########sequence Diagram############
interactionIdList = []
interactionNameList = []
interactionToLifelineIdDic = collections.defaultdict(list)
interactionIdToNameDic = collections.defaultdict(list)
interactionToLifelineNameDic = collections.defaultdict(list)
interactionToMessageDic = collections.defaultdict(list)
interactionToEndPointDic = collections.defaultdict(list)
interactionNameIsSame = 0.05
lifelineNameIsSame = 0.05
messageType = ['createMessage', 'synchCall']


def generInteraction():
    global totalId
    global totalParentId
    p = random.random()
    if p < interactionNameIsSame and interactionNameList:
        name = random.choice(interactionNameList)
    else:
        name = random.choice(NamesNoId) + str(totalId)
    interactionNameList.append(name)
    thisId = str(totalId)
    totalId += 1
    parentId = totalParentId
    visibility = random.choice(visibilities)
    interactionIdList.append(thisId)
    interactionIdToNameDic[thisId].append(name)
    return '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLInteraction\",\"_id\":\"{}\"}}'''.format(
        parentId, visibility, name, thisId)


def generLifeline():
    global totalId
    global totalParentId
    if not interactionIdList:
        return generInteraction()
    if not interactionIdList:
        return generInteraction()
    parentId = random.choice(interactionIdList)
    p = random.random()
    if p < lifelineNameIsSame and interactionToLifelineIdDic[parentId]:
        name = random.choice(interactionToLifelineNameDic[parentId])
    else:
        name = random.choice(NamesNoId) + str(totalId)
    thisId = str(totalId)
    totalId += 1
    interactionToLifelineIdDic[parentId].append(thisId)
    interactionToLifelineNameDic[parentId].append(name)
    return "{{\"_parent\":\"{}\",\"visibility\":\"public\",\"name\":\"{}\",\"_type\":\"UMLLifeline\",\"isMultiInstance\":false,\"_id\":\"{}\",\"represent\":\"111\"}}".format(
        parentId, name, thisId)


def generEndPoint():
    global totalId
    global totalParentId
    if not interactionIdList:
        return generInteraction()
    visibility = random.choice(visibilities)
    parentId = random.choice(interactionIdList)
    thisId = str(totalId)
    totalId += 1
    interactionToEndPointDic[parentId].append(thisId)
    return '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":null,\"_type\":\"UMLEndpoint\",\"_id\":\"{}\"}}'''.format(
        parentId, visibility, thisId)


def generMessage():
    return random.choice([generFoundMessage, generLostMessage, generCreateMessage])()


def generFoundMessage():
    global totalId
    global totalParentId
    if not interactionIdList:
        return generInteraction()
    parentId = random.choice(interactionIdList)
    if not interactionToEndPointDic[parentId]:
        return generEndPoint()
    sourceId = random.choice(interactionToEndPointDic[parentId])
    if not interactionToLifelineIdDic[parentId]:
        return generLifeline()
    targetId = random.choice(interactionToLifelineIdDic[parentId])
    name = random.choice(NamesNoId) + str(totalId)
    thisId = str(totalId)
    totalId += 1
    return "{{\"messageSort\":\"synchCall\",\"_parent\":\"{}\",\"visibility\":\"public\",\"name\":\"{}\",\"_type\":\"UMLMessage\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, name, thisId, sourceId, targetId)


def generLostMessage():
    global totalId
    global totalParentId
    if not interactionIdList:
        return generInteraction()
    parentId = random.choice(interactionIdList)
    if not interactionToEndPointDic[parentId]:
        return generEndPoint()
    targetId = random.choice(interactionToEndPointDic[parentId])
    if not interactionToLifelineIdDic[parentId]:
        return generLifeline()
    sourceId = random.choice(interactionToLifelineIdDic[parentId])
    name = random.choice(NamesNoId) + str(totalId)
    thisId = str(totalId)
    totalId += 1
    return "{{\"messageSort\":\"synchCall\",\"_parent\":\"{}\",\"visibility\":\"public\",\"name\":\"{}\",\"_type\":\"UMLMessage\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, name, thisId, sourceId, targetId)


def generCreateMessage():
    global totalId
    global totalParentId
    if not interactionIdList:
        return generInteraction()
    parentId = random.choice(interactionIdList)
    if len(interactionToLifelineIdDic[parentId]) < 2:
        return generLifeline()
    sourceId = random.choice(interactionToLifelineIdDic[parentId])
    a = set(interactionToLifelineIdDic[parentId]) - set(sourceId)
    targetId = random.choice(list(a))
    name = random.choice(NamesNoId) + str(totalId)
    thisId = str(totalId)
    totalId += 1
    return "{{\"messageSort\":\"createMessage\",\"_parent\":\"{}\",\"visibility\":\"public\",\"name\":\"{}\",\"_type\":\"UMLMessage\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, name, thisId, sourceId, targetId)


def generStateMachine():
    global totalId
    global totalParentId
    p = random.random()
    if p < statedMachineNameIsSame and statedMachineNameList:
        name = random.choice(statedMachineNameList)
    else:
        name = random.choice(NamesNoId) + str(totalId)
        statedMachineNameList.append(name)
    p = random.random()
    if p > 0.8:
        parentId = totalParentId
        parentId = "\"{}\"".format(parentId)
    else:
        parentId = 'null'
    statedMachineId = str(totalId)
    statedMachineIdList.insert(0, statedMachineId)
    totalId += 1
    stateMachineIdToNameDic[statedMachineId] = name
    return '''{{\"_parent\":{},\"name\":\"{}\",\"_type\":\"UMLStateMachine\",\"_id\":\"{}\"}}'''.format(
        parentId, name, statedMachineId)


def generRegion():
    global totalId
    global totalParentId
    if not statedMachineIdList or len(statedMachineIdList) == len(stateMachineToRegionDic.keys()):
        return generState()
    visibility = random.choice(visibilities)
    for ele in statedMachineIdList:
        if ele not in list(stateMachineToRegionDic.keys()):
            parentId = ele
    thisId = str(totalId)
    regionIdList.append(thisId)
    totalId += 1
    beginState = generBeginState(thisId)
    stateMachineToRegionDic[parentId] = thisId
    return beginState + '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":{},\"_type\":\"UMLRegion\",\"_id\":\"{}\"}}'''.format(
        parentId, visibility, 'null', thisId)


def generBeginState(parentId: str):
    global totalId
    global totalParentId
    visibility = random.choice(visibilities)
    thisId = str(totalId)
    totalId += 1
    regionToStartStateDic[parentId] = thisId
    return '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":{},\"_type\":\"UMLPseudostate\",\"_id\":\"{}\"}}\n'''.format(
        parentId, visibility, 'null', thisId)


def generState(parentId=None):
    global totalId
    global totalParentId
    global regionToStateDic
    if not regionIdList or not statedMachineIdList:
        return generStateMachine()
    p = random.random()
    if p < stateNameIsSame:
        name = random.choice(NamesNoId)
    else:
        name = random.choice(NamesNoId) + str(totalId)
    visibility = random.choice(visibilities)
    if not parentId:
        parentId = random.choice(regionIdList)
    thisId = str(totalId)
    regionToStateDic[parentId].append(thisId)
    regionToStateNameDic[parentId].append(name)
    totalId += 1
    return '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLState\",\"_id\":\"{}\"}}'''.format(
        parentId, visibility, name, thisId)


def generFinalState():
    global totalId
    global totalParentId
    if not regionIdList or not statedMachineIdList:
        return generStateMachine()
    visibility = random.choice(visibilities)
    parentId = random.choice(regionIdList)
    thisId = str(totalId)
    totalId += 1
    regionToFinalStateDic[parentId].append(thisId)
    return '''{{\"_parent\":\"{0}\",\"visibility\":\"{1}\",\"name\":{2},\"_type\":\"UMLFinalState\",\"_id\":\"{3}\"}}'''.format(
        parentId, visibility, 'null', thisId)


def generTransition():
    global totalId
    global totalParentId
    if not regionToStateDic:
        return generState()
    regionId = random.choice(list(regionToStateDic.keys()))
    if len(regionToStateDic[regionId]) < 2:
        return generState(regionId)
    p = random.random()
    if p < transitionFromBegin:
        sourceId = regionToStartStateDic[regionId]
    else:
        sourceId = random.choice(regionToStateDic[regionId])
    realStateList = regionToStateDic[regionId] + regionToFinalStateDic[regionId]
    targetId = random.choice(realStateList)
    thisId = str(totalId)
    totalId += 1
    transitionIdList.append(thisId)
    s = generEvent(thisId) + '\n'
    return s + "{{\"_parent\":\"{}\",\"visibility\":\"public\",\"guard\":null,\"name\":null,\"_type\":\"UMLTransition\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        regionId, thisId, sourceId, targetId)


def generEvent(parentId=None):
    global totalId
    global totalParentId
    if parentId == None:
        if not transitionIdList:
            return generTransition()
        else:
            parentId = random.choice(transitionIdList)
    name = random.choice(NamesNoId)
    thisId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"expression\":null,\"visibility\":\"public\",\"name\":\"{}\",\"_type\":\"UMLEvent\",\"_id\":\"{}\",\"value\":null}}".format(
        parentId, name, thisId)


def generUmlClass():
    global totalId
    global totalParentId
    p = random.random()
    if p < classNameIsSameP and classNameList:
        name = random.choice(classNameList)
    else:
        name = random.choice(NamesNoId) + str(totalId)
    classNameList.append(name)
    visibility = random.choice(visibilities)
    p = random.random()
    if p > 0.8:
        parentId = totalParentId
    else:
        parentId = 'null'
    classId = str(totalId)
    classIdList.insert(0, classId)
    totalId += 1
    return '''{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLClass\",\"_id\":\"{}\"}}'''.format(
        parentId, visibility, name, classId)


def generUmlInterface():
    global totalId
    global totalParentId
    name = random.choice(NamesNoId) + str(totalId)
    visibility = random.choice(visibilities)
    p = random.random()
    if p > 0.8:
        parentId = totalParentId
    else:
        parentId = 'null'
    interfaceId = str(totalId)
    interfaceIdList.append(interfaceId)
    totalId += 1
    return r'''{{"_parent":"{}","visibility":"{}","name":"{}","_type":"UMLInterface","_id":"{}"}}'''.format(
        parentId,
        visibility, name,
        interfaceId)


def generAttribute():
    global totalId
    if not classIdList:
        return generUmlClass()
    name = random.choice(NamesNoId) + str(totalId)
    visibility = random.choice(visibilities)
    p = random.random()
    if p < attributeIsClass or not interfaceIdList:
        parentId = random.choice(classIdList)
    else:
        parentId = random.choice(interfaceIdList)
    p = random.random()
    if p > attributeTypeIsError:
        p1 = random.random()
        if p1 < attributeIsNormal:
            attributeType = random.choice(normalType)
            attributeType = "\"{}\"".format(attributeType)
        else:
            attributeType = random.choice(classIdList)
            p2 = random.random()
            if p2 < attributeTypeIsParentClass:
                attributeType = parentId
            p3 = random.random()
            if p3 > 0.8:
                attributeType = random.choice(interfaceIdList)
            attributeType = "{{\"$ref\":\"{}\"}}".format(attributeType)
    else:
        attributeType = random.choice(classNameList)
        attributeType = "\"{}\"".format(attributeType)
    attributeId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLAttribute\",\"_id\":\"{}\"," \
           "\"type\":{}}}".format(
        parentId, visibility, name, attributeId, attributeType)


def generUmlGeneralizationOfClass():
    global totalId
    if len(classIdList) < 2:
        return generUmlClass()
    """
    a = set(classIdList)
    b = set(classHasSuperClassList)
    c = a - b
    if not c:
        return generUmlClass()
    """
    flag = False
    for i in range(len(classIdList) - 1):
        if not classOfSuperClassDic[classIdList[i]]:
            flag = True
            break
    if not flag:
        return generUmlInterface()
    a = random.randint(0, len(classIdList) - 2)
    while classOfSuperClassDic[classIdList[a]]:
        a = random.randint(0, len(classIdList) - 2)
    b = random.randint(a + 1, len(classIdList) - 1)
    subClassId = classIdList[a]
    superClassId = classIdList[b]
    classOfSuperClassDic[subClassId] = superClassId
    p = random.random()
    if p > 0.8:
        parentId = subClassId
    else:
        parentId = 'null'
    name = 'null'
    thisId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"name\":{},\"_type\":\"UMLGeneralization\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, name, thisId, subClassId, superClassId)


def generUmlGeneralizationOfInterface():
    global totalId
    if len(interfaceIdList) < 2:
        return generUmlInterface()
    a = random.randint(0, len(interfaceIdList) - 2)
    b = random.randint(a + 1, len(interfaceIdList) - 1)
    while interfaceIdList[b] in interfaceExtendDic[interfaceIdList[a]]:
        a = random.randint(0, len(interfaceIdList) - 2)
        b = random.randint(a + 1, len(interfaceIdList) - 1)
    subInterface = interfaceIdList[a]
    superInterface = interfaceIdList[b]
    p = random.random()
    if p > 0.8:
        parentId = subInterface
    else:
        parentId = 'null'
    name = 'null'
    interfaceExtendDic[superInterface] = subInterface
    thisId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"name\":{},\"_type\":\"UMLGeneralization\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, name, thisId, subInterface, superInterface)


def generOperation():
    global totalId
    if not classIdList:
        return generUmlClass()
    name = random.choice(NamesNoId)
    visibility = random.choice(visibilities)
    parentId = random.choice(classIdList)
    thisId = str(totalId)
    totalId += 1
    operationIdList.append(thisId)
    operationIdMapClassId[thisId] = parentId
    return "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLOperation\",\"_id\":\"{}\"}}".format(
        parentId, visibility, name, thisId)


def generParameter():
    global totalId
    if not classIdList:
        return generUmlClass()
    if not operationIdList:
        return generOperation()
    name = random.choice(NamesNoId)
    visibility = random.choice(visibilities)
    parentId = random.choice(operationIdList)
    direction = random.choice(parameterDirection)
    if direction == 'return' and parentId in operationHasReturnParameterList:
        direction = 'in'
    p = random.random()
    if p < parameterIsNoraml:
        p1 = random.random()
        if p1 < parameterIsError:
            parameterType = random.choice(classNameList)
        else:
            if direction == 'return':
                parameterType = random.choice(operationType)
            else:
                parameterType = random.choice(normalType)
        parameterType = "\"{}\"".format(parameterType)
    else:
        p2 = random.random()
        if p2 > 0.7:
            parameterType = random.choice(classIdList)
        elif p2 > 0.4:
            parameterType = random.choice(interfaceIdList)
        else:
            parameterType = operationIdMapClassId[parentId]
        parameterType = "{{\"$ref\":\"{}\"}}".format(parameterType)
    if direction == 'return':
        p = random.random()
        if p > 0.5:
            name = random.choice(classNameList)
        else:
            name = 'null'
        operationHasReturnParameterList.append(parentId)
    thisId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"visibility\":\"{}\",\"name\":\"{}\",\"_type\":\"UMLParameter\",\"_id\":\"{}\",\"type\":{},\"direction\":\"{}\"}}".format(
        parentId, visibility, name, thisId, parameterType, direction)


def generUmlInterfaceRealization():
    global totalId
    if not classIdList:
        return generUmlClass()
    if not interfaceIdList:
        return generUmlInterface()
    subClass = random.choice(classIdList)
    superInterface = random.choice(interfaceIdList)
    while superInterface in classRealizeInterfaceDic[subClass]:
        superInterface = random.choice(interfaceIdList)
    classRealizeInterfaceDic[subClass].append(superInterface)
    p = random.random()
    if p > 0.8:
        parentId = subClass
    else:
        parentId = 'null'
    thisId = str(totalId)
    totalId += 1
    return "{{\"_parent\":\"{}\",\"name\":null,\"_type\":\"UMLInterfaceRealization\",\"_id\":\"{}\",\"source\":\"{}\",\"target\":\"{}\"}}".format(
        parentId, thisId, subClass, superInterface)


def CLASS_SUBCLASS_COUNT():
    p = random.random()
    if p > 0.01:
        return "CLASS_SUBCLASS_COUNT {}".format(random.choice(classNameList))
    else:
        return "CLASS_SUBCLASS_COUNT {}".format("fuck")


def CLASS_OPERATION_COUNT():
    p = random.random()
    if p > 0.01:
        return "CLASS_OPERATION_COUNT {}".format(random.choice(classNameList))
    else:
        return "CLASS_OPERATION_COUNT {}".format("fuck")


def CLASS_OPERATION_VISIBILITY():
    p = random.random()
    if p > 0.01:
        return "CLASS_OPERATION_VISIBILITY {} {}".format(random.choice(classNameList), random.choice(NamesNoId))
    else:
        return "CLASS_OPERATION_VISIBILITY {} {}".format("fuck", 'lab')


def CLASS_OPERATION_COUPLING_DEGREE():
    p = random.random()
    if p > 0.01:
        return "CLASS_OPERATION_COUPLING_DEGREE {} {}".format(random.choice(classNameList), random.choice(NamesNoId))
    else:
        return "CLASS_OPERATION_COUPLING_DEGREE {} {}".format("fuck", 'lab')


def CLASS_ATTR_COUPLING_DEGREE():
    p = random.random()
    if p > 0.01:
        return "CLASS_ATTR_COUPLING_DEGREE {}".format(random.choice(classNameList))
    else:
        return "CLASS_ATTR_COUPLING_DEGREE {}".format("fuck")


def CLASS_IMPLEMENT_INTERFACE_LIST():
    p = random.random()
    if p > 0.01:
        return "CLASS_IMPLEMENT_INTERFACE_LIST {}".format(random.choice(classNameList))
    else:
        return "CLASS_IMPLEMENT_INTERFACE_LIST {}".format("fuck")


def CLASS_DEPTH_OF_INHERITANCE():
    p = random.random()
    if p > 0.01:
        return "CLASS_DEPTH_OF_INHERITANCE {}".format(random.choice(classNameList))
    else:
        return "CLASS_DEPTH_OF_INHERITANCE {}".format("fuck")


def STATE_COUNT():
    p = random.random()
    if p > 0.01:
        a = random.choice(statedMachineNameList)
        return "STATE_COUNT {}".format(a)
    else:
        return "STATE_COUNT {}".format('fuck')


def STATE_IS_CRITICAL_POINT():
    p = random.random()
    machineId = random.choice(statedMachineIdList)
    machineName = stateMachineIdToNameDic[machineId]
    while not regionToStateNameDic[stateMachineToRegionDic[machineId]]:
        machineId = random.choice(statedMachineIdList)
        machineName = stateMachineIdToNameDic[machineId]
    stateName = random.choice(regionToStateNameDic[stateMachineToRegionDic[machineId]])
    if p > 0.02:
        return "STATE_IS_CRITICAL_POINT {} {}".format(machineName, stateName)
    elif p > 0.01:
        return "STATE_IS_CRITICAL_POINT {} {}".format('fuck', 'fuck')
    else:
        return "STATE_IS_CRITICAL_POINT {} {}".format(machineName, 'fuck')


def TRANSITION_TRIGGER():
    p = random.random()
    machineId = random.choice(statedMachineIdList)
    machineName = stateMachineIdToNameDic[machineId]
    while not regionToStateNameDic[stateMachineToRegionDic[machineId]]:
        machineId = random.choice(statedMachineIdList)
        machineName = stateMachineIdToNameDic[machineId]
    stateName1 = random.choice(regionToStateNameDic[stateMachineToRegionDic[machineId]])
    stateName2 = random.choice(regionToStateNameDic[stateMachineToRegionDic[machineId]])
    if p > 0.03:
        return "TRANSITION_TRIGGER {} {} {}".format(machineName, stateName1, stateName2)
    elif p > 0.02:
        return "TRANSITION_TRIGGER {} {} {}".format('fuck', stateName1, stateName2)
    elif p > 0.01:
        return "TRANSITION_TRIGGER {} {} {}".format(machineName, 'fuck', stateName2)
    else:
        return "TRANSITION_TRIGGER {} {} {}".format(machineName, stateName1, 'fuck')


def PTCP_OBJ_COUNT():
    p = random.random()
    interactionName = random.choice(interactionNameList)
    if p > 0.01:
        return "PTCP_OBJ_COUNT {}".format(interactionName)
    else:
        return "PTCP_OBJ_COUNT {}".format('fuck')


def PTCP_CREATOR():
    p = random.random()
    interactionId = random.choice(interactionIdList)
    interactionName = random.choice(interactionIdToNameDic[interactionId])
    while not interactionToLifelineNameDic[interactionId]:
        interactionId = random.choice(interactionIdList)
        interactionName = random.choice(interactionIdToNameDic[interactionId])
    lifelineName = random.choice(interactionToLifelineNameDic[interactionId])
    if p > 0.02:
        return "PTCP_CREATOR {} {}".format(interactionName, lifelineName)
    elif p > 0.01:
        return "PTCP_CREATOR {} {}".format('fuck', lifelineName)
    else:
        return "PTCP_CREATOR {} {}".format(interactionName, 'fuck')


def PTCP_LOST_AND_FOUND():
    p = random.random()
    interactionId = random.choice(interactionIdList)
    interactionName = random.choice(interactionIdToNameDic[interactionId])
    while not interactionToLifelineNameDic[interactionId]:
        interactionId = random.choice(interactionIdList)
        interactionName = random.choice(interactionIdToNameDic[interactionId])
    lifelineName = random.choice(interactionToLifelineNameDic[interactionId])
    if p > 0.02:
        return "PTCP_LOST_AND_FOUND {} {}".format(interactionName, lifelineName)
    elif p > 0.01:
        return "PTCP_LOST_AND_FOUND {} {}".format('fuck', lifelineName)
    else:
        return "PTCP_LOST_AND_FOUND {} {}".format(interactionName, 'fuck')


InitClassAndInterface = [generUmlClass, generUmlInterface]
InitExtendAndRealize = [generUmlInterfaceRealization, generUmlGeneralizationOfClass, generUmlGeneralizationOfClass]

ClassfunctionList = [CLASS_IMPLEMENT_INTERFACE_LIST, CLASS_DEPTH_OF_INHERITANCE, CLASS_OPERATION_COUNT,
                     CLASS_SUBCLASS_COUNT,
                     CLASS_ATTR_COUPLING_DEGREE, CLASS_OPERATION_COUPLING_DEGREE, CLASS_OPERATION_VISIBILITY]
SequenceFuncList = [PTCP_CREATOR, PTCP_OBJ_COUNT, PTCP_LOST_AND_FOUND]
StateFuncList = [STATE_COUNT, STATE_IS_CRITICAL_POINT, TRANSITION_TRIGGER]


# functionList = [CLASS_OPERATION_COUPLING_DEGREE]
def generData():
    global operationIdList
    global classRealizeInterfaceDic
    global classNameList
    global classIdList
    global interfaceIdList
    global classHasSuperClassList
    global interfaceExtendDic
    global totalId
    global operationHasReturnParameterList
    global statedMachineIdList
    global stateMachineToRegionDic
    global statedMachineNameList
    global regionIdList
    global regionToStateDic
    global regionToStateNameDic
    global regionToStartStateDic
    global regionToFinalStateDic
    global transitionIdList
    global interactionIdList
    global interactionToLifelineIdDic
    global interactionNameList
    global interactionToLifelineNameDic
    global interactionToMessageDic
    global interactionToEndPointDic
    global stateMachineIdToNameDic
    global interactionIdToNameDic
    interactionIdToNameDic = collections.defaultdict(list)
    stateMachineIdToNameDic = {}
    interactionIdList = []
    interactionNameList = []
    interactionToLifelineIdDic = collections.defaultdict(list)
    interactionToLifelineNameDic = collections.defaultdict(list)
    interactionToMessageDic = collections.defaultdict(list)
    interactionToEndPointDic = collections.defaultdict(list)
    statedMachineNameList = []
    statedMachineIdList = []
    stateMachineToRegionDic = {}
    regionIdList = []
    regionToStateDic = collections.defaultdict(list)
    regionToStateNameDic = collections.defaultdict(list)
    regionToStartStateDic = {}
    regionToFinalStateDic = collections.defaultdict(list)
    transitionIdList = []
    operationIdList = []
    classNameList = []
    classIdList = []
    interfaceIdList = []
    classHasSuperClassList = []
    interfaceExtendDic = collections.defaultdict(list)
    classRealizeInterfaceDic = collections.defaultdict(list)
    operationHasReturnParameterList = []
    totalId = 0
    slist = []
    for i in range(5):
        s = ''
        s += generUmlClass()
        s += '\n'
        slist.append(s)
    for i in range(15):
        s = ''
        s += generUmlInterface()
        s += '\n'
        slist.append(s)
    for i in range(100):
        s = ''
        s += random.choice(InitExtendAndRealize)()
        s += '\n'
        slist.append(s)
    for i in range(300):
        s = ''
        s += generAttribute()
        s += '\n'
        slist.append(s)
    for i in range(100):
        s = ''
        s += generOperation()
        s += '\n'
        slist.append(s)
    for i in range(400):
        s = ''
        s += generParameter()
        s += '\n'
        slist.append(s)
    for i in range(20):
        s = ''
        s += generStateMachine()
        s += '\n'
        slist.append(s)
    for i in range(20):
        s = ''
        s += generRegion()
        s += '\n'
        slist.append(s)
    for i in range(100):
        s = ''
        s += generState()
        s += '\n'
        slist.append(s)
    for i in range(20):
        s = ''
        s += generFinalState()
        s += '\n'
        slist.append(s)
    for i in range(1000):
        s = ''
        s += generTransition()
        s += '\n'
        slist.append(s)
    for i in range(2000):
        s = ''
        s += generEvent()
        s += '\n'
        slist.append(s)
    for i in range(40):
        s = ''
        s += generInteraction()
        s += '\n'
        slist.append(s)
    for i in range(100):
        s = ''
        s += generLifeline()
        s += '\n'
        slist.append(s)
    for i in range(300):
        s = ''
        s += generEndPoint()
        s += '\n'
        slist.append(s)
    for i in range(2000):
        s = ''
        s += generMessage()
        s += '\n'
        slist.append(s)
    s = ''
    random.shuffle(slist)
    for ele in slist:
        s += ele
    s += "END_OF_MODEL\n"
    s += "CLASS_COUNT\n"
    for i in range(300):
        s += random.choice(ClassfunctionList)()
        s += '\n'
    for i in range(2000):
        s += random.choice(SequenceFuncList)()
        s += '\n'
    for i in range(2000):
        s += random.choice(StateFuncList)()
        s += '\n'
    """
    with open("1.txt", 'w', encoding='utf-8') as f:
        f.write(s)
    """
    return s


initFunc = [generUmlGeneralizationOfClass, generUmlGeneralizationOfInterface,
            generOperation, generParameter, generAttribute, generUmlInterfaceRealization]


def generData2():
    global operationIdList
    global classRealizeInterfaceDic
    global classNameList
    global classIdList
    global interfaceIdList
    global classHasSuperClassList
    global interfaceExtendDic
    global totalId
    global operationHasReturnParameterList
    operationIdList = []
    classNameList = []
    classIdList = []
    interfaceIdList = []
    classHasSuperClassList = []
    interfaceExtendDic = collections.defaultdict(list)
    classRealizeInterfaceDic = collections.defaultdict(list)
    operationHasReturnParameterList = []
    totalId = 0
    slist = []
    for i in range(5):
        s = ''
        s += generUmlClass()
        s += '\n'
        slist.append(s)
    for i in range(15):
        s = ''
        s += generUmlInterface()
        s += '\n'
        slist.append(s)
    for i in range(1000):
        s = ''
        s += generAttribute()
        s += '\n'
        slist.append(s)
    for i in range(400):
        s = ''
        s += generOperation()
        s += '\n'
        slist.append(s)
    for i in range(1000):
        s = ''
        s += generParameter()
        s += '\n'
        slist.append(s)
    for i in range(2000):
        s = ''
        s += random.choice(InitExtendAndRealize)()
        s += '\n'
        slist.append(s)
    s = ''
    for i in range(2000):
        s += random.choice(initFunc)()
        s += '\n'
    random.shuffle(slist)
    for ele in slist:
        s += ele
    s += "END_OF_MODEL\n"
    s += "CLASS_COUNT\n"
    for i in range(3000):
        s += random.choice(ClassfunctionList)()
        s += '\n'
    return s


def limitData():
    global operationIdList
    global classRealizeInterfaceDic
    global classNameList
    global classIdList
    global interfaceIdList
    global classHasSuperClassList
    global interfaceExtendDic
    global totalId
    global operationHasReturnParameterList
    operationIdList = []
    classNameList = []
    classIdList = []
    interfaceIdList = []
    classHasSuperClassList = []
    interfaceExtendDic = collections.defaultdict(list)
    classRealizeInterfaceDic = collections.defaultdict(list)
    operationHasReturnParameterList = []
    totalId = 0
    slist = []
    for i in range(1):
        s = ''
        s += generUmlClass()
        s += '\n'
        s += generUmlInterface()
        s += '\n'
        slist.append(s)
    for i in range(2):
        s = ''
        s += generOperation()
        s += '\n'
        slist.append(s)
    for i in range(400):
        s = ''
        s += generParameter()
        s += '\n'
        slist.append(s)
    s = ''
    random.shuffle(slist)
    for ele in slist:
        s += ele
    s += "END_OF_MODEL\n"
    for i in range(200):
        s += CLASS_OPERATION_COUPLING_DEGREE()
        s += '\n'
    return s

# generData()
# print(generData())
# print("\"_parent\":\"{}\"".format(1))
# with open("1.txt", 'w', encoding='utf-8') as f:
#    f.write(generData())
