''''
For quickly testing sequential SCBs on a lan to determine if they are all still functioning, and generate a log of offline hosts

'''


import platform
import subprocess
import time
#from gpiozero import LED, Button

from datetime import datetime




SUBNET = "192.168.1."

IP_START = 1
IP_END = 11

IP_LIST = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"}

ONLINE = "8.8.8.8"


LOOP = True


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

def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    response = subprocess.call(command) == 0
    print(response)
    return response


'''
States
Topology
- State Machine
- One of 3/4 states:
1. init, Checking for power - when power detected enter State 2: (Kept as a seperate state as we do not know what the power state will be in on init)
2. Power Detected - Start ping test & logging dead & alive Hosts
3. Power Lost - End ping test and go to state 4:
4. Waiting for change on power to reenter state 2

'''

def initState():
    f = open("testLog.log", "a")
    f.write(f"Starting New Test Log, Date: {returnDateTime()}")
    f.close()
'''
   // print("Checking Power State")
   // while power_state == 0:
    power_state = checkPower()
    print("Voltage Detected")
'''



def logState():
    power_state = True
    print("Starting Ping Test")
    print(f"Scanning range {SUBNET}{IP_START} to {SUBNET}{IP_END}")

    up_list = []
    down_list = []
    # for ip in ip_list:    # for some reason, this method scans in a random order, but maybe faster?
    for ip in range(IP_START, IP_END + 1):
        response = ping(f"{SUBNET}{ip}")
        print("-----------------------")
        if response == True:
            print(f"UP     {SUBNET}{ip}    Ping Successful, Host is ONLINE")
            up_list.append(f"{SUBNET}{ip}")
        else:
            print(f"DOWN  {SUBNET}{ip}    Ping Unsuccessful, Host is OFFLINE.")
            down_list.append(f"{SUBNET}{ip}")
        print("-----------------------\n")
        #time.sleep(1)
    print("\n\nPing Test Complete")
    print("\nThe following Hosts are ONLINE:")
    print(*up_list, sep='\n')
    print("\nThe following Hosts are OFFLINE:")
    print(*down_list, sep='\n')
    updateLog(up_list, down_list)
    if down_list:
        print("\nNot all Hosts Alive\n")
    else:
        print("\nALL HOSTS ALIVE\n")










def main():
    i = 0
    print(f"Starting Test, Date:  {returnDateTime()}")
    while True:
        print(f"\nLoop Iteration {i}")
        logState()
        i = i + 1
        print("Waiting")
        space_string = ""
        for i in range(10):
            time.sleep(1)                      
            print(f". {space_string} ", end="\r")
            space_string = space_string + ". "
        print(" Restarting Loop\n\n")



if __name__ == "__main__":
   main()

