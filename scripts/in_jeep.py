import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()

player = scene.objects["player"]


player.visible = False
player.worldPosition = [0,  0, -50]
player.suspendDynamics()
player.disableRigidBody()