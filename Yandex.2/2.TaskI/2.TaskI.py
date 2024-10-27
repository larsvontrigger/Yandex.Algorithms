
M = int(input())
N = int(input())
K = int(input())

mines = []

# Mines coordinates
for i in range(K):
    x, y = map(int, input().split())  
    mines.append((x, y))  # Add them to the tuple

def saper():
    print('\n')
    # ans is counter of lines
    ans = 1
    for x in range(1,N+1):
        for item in range(1,M+1):
            #checking for mine coordinate
            if (ans,item) in mines:
                print('* ',end = '')
            elif item == (M):
                print(f'{item}\n')
                ans += 1
            else:
                print(f'{item} ',end = '')
saper()
