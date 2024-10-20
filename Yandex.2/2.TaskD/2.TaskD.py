list = list(map(int,input()))

def neighbors(list):
    ans = 0
    for n in range(1,len(list) - 1):
        if list[n-1] < list[n] and list[n] > list[n+1]:
            ans += 1
    print(ans)
neighbors(list)

