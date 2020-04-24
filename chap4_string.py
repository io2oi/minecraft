import sys
import time
import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create() 

x0, y0, z0 = mc.player.getTilePos()
mc.player.setTilePos(x0, y0, z0)


a, b = (0, 80)
ya, yb = (0, 10)
block_types = [51, 10]
for ii in range(1000):
    x, y, z = (
        random.randint(a, b),
        random.randint(ya, yb),
        random.randint(a, b))
    blocktype = random.choice(block_types)
    mc.player.setTilePos(x0+x, y0+y, z0+z)
    mc.setBlock(x0+x, y0+y-1, z0+z, blocktype)
    mc.postToChat(
        f"iter: {ii}, x:{x0+x}, y:{y0+y}, z:{z0+z}, block:{blocktype}")
    time.sleep(0.1)
