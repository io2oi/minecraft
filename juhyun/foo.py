import sys
import time
import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create() 

x0, y0, z0 = mc.player.getPos()
mc.player.setTilePos(x0, y0, z0)


a, b = (0, 10)
for ii in range(100):
    x, y, z = (random.randint(a, b), random.randint(a, b), random.randint(a, b))
    blocktype = random.randint(a,b)
    mc.player.setTilePos(x0+x, y0+y, z0+z)
    mc.setBlock(x0+x, y0+y-1, z0+z, blocktype)
    time.sleep(1)
