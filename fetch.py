from ftplib import FTP

METHOD = "7"

# some ftp details
# IP = "localhost"
IP = "127.0.0.1"
PORT = 21
USER = "anonymous"
PASSWORD = ""
if METHOD == "7":
    FOLDER = "/7"
elif METHOD == "10":
    FOLDER = "/10"
else:
    print("That method does not exist")
    exit()
USE_PASSIVE = True # set this to False if the connection times out
DEBUG = False

# main
if (DEBUG):
    print("Logging in...")
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

if (DEBUG):
    print("Logged in.")
    print("Navigating...")

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the ftp server
ftp.quit()

# decode the "/7" folder
if METHOD == "7":
    list7 = []
    for f in files:
        for i in range(10):
            if i < 3:
                if f[i] == "-":
                    pass
                else:
                    break
            else:
                if f[i] == "-":
                    list7.append("0")
                else:
                    list7.append("1")
            
    string7 = "".join(list7)
    chunks7 = []
    for i in range(0, len(string7), 7):
        chunks7.append(string7[i:i+7])
    list72 = []
    for i in range(len(chunks7)):
        list72.append(chr(int(chunks7[i], 2)))
    string72 = "".join(list72)
    print(string72)

# decode the "/10" folder
if METHOD == "10":
    list10 = []
    for f in files:
        for i in range(10):
            if f[i] == "-":
                list10.append("0")
            else:
                list10.append("1")
    while (len(list10) % 7 != 0):
        list10.append("0")

    string10 = "".join(list10)
    chunks10 = []
    for i in range(0, len(string10), 7):
        chunks10.append(string10[i:i+7])
    list102 = []
    for i in range(len(chunks10)):
        list102.append(chr(int(chunks10[i], 2)))
    string102 = "".join(list102)
    print(string102)