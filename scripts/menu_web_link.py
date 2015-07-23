import bge
cont = bge.logic.getCurrentController()

if cont.sensors['MouseOver'].hitObject == cont.owner and cont.sensors['Mouse'].getButtonStatus(bge.events.LEFTMOUSE) == bge.logic.KX_INPUT_JUST_ACTIVATED:
	import webbrowser
	webbrowser.open("https://github.com/VScalia/RadishZombies",0,True)