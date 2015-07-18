import bge

def inJeep():
    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()

    player = scene.objects["player"]


    player.visible = False
    #Temporary fix to return the player to previous location.
    bge.logic.returnPos = player.worldPosition
    player.worldPosition = [0,  0, -50]
    player.suspendDynamics()
    player.disableRigidBody()
def outJeep():
    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()

    player = scene.objects["player"]


    player.visible = True
    #Temporary fix to return the player to previous location.
    player.worldPosition = bge.logic.returnPos 
    player.restoreDynamics()
    player.enableRigidBody()