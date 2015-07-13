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
    ]

    for location in locations:
        scene.addObject('ZombieMaster', obj).worldPosition = location[0]