import math
w,h,n = map(int,input().split())
square = w * h
nums = [i**2 for i in range(int(math.sqrt(square)),int(math.sqrt(square * n * 2)))]

def sqr(massive):
    for num in massive:
        if num >= (square * n):
            left = math.sqrt(num) // w
            up = math.sqrt(num) // h
            if left * up >= n:
                goalside = int(math.sqrt(num))
                print(goalside)
                break  

sqr(nums)


