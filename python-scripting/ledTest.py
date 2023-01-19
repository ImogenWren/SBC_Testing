


'''
Really Simple Script to Light an LED to test other things are working
'''


from gpiozero import LED
import time


red_ch = LED(12)
green_ch = LED(16)
blue_ch = LED(20)



def control_led(state = 0):
    #red_ch.value = state
    red_ch.toggle()
    if red_ch.is_lit:
        print("Red Channel On")
    else:
        print("Red Channel is Off")
    time.sleep(30)
    try:
        countdown = 30
        while countdown:
            print("Countdown [",countdown,"]")
            countdown = countdown - 1
        #user = input("Enter Any Key to Exit")
    except:
        print("Program Exiting")



def main():
    control_led(1)


if __name__ == '__main__':
    main()
