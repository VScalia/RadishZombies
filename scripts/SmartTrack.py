import GameLogic
from bge import logic

cont = logic.getCurrentController() 
scene = logic.getCurrentScene()
own = cont.owner
print(GameLogic.track)
objectToTrack = scene.objects[GameLogic.track]
track = cont.actuators[0]
track.target = objectToTrack
cont.activate(track)