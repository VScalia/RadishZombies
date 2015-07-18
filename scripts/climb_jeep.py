import bge
import math

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()

player = scene.objects["player"]
jeep = scene.objects["bare"]

offsetFromJeep = [3.5,1]

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
    Rotation = jeep.worldOrientation.to_euler()
    print(Rotation)
    playerPos = [0,0,0]
    playerPos[0] = jeep.worldPosition[0] - math.cos(Rotation.z) * offsetFromJeep[0]
    playerPos[1] = jeep.worldPosition[1] + math.sin(Rotation.z) * offsetFromJeep[1]
    playerPos[2] = 0
    print(playerPos)
    player.worldPosition = playerPos
    player.worldOrientation =  Rotation
    player.restoreDynamics()
    player.enableRigidBody()