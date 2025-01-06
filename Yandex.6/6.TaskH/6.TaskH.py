n,k = map(int,input().split())
wires = []

for _ in range(0,n):
    wires.append(int(input()))
summ = sum(wires)

def wirewirewire(k,summ,wires):
    left = 1
    right = summ//k
    
    if min(wires) < k:
        return 0
    
    while left <= right:
        mid = (left + right)//2
        integer = 0
        
        for i in wires:
            integer += i//mid
        
        if integer >= k:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(wirewirewire(k,summ,wires))
