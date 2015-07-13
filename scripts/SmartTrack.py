import GameLogic
from bge import logic

cont = logic.getCurrentController() 
scene = logic.getCurrentScene()

objectToTrack = scene.objects['bare.001']

track = cont.actuators[0]
track.target = objectToTrack
cont.activate(track)