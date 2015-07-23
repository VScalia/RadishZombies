import bge

cont = bge.logic.getCurrentController()
menu = cont.owner

print("Play")

nextLevel = cont.actuators["startGame"]
nextLevel.scene = "level2" #Currently level2 is level1... not my or @Davids fault!
cont.activate(nextLevel)
