import GameLogic
from bge import logic

scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this script
obj = cont.owner                         # Get this object

if not "Scattered" in obj:
    obj["Scattered"] = True
    locations = [
    [[-76.9175,5.2857,0],[0,0,0],'ZombieMaster'],
    [[-72.948,5.6023,0],[0,0,0],'ZombieMaster'],
    [[1,1,0],[0,0,0],'ZombieMaster'],
    [[-44.7737,-75.1513,0],[0,0,0],'ZombieMaster'],
    [[58.2994,50.9079,0],[0,0,0],'ZombieMaster'],
    [[29.8511,162.6793,0],[0,0,0],'ZombieMaster'],
    [[2,2,0],[0,0,0],'jerryCan'],
    [[-13.6,-55,0],[0,0,0],'syrynge'],
    [[-101.7,-34.1,0],[0,0,0],'syrynge'],
    [[-18.6,-52.6,0],[0,0,0],'ammoCrate'],
    [[-35,-8.6,0],[0,0,0],'ammoCrate'],
    [[-88.3,-52.4,0],[0,0,0],'ammoCrate']
    ]

    for location in locations:
        newZombie = scene.addObject(location[2], obj)
        newZombie.worldPosition = location[0]
        newZombie.worldOrientation = location[1]