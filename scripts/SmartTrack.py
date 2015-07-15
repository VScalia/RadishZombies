import GameLogic
from bge import logic

cont = logic.getCurrentController() 
scene = logic.getCurrentScene()
print(cont.sensors["Mount"].frameMessageCount)
if cont.sensors["Mount"].frameMessageCount > 0:
    print("pass")
    objectToTrack = scene.objects['bare']
else:
    objectToTrack = scene.objects['player']

track = cont.actuators[0]
track.target = objectToTrack
cont.activate(track)