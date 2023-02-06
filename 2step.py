import os

import pyvjoy
import atexit
import time
import keyboard

j = pyvjoy.VJoyDevice(1)
    
secondConstant = 9.562506285*1.4
firstConstant = 10.562506285*1.4

def twoStepOn():
    print("2step on")
    global ticker
    global toggle
    global twoStepRunning
    twoStepRunning = True
    while twoStepRunning:
        time.sleep(1 / 1_000_000_000 * 10)
        keyboard.press('home')

        time.sleep(1 / 1_000_000_000 * 10)

        keyboard.release('home')

def exit_handler():
    print('exit')

def handbrakeOn(a):
    print("handbrake true")
    j.set_button(1, 1)


def handbrakeOff(a):
    print("handbrake false")
    j.set_button(1, 0)

def leftOn(a):
    print("left true")
    j.set_button(4, 1) # olha pra frente
    j.set_button(5, 1) # olha pra esquerda


def leftOff(a):
    print("left false")
    j.set_button(4, 1)
    j.set_button(5, 0)
    time.sleep(0.01)
    j.set_button(4, 0)


def rightOn(a):
    print("right true")
    j.set_button(4, 1)
    j.set_button(6, 1)



def rightOff(a):
    print("right false")
    j.set_button(4, 1)
    j.set_button(6, 0)
    time.sleep(0.01)
    j.set_button(4, 0)

def twoStepOff(a):
    print("2step off")

keyboard.on_press_key(key='space', callback=handbrakeOn, suppress=True)
keyboard.on_release_key('space', handbrakeOff)

keyboard.on_press_key(key='j', callback=leftOn, suppress=True)
keyboard.on_release_key('j', leftOff)

keyboard.on_press_key(key='l', callback=rightOn, suppress=True)
keyboard.on_release_key('l', rightOff)

atexit.register(exit_handler)
while True:
    while keyboard.is_pressed('3'):
        print('2stepclutch')
        time.sleep(1 / firstConstant)
        keyboard.press('home')
        time.sleep(1 / secondConstant)
        keyboard.release('home')
    else:
        pass

    while keyboard.is_pressed('2'):


        keyboard.press('w')
        time.sleep(round((1 / 60), 2))
        keyboard.release('w')
        time.sleep(round((1 / 20), 2))
        print('2stepgas')
    else:
        pass
    continue
