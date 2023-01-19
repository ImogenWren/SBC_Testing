




def testOnline():
    response = os.popen(f"ping {ONLINE} ").read()
    if "Received = 4" in response:
        print(f"UP 8.8.8.8 Ping Successful, Host is UP!")
    else:
        print(f"DOWN 8.8.8.8 Ping Unsuccessful, Host is DOWN.")