#Michael Tang
#12/2/14
#Script to change child elements in folder to match the name of the parent directory
#Version 1.1
    #12/14/15
    #append name to the front only if the file is a .raw file
    #remove parenthese and substitute with dash
    #script will now alert when a non directory is found in the home directory instead of quitting
    #script will now alert when a new directory is found in a folder instead of quitting
    #support multiple period names
    #support multiple dash names

import os
import sys

startIndex = 0
def main():
    numFiles = numberOfFiles()
    isMac = False
    print("")
    print("You are currently in " + getCurrentDirectory())
    dsStore = input("Are you running OS X? (y)yes (n)no : ")
    if(dsStore == 'y'):
        startIndex = 1
        isMac = True
    elif(dsStore == 'n'):
        startIndex = 0
        isMac = False
    else:
        sys.exit("Script Aborted")
    print("")
    checkForBadFiles = input("Does the current directory contain only folders? (y)yes (n)no : ")
    if(checkForBadFiles == 'n'):
        sys.exit("Please remove everything but folders in the desired directory before continuing.")
    print("")
    lastConfirmation = input("Are you sure you want to change all the filenames? (y)yes (n)no : ")
    if(lastConfirmation == 'y'):
        listOfFiles = getFilesInDirectory()
        for i in range(startIndex,numFiles):
            token = str(listOfFiles[i])
            if(token != "pyScript.py" and token != "Compare.py"):
                #check isdir(token) so it doesn't quit
                if(os.path.isdir(token)):
                    changeDirectory(token)
                    changeName(startIndex,token)
                    returnToParent()
                else:
                    print("-A non folder found named "+token+" in "+getCurrentDirectory())
    else:
        sys.exit("Script Aborted")
        
    
    print("")
    print("Files successfully changed")

def getCurrentDirectory():
    currentLocation = os.getcwd()
    return currentLocation

def getFilesInDirectory():
    listOfFiles = os.listdir(getCurrentDirectory())
    return listOfFiles

def changeDirectory(index):
    os.chdir(index)

def returnToParent():
    os.chdir('..')

def changeName(startIndex,parentName):
    listOfFiles = getFilesInDirectory()
    for i in range(startIndex,numberOfFiles()):
        Test1 = False
        Test2 = False
        Test3 = False
        line = listOfFiles[i]
        #Test 0 directory test
        if((os.path.isdir(listOfFiles[i])) == False):
            rowName, fileType = os.path.splitext(str(line))
            
            #Test 1 .raw files
            if(fileType == ".raw"):
                line = rowName+fileType
                bool = checkForExistingRaw(line,parentName)
                rawString = rawFileManager(parentName,rowName)
                if(bool == False):
                    os.rename(listOfFiles[i],rawString)
                    Test1 = True
                else:
                    Test1 = True
       
            #Test 2 general test
            if((rowName != parentName) and (Test1 == False)):
                newLine = checkForDuplicates(parentName,fileType)
                os.rename(listOfFiles[i],newLine)
                Test2 = True
    
            #Test 3 multiple dashes
            if((Test1 == False) and (Test2 == False) and (rowName != parentName)):
                partialString = dashTest(rowName)
                newLine = checkForDuplicates(partialString,fileType)
                os.rename(listOfFiles[i],newLine)
                Test3 = True
                    
        else:
            print("-A non file found in folder "+parentName+" named "+str(line)+" in "+getCurrentDirectory())

def checkForExistingRaw(line,parentName):
    lengthOfParent = len(parentName)
    lengthOfLine = len(line)
    if(line[0:lengthOfParent] == parentName):
        return True
        #File exist
    else:
        return False

def checkForDuplicates(parentName,fileType):
    newLine = parentName + fileType
    line = getFilesInDirectory()
    if(getAnswer(newLine)):
        newLine = changeTail(parentName,fileType)
    else:
        return newLine
    return newLine

def rawFileManager(parentName,rowName):
    return parentName+"_"+rowName+".raw"

def dashTest(rowName):
    length = len(rowName)
    index = -1
    for i in range(0,length-1):
        if(rowName[i] == "-"):
            index = i
    if(index == -1):
        return rowName
    else:
        return rowName[0:index]

def changeTail(parentName,fileType):
    newLine = parentName+fileType
    count = 1
    while(getAnswer(newLine)):
        countstr = str(count)
        newLine = parentName+"-"+countstr+fileType
        count = count + 1
    return newLine

def getAnswer(newLine):
    line = getFilesInDirectory()
    i = 0
    for i in range(startIndex,numberOfFiles()):
        if(newLine == str(line[i])):
            return True
    if(i == numberOfFiles()-1):
        return False

def numberOfFiles():
    numOfFiles = len(os.listdir(getCurrentDirectory()))
    return numOfFiles

main()
