#!/usr/bin/env python3

''''
Writes generic data to a file, constantly checking the size untill greater than Q
Deletes the file
loops

To call this on boot up:
Copy dataDump.py to home directory
sudo chmod +x dataDump.py
crontab -e -> @reboot sudo python3 dataDump.py
mkdir data_dump
nano genData.txt # maybe Not Nessissary
sudo chmod 777 genData.txt # Might not be nessissary
sudo reboot
after reboot
cat genData.txt to see if data is being written to file
on odroid08 crontab = @reboot sudo sh /home/odroid/runDataDump.sh
'''

import os
import platform
import subprocess
import time
import shutil


from datetime import datetime


FILENAME = "genData.txt"
FILEPATH = "/home/odroid/"

COPYPATH = "/home/odroid/data_dump/"

STRINGDATA = " All Work and No Play Make Jack a Dull Boy "

MAX_FILESIZE_MB = 3000

SLEEP_TIME = 0





'''
Tools
'''
def returnDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)
    return dt_string

# Dumps data into a file
def dumpData(filename, filepath, data):
    f = open(f"{filepath}{filename}", "a")
    f.write(returnDateTime())
    f.write(data)
    f.close()



# Checks the Size of the File and returns true if > passed value
def checkFileSize(filename, filepath, max_filesize_MB):
    size_byte = os.stat(f"{filepath}{filename}").st_size
    print(f"File Size: {size_byte} bytes")
    size_MB = size_byte / 1048576
    print(f"File Size: {size_MB} MB")
    size_GB = size_byte / 1073741824
    print(f"File Size: {size_GB} GB")
    # time.sleep(1)  # Used for testing
    if size_MB > max_filesize_MB:
        print(f"\n\nFile Size > {max_filesize_MB} MB. Now Deleting!\n\n")
        return True
    else:
        return False




def deleteData(filename, filepath):
    if os.path.exists(f"{filepath}{filename}"):
        print(f"Deleting File: {filepath}{filename}")
        os.remove(f"{filepath}{filename}")
    else:
        print("The file does not exist")


def updateLog(up_list, down_list):
    print("\n\nUpdating Log")
    deliminator = "\n"
    up_string = deliminator.join(up_list)
    down_string = deliminator.join(down_list)
    f = open("testLog.log", "a")
    f.write(f"\n\nNew Log:\n Date: {returnDateTime()}:")
    f.write("\nHosts ALIVE:\n")
    f.write(up_string)
    f.write("\nHosts DOWN:\n")
    f.write(down_string)
    f.write("\n------\n")
    f.close()





def copy_file():
    shutil.copy(FILEPATH + FILENAME, COPYPATH + FILENAME)








def main():
    i = 0
    print("Starting Data Dump")
    while True:
        print(f"\n Loop Iteration: {i}")
        i = i + 1
        dumpData(FILENAME, FILEPATH, STRINGDATA)
        if (checkFileSize(FILENAME, FILEPATH, MAX_FILESIZE_MB)):
            copy_file()
            deleteData(FILENAME, FILEPATH)
            deleteData(COPYPATH, FILENAME)
            time.sleep(SLEEP_TIME) # // Just for testing





if __name__ == "__main__":
   main()

