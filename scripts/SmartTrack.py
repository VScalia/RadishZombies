import GameLogic
from bge import logic

cont = logic.getCurrentController() 
scene = logic.getCurrentScene()
if cont.sensors["Mount"].frameMessageCount > 0:
    objectToTrack = scene.objects['bare']
else:
    objectToTrack = scene.objects['player']

track = cont.actuators[0]
track.target = objectToTrack
cont.activate(track)