#
# Each text object you want this script to change the resolution of needs to have "Text" in the name. Not a problem here because nothing is named. :)
# Only run once from the camera ("Camera.002") in the player file.
#

import bge
scene = bge.logic.getCurrentScene()

# Loops through all the objects, looking for "Text" in the name
for obj in scene.objects:
	if "Text" in obj.name:
		obj.resolution = 8.0