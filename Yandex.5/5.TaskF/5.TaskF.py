#Classes
classes = int(input())
minpower = list(map(int,input().split()))
classesdict = {i + 1: minpower[i] for i in range(classes)}

#Airconditioners
condtypes = int(input())
cost = [0]
powers = [0]
while len(cost) <= condtypes:
    maininput = input()
    powers.append(int(maininput.split()[0]))
    cost.append(int(maininput.split()[1]))


def setup():
    fullcost = 0
    for i in range(1,len(classesdict)+1):
        bestcost = float('inf')
        for j in range(1,len(powers)):
            if powers[j] >= classesdict[i] and cost[j] <= bestcost:
                bestcost = cost[j]
        if bestcost != float('inf'):
            fullcost += bestcost               
    if fullcost > 0:
        print(fullcost)
    else:
        print('impossible to find air conditioners')
setup()


