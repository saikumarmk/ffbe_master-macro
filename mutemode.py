########################################################################################
#Property of Theorvolt. Don't skid >:(                                                 #
#Alternative mode that uses coordinates instead of detection.                          #
########################################################################################

import pyautogui, time, os, os.path, shutil, psutil

d = os.getcwd()

os.chdir("..")

o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] # Gets all directories in the folder as a tuple

l = 'C:\\Users\\Sai2\\Documents\\Coding\\ffbe-macro\\Buttons'

mc = pyautogui

mc.PAUSE = 0

mc.FAILSAFE = True
    
########################################################################################
#Starts defining different button clicks.                                              #
########################################################################################

def world():
    print(mc.locateOnScreen(l+"\\world.png"))
    world = mc.locateOnScreen(l+"\\world.png") #Is located at: (817, 688, 250, 223)
    world_int = mc.center(world)
    print(world_int)
    mc.click(945, 811)
    

def unit():
    unit = mc.locateOnScreen(l+"\\units.png")
    returner = mc.locateOnScreen(l+"\\return.png") #Is located at: (1882, 951, 38, 36)
    returner_int = mc.center(returner)
    mc.click(returner_int)#click at (1901, 969)

def nox_back():
    mc.click((1901,969))

def nox_home():
    mc.click(1903, 1007)

def end_session():
    #Detects run out of NRG. TODO
    print("undone")

def do_es():
    no = input("One run or infinite?")
    if no == "one":
        print("undone")
        #yadayada does a loop and once end session is detected, terminates.
    if no == "infinite":
        print("undone")
        #Does the same thing but once at 1 nrg, waits 5 minutes before doing.
        
########################################################################################
#Begins the bot.                                                                       #
########################################################################################

while True:
    userinput = input("What would you like to do today? \n If you don't know what to do, query with Help.  ")

    if userinput == "Help":
        print("")
        print("Available Commands:\n Help - Asks for available commands. \n es - Runs Earth Shrine.\n Abort - Breaks out of the loop.")
        print("")
        time.sleep(1)
    if userinput == "Abort":
        break
    if userinput == "es":
        do_es()
        


