from ftplib import FTP

METHOD = "7"

# some ftp details
IP = "localhost"
# IP = "127.0.0.1"
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
    encodedList7 = []
    for f in files:
        for i in range(10):
            if i < 3:
                if f[i] == "-":
                    pass
                else:
                    break
            else:
                if f[i] == "-":
                    encodedList7.append("0")
                else:
                    encodedList7.append("1")
            
    encodedString7 = "".join(encodedList7)
    chunks7 = []
    for i in range(0, len(encodedString7), 7):
        chunks7.append(encodedString7[i:i+7])
    decodedList7 = []
    for i in range(len(chunks7)):
        decodedList7.append(chr(int(chunks7[i], 2)))
    decodedString7 = "".join(decodedList7)
    print(decodedString7)

# decode the "/10" folder
if METHOD == "10":
    encodedList10 = []
    for f in files:
        for i in range(10):
            if f[i] == "-":
                encodedList10.append("0")
            else:
                encodedList10.append("1")
    while (len(encodedList10) % 7 != 0):
        encodedList10.append("0")

    encodedString10 = "".join(encodedList10)
    chunks10 = []
    for i in range(0, len(encodedString10), 7):
        chunks10.append(encodedString10[i:i+7])
    decodedList10 = []
    for i in range(len(chunks10)):
        decodedList10.append(chr(int(chunks10[i], 2)))
    decodedString10 = "".join(decodedList10)
    print(decodedString10)