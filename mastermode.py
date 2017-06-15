import pyautogui, time

mc = pyautogui

mc.PAUSE = 0

mc.FAILSAFE = True
    
width = 1920

height = 1080

returner = 0

def world():
#    print(mc.locateOnScreen("world.png"))
    world = mc.locateOnScreen("world.png") #Is located at: (817, 688, 250, 223)
    world_int = mc.center(world)
    mc.click(world_int)


def returner():
#    print(mc.locateOnScreen("return.png"))
    returner = mc.locateOnScreen("return.png") #Is located at: (1882, 951, 38, 36)
    returner_int = mc.center(returner)
    mc.click(returner_int)

def unit():
    unit = mc.locateOnScreen("units.png")
    returner = mc.locateOnScreen("return.png") #Is located at: (1882, 951, 38, 36)
    returner_int = mc.center(returner)
    mc.click(returner_int)#click at (1901, 969)
    
def unit1():        
    unit = mc.locateOnScreen("units.png")
    returner = mc.locateOnScreen("return.png") #Is located at: (1882, 951, 38, 36)
    returner_int = mc.center(returner)
    mc.click((1901, 969))#click at (1901, 969)
    
    
def fullunit():
    world()
    unit()
