import os

import pyvjoy
import atexit
import time
import keyboard

j = pyvjoy.VJoyDevice(1)
    
secondConstant = 9.562506285*1.4#9.562506285*1.2
firstConstant = 10.562506285*1.4#12.562506285*1.2

# default acceleration 02
# j.set_axis(pyvjoy.HID_USAGE_Z, 33000)

def twoStepOn():
    print("2step on")
    global ticker
    global toggle
    global twoStepRunning
    twoStepRunning = True
    # j.set_axis(pyvjoy.HID_USAGE_Z, 14000)
    while twoStepRunning:
        time.sleep(1 / 1_000_000_000 * 10)
        keyboard.press('home')
        # print('down')
        time.sleep(1 / 1_000_000_000 * 10)
        # time.sleep(1/12.665506285)
        # time.sleep(1/12.562506285)
        keyboard.release('home')
        # print('up')

        # ticker += 1
        #
        # if ticker == int(200_000):
        #     if toggle:
        #         print('down')
        #         keyboard.release('home')
        #         toggle = toggle != True
        #         ticker = 0
        #     else:
        #         keyboard.press('home')
        #         print('up')
        #         toggle = toggle != True
        #         ticker = 0

        # if ticker == int(200_000):
        #     if toggle:
        #         print('down')
        #         keyboard.release('home')
        #         toggle = toggle != True
        #     else:
        #         keyboard.press('home')
        #         print('up')
        #         toggle = toggle != True
        #
        # if ticker == int(250_000):
        #     if toggle:
        #         print('down')
        #         keyboard.release('home')
        #         toggle = toggle != True
        #         ticker = 0
        #     else:
        #         keyboard.press('home')
        #         print('up')
        #         ticker = 0
        #         toggle = toggle != True

        # if ticker == int(1_000_000):
        #     print('up')
        #     j.set_axis(pyvjoy.HID_USAGE_Z, 0)
        #     ticker = 0


    # 100 acceleration = 022
    # global twoStepRunning2
    # for i in range(10):
    #     print(i)
    #     j.set_axis(pyvjoy.HID_USAG2E_Z, 25000)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 23000)
    # if (twoStepRunning is False):
    #     twoStepRunning = True
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 25000)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 23000)
    #     time.sleep(0.5)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 25000)
    #     time.sleep(0.5)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 23000)
    #     time.sleep(0.5)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 25000)
    #     time.sleep(0.5)
    #     twoStepRunning = False

    #     time.sleep(0.2)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 20000)
    #     time.sleep(0.2)
    # time.sleep(2)
    # for i in range(10):
    #     print(i)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 5000)
    #     time.sleep(0.2)
    #     j.set_axis(pyvjoy.HID_USAGE_Z, 20000)
    #     time.sleep(0.2)


# def twoStepOff(a):
#     print("2step off")
#     # 0 acceleration = 20000
#     twoStepRunning = False
#     j.set_axis(pyvjoy.HID_USAGE_Z, 33000)
# twoStepOn()
def exit_handler():
    print('exit')
    # j.set_axis(pyvjoy.HID_USAGE_Z, 33000)

def handbrakeOn(a):
    print("handbrake true")
    j.set_button(1, 1)


def handbrakeOff(a):
    print("handbrake false")
    j.set_button(1, 0)

def leftOn(a):
    print("true")
    j.set_button(4, 1) # olha pra frnte
    j.set_button(5, 1) # olha pra esuqerda


def leftOff(a):
    print("false")
    j.set_button(4, 1)
    j.set_button(5, 0)
    time.sleep(0.01)
    j.set_button(4, 0)


def rightOn(a):
    print("true")
    j.set_button(4, 1)
    j.set_button(6, 1)



def rightOff(a):
    print("false")
    j.set_button(4, 1)
    j.set_button(6, 0)
    time.sleep(0.01)
    j.set_button(4, 0)

def twoStepOff(a):
    print("2step off")

keyboard.on_press_key(key='space', callback=handbrakeOn, suppress=True)
# keyboard.add_hotkey(hotkey='space', callback=handbrakeOn, suppress=True)
keyboard.on_release_key('space', handbrakeOff)

keyboard.on_press_key(key='j', callback=leftOn, suppress=True)
keyboard.on_release_key('j', leftOff)

keyboard.on_press_key(key='l', callback=rightOn, suppress=True)
keyboard.on_release_key('l', rightOff)

# keyboard.add_hotkey(hotkey='2', callback=twoStepOn2

atexit.register(exit_handler)
while True:

    # if keyboard.is_pressed("+"):
    #     print('+')
    #     firstConstant = 6.562506285 #18.562506285
    #     secondConstant = 18.562506285
    # if keyboard.is_pressed("-"):
    #     print('-')
    #     firstConstant = 12.562506285 #12.562506285
    #     secondConstant = 12.562506285
    # if keyboard.is_pressed("*"):
    #     print('*')
    #     firstConstant = 6.562506285  # 18.5625062853
    #     secondConstant = 18.562506285
        # firstConstant = 12.562506285  #15.562506285
        # secondConstant = 15.5625062852

    while keyboard.is_pressed('3'):
        print('2stepclutch')
        time.sleep(1 / firstConstant)
        #12
        keyboard.press('home')
        # print('down')
        time.sleep(1 / secondConstant)
        #50 ficou legal2

        # time.sleep(1/12.665506285)2
        # time.sleep(1/12.562506285)2
        keyboard.release('home')
    else:
        pass

    while keyboard.is_pressed('2'):


        keyboard.press('w')
        time.sleep(round((1 / 60), 2))
        # 12
        # print('down')


        keyboard.release('w')
        time.sleep(round((1 / 20), 2))
        print('2stepgas')

        # time.sleep(round((1/7), 2))
        # 50 ficou legal2
        # time.sleep(1/12.665506285)2
        # time.sleep(1/12.562506285)2
    else:
        pass
    continue
