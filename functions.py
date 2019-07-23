import os


def OpenOrCreate(filename, mode):
    file = open(filename, mode)
    return file


def ShowContent():
    print("Enter the name of the file  :  ", end="")
    filename = input()

    try:
        file = OpenOrCreate(filename, "r")
        content = file.read()
        print("Content of file :" + content)
        file.close()
    except:
        print("No such file exists")


def Overwrite():
    print("Enter the name of the file  :  ", end="")
    filename = input()

    try:
        file = OpenOrCreate(filename, "w")
        print("Overwrite something  :  ", end="")
        temp = input()
        file.write(temp)
        file.close()
    except:
        print("No such file exists!!")


def Append():
    print("Enter the name of the file  :  ", end="")
    filename = input()
    
    try:
        file = OpenOrCreate(filename, "a")
        print("Append somethingg  :  ", end="")
        temp = input()
        file.write(temp)
        file.close()
    except:
        print("No such file exists!!")
    

def SearchString():
    print("Enter the name of the file  :  ", end="")
    filename = input()

    try:
        file = OpenOrCreate(filename, "r")
        print("Enter the string you want to search  :  ", end="")
        inputVal = input()
        readFile = file.read()
        print(inputVal + " occurs " + str(readFile.count(inputVal)) + " times in the file")
        file.close()
    except:
        print("No such file exists!!")


def ReplaceString():
    print("Enter the name of the file  :  ", end="")
    filename = input()
    print("Enter the string you want to replace  :  ", end="")
    old_string = input()
    print("Enter the new string  :  ", end="")
    new_string = input()

    try:
        fileRead = OpenOrCreate(filename, "r")
        readFile = fileRead.read()
        fileRead.close()
        readFile = readFile.replace(old_string, new_string)
        fileWrite = OpenOrCreate(filename, "w")
        fileWrite.write(readFile)
        fileWrite.close()
    except:
        print("No such file exists!!")


def DeleteFile():
    print("Enter the name of the file  :  ", end="")
    filename = input()

    try:
        os.remove(filename)
    except:
        print("No such file exists!!")
