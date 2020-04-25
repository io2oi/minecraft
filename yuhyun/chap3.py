from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.getPos()

# x = 0
# y = 0
# z = 0
# mc.player.setPos(x,y,z)

# for i in range(100):
#     mc.setBlock(x+i,y+i,z,103)

# oripos=mc.player.getPos()


# mc.setBlock(oripos.x, oripos.y, oripos.


# oripos = mc.player.getPos()
# x = oripos.x
# y = oripos.y
# z = oripos.z

x = 60
y = -4
z = 14
mc.setBlocks(x,y,z,x+10,y+10,z+10, 57)
mc.setBlocks(x+1,y,z+1,x+9,y+9,z+9, 0)

# 계단 쌓기 부분
curpos = mc.player.getTilePos()

x = curpos.x+1
y = curpos.y
z = curpos.z

blocktype = 0
for ii in range(10):
    mc.setBlock(x, y, z, blocktype)
    x = x + 1
    y = y + 1
    z = z


# 평면에 원하는 블록 1층 쌓기
mc.player.getTilePos()
a=mc.player.getTilePos()
mc.setBlocks(a.x+1,a.y,a.z+1,a.x+100,a.y,a.z+100,0)


# 첨탑쌓기
curpos = mc.player.getTilePos()
a = 100 # 너비

x = curpos.x+1
y = curpos.y
z = curpos.z+1
mc.setBlocks(x,y,z,x+a,y,z+a,41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)

x = x + 1/4*a
y = y+1
z = z + 1/4*a
a = 1/2*a
mc.setBlocks(x,y, z, x+a, y, z+a, 41)
