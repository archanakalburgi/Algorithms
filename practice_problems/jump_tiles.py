"""
leetcode 55
"""

def jump_tiles(array):
    jumps=0
    if array[0] == 0 and len(array)>2:
        return False
    
    for tile in array:
        jumps = jumps+tile
    
    if jumps >= len(array) or jumps==0:
        return True
    return False

print(jump_tiles([0])) # true
print(jump_tiles([0,2,4])) # false
