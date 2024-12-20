N,K = map(int,input().split())
firstline = list(map(int,input().split()))
secondline = list(map(int,input().split()))

def binarysearch(lst,mass):
    for num in mass:
        l = 0
        r = len(lst) - 1
       
        while r - l > 1:
            m = (l + r) // 2
            guess = lst[m]
            
            if num < guess:
                r = m 
            else:
                l = m 
        if abs(num - lst[l]) <= abs(lst[r] - num):
            print(lst[l])
        else:
            print(lst[r])


if N == len(firstline) and K == len(secondline):
    binarysearch(firstline,secondline)
else:
    print('Enter the right data')