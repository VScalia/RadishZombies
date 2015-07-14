import GameLogic
from bge import logic

scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this script
obj = cont.owner                         # Get this object

if not "Scattered" in obj:
    obj["Scattered"] = True
    locations = [
    [[-76.9175,5.2857,0],[0,0,0]],
    [[-72.948,5.6023,0],[0,0,0]],
    [[1,1,0],[0,0,0]],
    [[-44.7737,-75.1513,0],[0,0,0]],
    [[58.2994,50.9079,0],[0,0,0]],
    [[29.8511,162.6793,0],[0,0,0]],
    ]

    for location in locations:
        newZombie = scene.addObject('ZombieMaster', obj)
        newZombie.worldPosition = location[0]
        newZombie.worldOrientation = location[1]