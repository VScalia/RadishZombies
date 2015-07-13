from bge import logic

cont = logic.getCurrentController
scene = logic.getCurrentScene

em = scene.objects["Mirror Empty.001"]
pl = scene.objects["player"]

pl.worldPosition = em.worldPosition