import bge
import math

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()

player = scene.objects["player"]
jeep = scene.objects["bare"]

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
    
    player.worldOrientation =  jeep.worldOrientation
    
    jp = jeep.localPosition
    
    player.localPosition = [jp[0] - 3.0, jp[1], jp[2]]
    
    player.restoreDynamics()
