import bge

cont = bge.logic.getCurrentController()
menu = cont.owner

cont.actuators["startGame"].scene = "level2" #Currently level2 is level1... not my or @Davids fault!
