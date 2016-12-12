#Basic FTP client

import ftplib
up = None

def changeDir():
    global s
    directory = input("Change Directory: ")
    print()
    return("-" + s.cwd(directory))

def createDir():
    global s
    directory = input("Create Folder: ")
    print()
    return("-" + s.mkd(directory))

def delDir():
    global s
    directory = input("Delete Folder: ")
    print()
    return("-" + s.rmd(directory))
    
def delFile():
    global s
    file = input("Delete File: ")
    print()
    return("-" + s.delete(file))

def getFile():
    global s
    file = input("Download File: ")
    print()
    down = open(file, "wb")
    try:
        print("Downloading " + file + "...")
        return("-" + s.retrbinary("RETR " + file, down.write))
    except:
        return("Error")
    

def uploadFile():
    global s,up
    file = input("Upload File: ")
    print()
    up = open(file, "rb")
    try:
        print("Uploading " + file + "...")
        return("-" + s.storbinary("STOR " + file,up))
    except:
        return("Error")

def printDir():
    global s
    print()
    print(s.pwd() + ":")
    print(s.dir())
    print()
    
s = ftplib.FTP()

ip = input("IP Address: ")
port = int(input("Port: "))
print()

print("-" + s.connect(ip,port))
print()

login = input("Login: ")
password = input("Password: ")
print()

print("-" + s.login(login,password))
print()
print(s.pwd() + ":")
print(s.dir())
print()

while True:
    print("1. Change directory")
    print("2. Create folder")
    print("3. Delete folder")
    print("4. Delete file")
    print("5. Download file")
    print("6. Upload file")
    print("7. Close connection")
    print()
    option = input("Option: ")
    print()
    if option == "1":
        print(changeDir())
        printDir()
        
    elif option == "2":
        print(createDir())
        printDir()
        
    elif option == "3":
        print(delDir())
        printDir()

    elif option == "4":
        print(delFile())
        printDir()
        
    elif option == "5":
        print(getFile())
        printDir()
        
    elif option == "6":
        print(uploadFile())
        up.close()
        printDir()
        
    elif option == "7":
        print("Closing connection...")
        print("-" + s.quit())
        print()
        break
