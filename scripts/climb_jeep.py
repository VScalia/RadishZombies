import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()

player = scene.objects["player"]

def inJeep():
    player.visible = False
    #Temporary fix to return the player to previous location.
    bge.logic.returnPos = player.worldPosition.copy()
    player.worldPosition = [0,  0, -50]
    player.suspendDynamics()
    player.disableRigidBody()
    print("player called from state 2 ,in jeep")


def outJeep():
    player.visible = True
    #Temporary fix to return the player to previous location.
    player.worldPosition = bge.logic.returnPos 
    player.restoreDynamics()
    player.enableRigidBody()