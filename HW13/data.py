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
classNameIsSameP = 0
attributeIsNormal = 0.4
attributeIsClass = 0.5
attributeTypeIsError = 0.3
attributeTypeIsParentClass = 0.8
parameterIsNoraml = 0.7
parameterIsError = 0


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
    return '''{{\"_parent\":\"{0}\",\"visibility\":\"{1}\",\"name\":\"{2}\",\"_type\":\"UMLClass\",\"_id\":\"{3}\"}}'''.format(
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
        return "CLASS_SUBCLASS_COUNT {}".format("fuck")


InitClassAndInterface = [generUmlClass, generUmlInterface]
InitExtendAndRealize = [generUmlInterfaceRealization, generUmlGeneralizationOfClass, generUmlGeneralizationOfClass]

functionList = [CLASS_IMPLEMENT_INTERFACE_LIST, CLASS_DEPTH_OF_INHERITANCE, CLASS_OPERATION_COUNT, CLASS_SUBCLASS_COUNT,
                CLASS_ATTR_COUPLING_DEGREE, CLASS_OPERATION_COUPLING_DEGREE, CLASS_OPERATION_VISIBILITY]


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
    s = ''
    random.shuffle(slist)
    for ele in slist:
        s += ele
    s += "END_OF_MODEL\n"
    s += "CLASS_COUNT\n"
    for i in range(1000):
        s += random.choice(functionList)()
        s += '\n'
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
    for i in range(1000):
        s = ''
        s += random.choice(InitExtendAndRealize)()
        s += '\n'
        slist.append(s)
    s = ''
    for i in range(1000):
        s += random.choice(initFunc)()
        s += '\n'
    random.shuffle(slist)
    for ele in slist:
        s += ele
    s += "END_OF_MODEL\n"
    s += "CLASS_COUNT\n"
    for i in range(3000):
        s += random.choice(functionList)()
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

# print("\"_parent\":\"{}\"".format(1))
# with open("1.txt", 'w', encoding='utf-8') as f:
#    f.write(generData())
