# FTP (storage) covert channel
from ftplib import FTP

IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True # set this to False if the connection times out
DEBUG = False
METHOD = "7-bit" # Either "7-bit" or "10-bit"

def get_file_permissions(ftp):
    permissions = []
    ftp.retrlines('LIST', permissions.append) # found on GeeksForGeeks.org
    return permissions

def decrypt_permissions(permissions, method):
    covert_message = ""
    for line in permissions:
        # get 10 permission bits per file
        permission_bits = line[:10] 
        if method == "7-bit":
            # check to make sure first 3 permission bits are empty
            if permission_bits[:3] == "---":
                # use all 7 bits after the first 3 (base 2 -> string)
                covert_message += chr(int(permission_bits[3:], 2))
        elif method == "10-bit":
            # use all 10 bits
            covert_message += chr(int(permission_bits, 2))
    return covert_message


def main():
    # Connect to FTP server
    ftp = FTP()
    ftp.connect(IP, PORT)
    ftp.login(USER, PASSWORD)

    ftp.set_pasv(USE_PASSIVE)

    if (DEBUG):
        print("Logged in.")
        print("Navigating...")

    # Navigate to specified directory
    ftp.cwd(FOLDER)

    # Get file permissions
    if (DEBUG):
        print("Getting file permissions...")

    permissions = get_file_permissions(ftp)

    # Exit the ftp server
    ftp.quit()

    # Decrypt the message in the permissions
    if (DEBUG):
        print("Decrypting permissions...")
    covert_message = decrypt_permissions(permissions, METHOD)

    # Display the message
    print(covert_message)

if __name__ == '__main__':
    main()