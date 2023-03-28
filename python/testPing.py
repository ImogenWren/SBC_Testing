''''
For quickly testing sequential SCBs on a lan to determine if they are all still functioning, and generate a list of any that are offline

'''


import os



SUBNET = "192.168.1."

IP_START = 1
IP_END = 11

IP_LIST = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"}

ONLINE = "8.8.8.8"

LOOP = True




def testPing(ip_list):
    print("Starting Ping Test - Please wait for Completion")
    print(f"Scanning range {SUBNET}{IP_START} to {SUBNET}{IP_END}")
    up_list = []
    down_list = []
    #for ip in ip_list:    # for some reason, this method scans in a random order, but maybe faster?
    for ip in range(IP_START, IP_END+1):
        response = os.popen("ping " + SUBNET + f"{ip}").read()
        if "Received = 4" in response:
            print(f"UP    " + SUBNET + f"{ip}    Ping Successful, Host is ONLINE")
            up_list.append(SUBNET + f"{ip}")
        else:
            print(f"DOWN  "+ SUBNET + f"{ip}    Ping Unsuccessful, Host is OFFLINE.")
            down_list.append(SUBNET + f"{ip}")
    print("\n\nPing Test Complete")
    print("\nThe following Hosts are ONLINE:")
    #up_list.sort()  # Not needed now program operates sequentially
    #down_list.sort()
    print(*up_list, sep='\n')
    print("\nThe following Hosts are OFFLINE:")
    print(*down_list, sep='\n')
    if down_list:
        print("Not all Hosts Alive")
    else:
        print("ALL HOSTS ALIVE")
    if up_list:
        return True
    else:
        return False

def testOnline():
    response = os.popen(f"ping {ONLINE} ").read()
    if "Received = 4" in response:
        print(f"UP 8.8.8.8 Ping Successful, Host is UP!")
    else:
        print(f"DOWN 8.8.8.8 Ping Unsuccessful, Host is DOWN.")



def main():
    i = 0
    while testPing(IP_LIST):
        print(f"\nIteration {i}")
        i = i + 1
        print("Restarting\n\n")
    print("No Active Hosts, Ending loop")
   # except:
      #  print("User Ended Process")



if __name__ == "__main__":
   main()

