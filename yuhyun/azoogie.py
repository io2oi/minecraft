from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = (63,7,46)
mc.setBlocks(x,y,z,x+6,7,z+6,2)

mc.setBlocks(x+1,y+1,z+1,x+5,y+1,z+5,2)
mc.setBlocks(x+2,y+2,z+2,x+4,y+2,z+4,2)

높이 = mc.getHeight(x, z)
mc.setBlock(x, 높이, z, 6)

높이 = mc.getHeight(x+1,z)
mc.setBlock(x+1, 높이, z, 6)
