maininput = input()
numoftrees,numtypes = map(int,maininput.split())
types = [ i for i in range(1,numtypes+1)]

def newalley(data):
    data = [0] + data
    newalley = []
    alleylenght = float('inf')
    r = int()
    l = int()
    setik = set(types)
    for i in range(1,len(data)):
        newalley = [data[i]]
        for j in range(i+1,len(data)):
            newalley.append(data[j])
            if set(newalley) == setik and (j - i + 1) < alleylenght:
                alleylenght = len(newalley)
                l = i
                r = j
                break
            
    print(f'{l} {r}')
    
alley = list(map(int,input().split()))

if set(types) == set(alley):
    newalley(alley)
else:
    print('ERROR')

    
