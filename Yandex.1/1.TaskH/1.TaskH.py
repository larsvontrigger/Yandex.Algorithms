a = int(input()) #Pause between trains on first platform
b = int(input()) #Pause between trains on second platform
n = int(input()) #Number of trains that Tanya count on first platform
m = int(input()) #Number of trains that Tanya count on second platform

#Minimum time
T1_1 = n + a * (n - 1)
T1_2 = m + b * (m - 1)

#Maximum time
T2_1 = n + a * (n + 1)
T2_2 = m + b * (m + 1)

#Our valid time period(from max of min and to min of max)
Min = max(T1_1,T1_2)
Max = min(T2_1,T2_2)

#Check if Tanya made mistake
Period = []
if Min >= Max:
    print('-1')
else:
    #Check every minute in time period
    for item in range(Min,(Max+1)):
        if item >= Min and item <= Max:
            Period.append(item)
    print(f'{Period[0]}  {Period[-1]}')
