''''
For quickly testing sequential SCBs on a lan to determine if they are all still functioning, and generate a list of any that are offline

'''


import os



SUBNET = "192.168.1."

IP_START = "1"
IP_END = "9"

IP_LIST = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}

ONLINE = "8.8.8.8"


def testPing(ip_list):
    for ip in ip_list:
        response = os.popen("ping " + SUBNET + f"{ip}").read()
        if "Received = 4" in response:
            print(f"UP" + SUBNET + f"{ip} Ping Successful, Host is UP!")
        else:
            print(f"DOWN"+ SUBNET + f"{ip} Ping Unsuccessful, Host is DOWN.")

def testOnline():
    response = os.popen(f"ping {ONLINE} ").read()
    if "Received = 4" in response:
        print(f"UP 8.8.8.8 Ping Successful, Host is UP!")
    else:
        print(f"DOWN 8.8.8.8 Ping Unsuccessful, Host is DOWN.")
