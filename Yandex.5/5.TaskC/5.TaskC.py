
#INPUT moment
peaks = int(input())
y = []
while peaks > len(y):
    peakscoordinates = list(map(int,input().split()))
    y.append(peakscoordinates[1])

peaksplan = int(input())
yourway = []

for _ in range(peaksplan):
    start, end = map(int, input().split())
    if 1 <= start <= peaks and 1 <= end <= peaks:  
        yourway.append((start - 1, end - 1))
    else:
        print('error')
        break

results = []
for start,end in yourway:
    ans = 0
    if start < end:
        for i in range(start,end):
            if y[i] < y[i+1]:
                ans += (y[i+1] - y[i])
    else:
        for i in range(start,end,-1):
            if y[i] < y[i-1]:
                ans += (y[i-1] - y[i])
    results.append(ans)

for item in results:
    print(item)



