import GameLogic
from bge import logic

scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this script
obj = cont.owner                         # Get this object

if not "Scattered" in obj:
    obj["Scattered"] = True
    locations = [
    [[-76.9175,5.2857,-0.6],[0,0,0],'ZombieMaster'],
    [[-72.948,5.6023,-0.6],[0,0,0],'ZombieMaster'],
    [[1,1,-0.6],[0,0,0],'ZombieMaster'],
    [[-44.7737,-75.1513,-0.6],[0,0,0],'ZombieMaster'],
    [[58.2994,50.9079,-0.6],[0,0,0],'ZombieMaster'],
    [[29.8511,162.6793,-0.6],[0,0,0],'ZombieMaster'],
    [[79.7546,-70.7662,-0.6],[0,0,0],'ZombieMaster'],
    [[-18.8812,-99.864807,-0.6],[0,0,0],'ZombieMaster'],
    [[-76.0846,-87.9987,-0.6],[0,0,0],'ZombieMaster'],
    [[-85.4402,-95.4832,-0.6],[0,0,0],'ZombieMaster'],
    [[118.7712,161.3121,-0.6],[0,0,0],'ZombieMaster'],
    [[126.5892,136.8092,-0.6],[0,0,0],'ZombieMaster'],
    [[124.5881,155.7543,-0.6],[0,0,0],'ZombieMaster'],
    [[77.5589,-42.5318,-0.6],[0,0,0],'ZombieMaster'],
    [[-6.8085,165.5291,-0.6],[0,0,0],'ZombieMaster'],
    [[-91,68.2365,-0.6],[0,0,0],'ZombieMaster'],
    [[92.7706,60.6761,-0.6],[0,0,0],'ZombieMaster'],
    [[-64.1551,-51.9408,-0.6],[0,0,0],'ZombieMaster'],
    [[2,2,0],[0,0,0],'jerryCan'],
    [[-39.7,-32.9,0],[0,0,0],'jerryCan'],
    [[132,148,-0.6],[0,0,0],'jerryCan'],
    [[-94.2,-1.4,0],[0,0,0],'jerryCan'],
    [[-13.6,-55,0],[0,0,0],'syrynge'],
    [[54.5,105.2,0],[0,0,0],'syrynge'],
    [[-101.7,-34.1,0],[0,0,0],'syrynge'],
    [[-18.6,-52.6,0],[0,0,0],'ammoCrate'],
    [[-35,-8.6,0],[0,0,0],'ammoCrate'],
    [[-62.6,140.375,0],[0,0,0],'ammoCrate'],
    [[-48.6,97.7,0],[0,0,0],'ammoCrate'],
    [[50.9393,114.1791,0],[0,0,0],'ammoCrate'],
    [[1.737,-15.6217,0],[0,0,0],'ammoCrate'],
    [[28.2387,-99.2614,0],[0,0,0],'ammoCrate'],
    [[54.0603,10.1999,0],[0,0,0],'ammoCrate'],
    [[-96.9,14.5881,0],[0,0,0],'ammoCrate'],
    [[98.8,61.405,0],[0,0,0],'ammoCrate'],
    [[33.7,-23.3835,0],[0,0,0],'ammoCrate'],
    [[70.5053,-91.0459,0],[0,0,0],'ammoCrate'],
    [[28.7479,156.4052,0],[0,0,0],'ammoCrate'],
    [[55.0396,121.2207,0],[0,0,0],'ammoCrate'],
    [[5,5,0],[0,0,0],'MP_Main'],
    [[5,10,0],[0,0,0],'MP_Main']
    ]

    for location in locations:
        newItem = scene.addObject(location[2], obj)
        newItem.worldPosition = location[0]
        newItem.worldOrientation = location[1]
        print(newItem.childrenRecursive)
        for newItemChild  in newItem.childrenRecursive:
            newItemChild.worldPosition = location[0]
            newItemChild.worldOrientation = location[1]