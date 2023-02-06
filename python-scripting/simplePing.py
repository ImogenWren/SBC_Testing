'''
Tesst if PING Will work on raspberry pi as problems experienced in last implementation

'''

#import os
import time
from gpiozero import LED
led = LED(12)


import platform   # Gets OS system name
import subprocess  ## For executing shell command

PING_IP = "192.168.1.113"


def control_led(state = 0):
    led.value = state

def flash_led(repeats = 1, delay = 200):
    for i in range(repeats):
        control_led(1)
        time.sleep(delay)
        control_led(0)
        time.sleep(delay)


def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    response = subprocess.call(command) == 0
    print(response)
    return response


def pingIP(ip_addr):
    print("Starting Ping Test")
    print(f"Scanning {PING_IP}")
    response = ping(PING_IP)
    if response == True:
        print("Host is Alive")
        control_led(1)
        return True
    else:
        print("No Host Detected")
        control_led(0)
        return False


def main():
    while 1:
        pingIP(PING_IP)
        #ping(PING_IP)
        time.sleep(5)


if __name__ == "__main__":
   main()
