#-*- coding:utf-8 -*-

import os

def listReplaceStr(strList, fromStr, toStr):
    '''
    整体替换列表中的某个字符串
    '''
    returnList = []
    for str_i in strList:
        returnList.append(str_i.replace(fromStr, toStr))

    return returnList

def getFilePath(fileFullName):
    '''
    获取带后缀名的文件的路径
    '''
    #根据是否包含了后缀名来进行不同的处理，不包含后缀名则直接返回
    if "." in fileFullName:
        fileUnits = []

        #如果不存在正斜杠，用反斜杠进行分割
        if "/" not in fileFullName:
            fileUnits = fileFullName.split("\\")
        else:
            fileUnits = fileFullName.split("/")

        #如果是分出了多个，说明是多层目录
        if len(fileUnits) >= 1:
            return fileFullName.replace(fileUnits[len(fileUnits) - 1], "")
        else:
            return fileFullName
    else:
        return fileFullName

def getFileLines(fileFullPath):
    '''
    按行读取文件内容并且保存到列表之中
    '''
    inf = open(fileFullPath, "r")

    lines = []

    for line in inf:
        lines.append(line.replace("\n", ""))

    inf.close()

    return lines
    
if __name__ == "__main__":
    #各种文件来源路径
    fromFileTypePathMap = { \
        ".java" : "D:/", \
        ".jsp" : "D:/" \
    }

    #各种文件复制到的路径
    toFileTypePathMap = { \
        ".class" : "D:/", \
        ".jsp" : "D:/" \
    }

    #各种文件对应的编译后的文件
    fileCompileTypeMap = { \
        "java" : "java", \
        "jsp" : "jsp"
    }

    #print fileTypePathMap
    
    for inl in getFileLines("F:\\ProgramData\\IDEA\\GenDBOperate\\src\\main\\GenDBOperate.java"):
        print inl
    
    
