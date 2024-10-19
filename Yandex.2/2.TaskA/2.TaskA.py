list = list(input())
def monotone(x):
    firstsymbol = list[0]
    #Making ans counter to check if we have 2 or more same element in a row
    ans = 0
    #Starting from 1 element, because firstsymbol is our first element
    for item in list[1:]:
        if item > firstsymbol:
            firstsymbol = item
        elif item <= firstsymbol:
            ans += 1
    if firstsymbol == list[-1] and ans == 0:
        print('YES')
    else:
        print('NO')

monotone(list)