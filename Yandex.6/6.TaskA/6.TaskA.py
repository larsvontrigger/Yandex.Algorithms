N,K = map(int,input().split())
firstline = list(map(int,input().split()))
secondline = list(map(int,input().split()))

def binarysearch(lst,mass):
    lst = sorted(lst)

    for num in mass:
        l = 0
        r = len(lst) - 1
        result = False
        while l <= r:
            m = (l + r) // 2
            guess = lst[m]
            if guess == num:
                result = True
                break
            if num < guess:
                r = m - 1
            else:
                l = m + 1
        if result:
            print('YES')
        else:
            print('NO')

if N == len(firstline) and K == len(secondline):
    binarysearch(firstline,secondline,)
else:
    print('Enter the right data')

