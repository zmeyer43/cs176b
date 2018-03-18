import requests
import time
import os
import sys
import socket
from functions import *

#loop to act like command line
while(1):
    
    #read in decision from command line
    cmd = input('\ninput 0, 1, or 2 for downspeed, upspeed, or ping test (or q for quit)\n')
    
    #if decision is 0, test download speed
    if(cmd == '0'):
        tmp = downRate()
        print("downspeed(Mbps): ", tmp)
    
    #if decision is 1, test upload speed
    elif(cmd == '1'):
        uploop = input('input number of times to write the string:\n')
        tmp = upRate(uploop)
        print("upspeed(Mbps): ", tmp)
    
    #if decision is 2, test ping
    elif(cmd == '2'):
        pingplace = input('input pingplace: ')
        pingTest(pingplace)
    
    #if decision is q, quit the command line
    elif(cmd == 'q'):
        break
    
    #if decision is anything else, print error and ask for new input
    else:
        print('please enter a valid input next time')

