import GameLogic
from bge import logic

def Mount():
    logic.track = 'bare'
def Dismount():
    logic.track = 'player'