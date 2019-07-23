import functions

def run():
    input_value = 0
    print("=====Welcome to File System=====")

    while(True):
        print("""
1- Press 1 to show the file's contents.
2- Press 2 to append to file.
3- Press 3 to overwrite the file.
4- Press 4 to search for a string in file.
5- Press 5 to replace a word with other word.
6- Press 6 to delete the file.
7- Press 7 to Exit.""")

        print("\nEnter your input: ")
        input_value = int(input())

        if input_value == 1:
            functions.ShowContent()
        elif input_value == 2:
            functions.Append()
        elif input_value == 3:
            functions.Overwrite()
        elif input_value == 4:
            functions.SearchString()           
        elif input_value == 5:
            functions.ReplaceString()
        elif input_value == 6:
            functions.DeleteFile()
        else:
            break


if __name__ == "__main__":
    run()