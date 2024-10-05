a = int(input())
b = int(input())
c = int(input())
rectangle = [a,b,c]
if a <= 0 or b <=0 or c <= 0:
    print("Invalid data")
else:
    if (a + b > c) and (b + c > a) and (a + c > b):
        print("YES")
    else:
        print("NO")
    