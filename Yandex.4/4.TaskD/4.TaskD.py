#input keys
keys = int(input())
values = [0]
while len(values) < keys + 1:
    num = int(input())
    values.append(num)

#input clicks
numclicks = int(input())
clicks = []
while len(clicks) < numclicks:
    clicks.append(int(input()))

keyboardlive = dict()
def keyboard():
    for item in range(keys+1):
        keyboardlive[item] = values[item]
    
    for click in clicks:
        if click <= keys:
            keyboardlive[click] -= 1
    
    for i in range(1, keys + 1):
        if keyboardlive[i] < 0:
            print("YES")  
        else:
            print("NO") 

keyboard()
