import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()


def init():
	bge.logic.track = 'player'
	bge.logic.skips = 0
	bge.logic.zombieCount = 1


def menu_web_link():
	cont = bge.logic.getCurrentController()
	if cont.sensors['MouseOver'].hitObject == cont.owner and cont.sensors['Mouse'].getButtonStatus(bge.events.LEFTMOUSE) == bge.logic.KX_INPUT_JUST_ACTIVATED:
		import webbrowser
		webbrowser.open("https://github.com/VScalia/RadishZombies",0,True)


def text_resolution():
	# Each text object you want this script to change the resolution of needs to have "Text" in the name. Not a problem here because nothing is named. :)
	# Only run once from the camera ("Camera.002") in the player file.

	# Loops through all the objects, looking for "Text" in the name
	for obj in scene.objects:
		if "Text" in obj.name:
			obj.resolution = 8.0


def Mount():
	bge.logic.track = 'bare'


def Dismount():
	bge.logic.track = 'player'


def inJeep():
	player = scene.objects["player"]
	player.visible = False
	#Temporary fix to return the player to previous location.
	bge.logic.returnPos = player.worldPosition.copy()
	player.worldPosition = [0,  0, -50]
	player.suspendDynamics()
	player.disableRigidBody()
	print("player called from state 2 ,in jeep")


def outJeep():
	player = scene.objects["player"]
	jeep = scene.objects["bare"]
	player.visible = True
	player.worldOrientation[2] =  jeep.worldOrientation[2]
	jp = jeep.localPosition
	player.localPosition = [jp[0] - 3.0, jp[1], jp[2]]
	player.restoreDynamics()


def cloner():
	scene = bge.logic.getCurrentScene()        # Get the current game scene
	cont = bge.logic.getCurrentController() # Get the controller executing this 
	owner = bge.cont.owner                       # Get this object

	zombieRoof = 150

	skips = int((50 - bge.logic.zombieCount)/12)

	print(bge.logic.skips)
	print(skips)

	if bge.logic.skips <= 0:
		bge.logic.skips = skips

		if bge.logic.zombieCount < zombieRoof:
			newZombieClone = scene.addObject('zombieClone', owner)
			bge.logic.zombieCount += 1
else:
	bge.logic.skips = bge.logic.skips - 1
    

def track():
	cont = bge.logic.getCurrentController()
	objectToTrack = scene.objects[bge.logic.track]
	track = cont.actuators[0]
	track.target = objectToTrack
	cont.activate(track)
def killZombie():
    bge.logic.zombieCount -= 1
    