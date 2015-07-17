from bge import logic

scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this 
owner = cont.owner                         # Get this object
if owner["zombiecount"] < 90:
	newZombieClone = scene.addObject('zombieClone', owner)
	owner["zombiecount"] += 1