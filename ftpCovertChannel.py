# FTP (storage) covert channel
from ftplib import FTP

IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True # set this to False if the connection times out
DEBUG = False

def binDecode(inp):
  inp = input()
  if (len(inp) % 7 == 0):
      bitLength = 7
  elif (len(inp) % 8 == 0):
      bitLength = 8
  else:
      bitLength = 9

  #force bitlength if known value
  forcebitLength = False
  if (forcebitLength == True):
      bitLength = 7

  strBinOut = [inp[i:i+bitLength] for i in range(0, len(inp), bitLength)] # I found the idea for this line on stackoverflow
  binOut = [int(strBinOut[i], 2) for i in range(0, len(strBinOut))]
  output = ''.join(chr(binOut[i]) for i in range(0, len(binOut)))
  return output

  if DEBUG:
      print(f"Input: {inp}")
      print(f"Split binary output: {strBinOut}")
      print(f"Output: {output}")


# main
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

#exit the ftp server
ftp.quit()

#display the server contents
for f in files:
    print(f)
