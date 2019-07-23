import functions

def run():
    inputVal = 0
    file_write = functions.New_File("w+")
    file_append = functions.New_File("a")
    file_read = functions.New_File("r")
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
        inputVal = int(input())

        if inputVal == 1:
            functions.Show_Content(file_read)
        elif inputVal == 2:
            functions.Append(file_append)
        elif inputVal == 3:
            functions.Overwrite(file_write)
        elif inputVal == 4:
            functions.Search_String(file_read)           
        elif inputVal == 5:
            functions.Replace_String(file_read)
        # elif inputVal == 6:
        #     functions.Delete_File(f)
        else:
            break


if __name__ == "__main__":
    run()