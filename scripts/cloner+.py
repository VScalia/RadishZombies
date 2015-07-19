from bge import logic
import math
scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this 
owner = cont.owner                       # Get this object

zombieRoof = 100

skips = (owner["zombiecount"] - zombieRoof)/8

print(logic.skips)
print(skips)

if logic.skips <= 0:
	logic.skips = skips

	if owner["zombiecount"] < zombieRoof:
		newZombieClone = scene.addObject('zombieClone', owner)
		owner["zombiecount"] += 1
else:
	logic.skips = logic.skips - 1

