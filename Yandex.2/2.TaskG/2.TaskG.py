seq = list(map(int, input().split()))

def findanswer(seq):
    
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in seq:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1 * max2 > min1 * min2:
        return min(max1, max2), max(max1, max2)
    else:
        return min(min1, min2), max(min1, min2)

print(findanswer(seq))

#First solution, its nice but O(logN) because of sorted() function
'''seq = list(map(int, input().split()))

def findanswer(ans):
    newseq = sorted(seq)
    if (newseq[0] * newseq[1]) > (newseq[-1] * newseq[-2]):
        return newseq[1],newseq[0]
    else:
        return newseq[-1],newseq[-2]

print(findanswer(seq))'''