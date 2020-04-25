import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def e(ii, a, b):
    # a = 0
    # b = 10
    x = random.randint(a, b) + 30
    y = random.randint(a, b)
    z = random.randint(a, b) + 30
    blocktype = random.randint(0, 100)
    mc.player.setTilePos(x, y, z)
    mc.setBlock(x, y, z,blocktype)
    mc.postToChat(
        f"I'm at ({x}, {y}, {z}) (iter:{ii}, block: {blocktype})")



for ii in range(1000):
    e(ii, 0, 10)


