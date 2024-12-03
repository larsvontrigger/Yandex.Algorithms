maininput = input()
numofmonuments,distance = map(int,maininput.split())

def date(data):
    cnt = 0
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            diff = abs(data[j] - data[i])
            if diff > distance:
                cnt += 1
    print(cnt)

monuments = list(map(int,input().split()))
if len(monuments) != numofmonuments:
    print('error')
else:
    date(monuments)
    

