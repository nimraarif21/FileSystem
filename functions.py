import os



def New_File(mode):
    file = open("test.txt", mode)
    return file


def Show_Content(file):
    content = file.read()
    print("Content of file :"+ content)

def Overwrite(file):
     print("Overwrite something  :  ", end="")
     temp = input()
     file.seek(0,0)
     file.write(temp)
     file.flush() 

def Append(file):
    print("Append somethingg  :  ", end="")
    temp = input()
    file.write(temp)
    file.flush()
    

def Search_String(file):
    print("Enter the string you want to search  :  ", end="")
    inputVal = input()
    readFile = file.read()
    print(inputVal + " occurs "+ str(readFile.count(inputVal))+" times in the file")

def Replace_String(file):
    print("Enter the string you want to replace  :  ", end="")
    oldS = input()
    print("Enter the new string  :  ", end="")
    newS = input()

    readFile = file.read()
    readFile.replace(oldS, newS)


def Delete_File(file):
    os.remove(file)
