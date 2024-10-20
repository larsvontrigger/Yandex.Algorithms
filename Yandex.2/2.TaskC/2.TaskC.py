import math
number = int(input())
list = list(map(int,input()))
goal = int(input())
#Function that find closest number
def closestnum(list):
    closest = list[0] - goal
    for item in list:
        dif = item - goal
        #abs of difference between our numbers
        if abs(dif) <= abs(closest):
            closest = dif
            ournum = item
    print(ournum)


if len(list) != number:
    print('You are wrong, buddy')
else:
    closestnum(list)