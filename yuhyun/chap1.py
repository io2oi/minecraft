import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ori_pos = (91.303546666,10.0,30.0963656926)

# for i in range(100):
#     mc.player.setTilePos(i,0,0)
#     time.sleep(1)

x = 0
y=0
z = 0
for i in range(0,-1000000000000,10000):
    y = y + i/1000000
    mc.player.setPos(x,y,0)
    print(mc.player.getPos())