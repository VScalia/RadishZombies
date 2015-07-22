#
# Add a game property of "text" to each text object you want this script to change the resolution.
# Only run once from the camera ("Camera.002") in the player file.
#

import bge
scene = bge.logic.getCurrentScene()

# Loops through all the objects, loking for the property "text"
for obj in scene.objects:
	if "text" in obj:
		obj.resolution = 8.0