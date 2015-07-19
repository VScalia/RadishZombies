import GameLogic
from bge import logic

cont = logic.getCurrentController() 
scene = logic.getCurrentScene()
own = cont.owner
objectToTrack = scene.objects[logic.track]
track = cont.actuators[0]
track.target = objectToTrack
cont.activate(track)