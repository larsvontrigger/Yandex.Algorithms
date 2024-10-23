seq = list(map(int, input().split()))

def findanswer(seq):
    
    max1 = max2 = max3 =  float('-inf')
    min1 = min2 = min3 = float('inf')

    for num in seq:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        
        elif num > max3:
            max3 = num

        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
       
        elif num < min2:
            min3 = min2
            min2 = num
        
        elif num < min3:
            min3 = num

    if (min2 * min1 * max1) > (max3 * max2 * max1):
        return min1,min2,max1
    else:
        return max1,max2,max3
print(findanswer(seq))