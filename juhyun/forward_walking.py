from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

cur_pos = mc.player.getTilePos()
x = cur_pos.x
y = cur_pos.y
z = cur_pos.z

for i in range(1001):
    mc.player.setTilePos(x,y, z-i)
    time.sleep(0.01)
