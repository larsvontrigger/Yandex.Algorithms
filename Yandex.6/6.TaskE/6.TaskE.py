import math
two = int(input())
three = int(input())
four = int(input())
  
def averagemark(two,three,four,five):
    markcheck = False
    avgmark = (2 * two + 3 * three + 4 * four + 5 * five)/(two + three + four + five)
    
    if avgmark >= 3.5:
        markcheck = True
    else:
        markcheck = False
    
    return markcheck

def findingfive(two,three,four):
    current_sum = 2 * two + 3 * three + 4 * four
    current_count = two + three + four
    l = 0
    r = math.ceil((3.5 * current_count - current_sum) / 1.5) + 10
    result = 0
    while l <= r:
        five = (l + r)//2
        
        if averagemark(two,three,four,five):
            result = five
            r = five - 1
        else:
            l = five + 1
    return result

print(findingfive(two,three,four))


