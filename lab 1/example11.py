# Pythin3 program to swap elements 
# at given positions

# swap function
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# driver function
list = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(list, pos1-1, pos2-1))