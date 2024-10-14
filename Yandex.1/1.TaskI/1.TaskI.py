#A,B,C is sides of the brick. D and E are sides of the hole
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

# First of all we will calculate all areas
main = D * E

first = A * B
second = A * C
thirst = C * B

#And then we will make a function that will check if our brick can fit into this hole
def brick_in_the_wall():
    if main >= first:
        if max(D,E) >= max(A,B):
            print('YES')
        else:
            print('NO')
    elif main <= first:
        if main >= second:
            if max(D,E) >= max(A,C):
                print('YES')
            else:
                print('NO')
        elif main <= second:
            if main >= thirst:
                if max(D,E) >= max(C,B):
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
brick_in_the_wall()