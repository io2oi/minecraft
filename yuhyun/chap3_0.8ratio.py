from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = (10, 4, 47) #mc.player.getTilePos()
width = 10
block_type = 41 
mc.setBlocks(x, y, z, x+width, y, z+width, block_type)
mc.setBlocks(
    x +1/10*width, y+1, z+1/10*width,
    x+9/10*width, y+1, z+9/10*width, 
    block_type)
mc.setBlocks(
    x +2/10*width, y+2, z+2/10*width,
    x+8/10*width, y+2, z+8/10*width, 
    block_type)
mc.setBlocks(
    x +3/10*width, y+3, z+3/10*width,
    x+7/10*width, y+3, z+7/10*width, 
    block_type)