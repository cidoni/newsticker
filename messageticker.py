# THIS SCRIPT USES THE LIBRARY AT:
# https://github.com/hzeller/rpi-rgb-led-matrix

import os, time, threading, random
from random import shuffle
import argparse

def colorRandom():
    return str(random.randint(0,255)) + "," + str(random.randint(0,255))  + "," + str(random.randint(0,255))

def getIoTMessage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", action="store", required=True, dest="iotmessage", help="Your incoming AWS IoT message")
    args = parser.parse_args()
    return args.iotmessage

def showOnLEDDisplay(dispmsg):
    os.system("sudo /home/pi/risrim/display16x32/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-rows=16 --led-cols=32 -f /home/pi/risrim/display16x32/rpi-rgb-led-matrix/fonts/7x14.bdf -s 10 -C "+ colorRandom() +" -b 50 -l 10 "+dispmsg)

def run():
    showOnLEDDisplay(getIoTMessage())

if __name__ == '__main__':
    run()
