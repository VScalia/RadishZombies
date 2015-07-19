from bge import logic
import math
scene = logic.getCurrentScene()        # Get the current game scene
cont = logic.getCurrentController() # Get the controller executing this 
owner = cont.owner                       # Get this object

zombieRoof = 300

newZombieCount = owner["zombiecount"] * 1.1
newZombieCount = int(newZombieCount + 1)
addZombieCount = newZombieCount - (owner["zombiecount"])
if newZombieCount >= zombieRoof:
	addZombieCount = addZombieCount - (newZombieCount - zombieRoof)

print(newZombieCount)
# print(addZombieCount)
for x in range(0,addZombieCount):
	newZombieClone = scene.addObject('zombieClone', owner)
	owner["zombiecount"] += 1

#GiantCowFilms