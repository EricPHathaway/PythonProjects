while True:
    file = input("What phrase would you like to check? ")
    fileList = file.split()
    newFile = ""
    for i in (fileList):
        i = int(i)
        newFile += chr(i)
    print(newFile)
