numofturtles = int(input())
turtleword = []

#Making a turtleword tuple
while len(turtleword) < numofturtles:
    word = list(map(int,input().split()))
    turtleword.append(word)

#Turtle is not lying only when sum of turtle == (numofturtles - 1)
def turtlewords():
    ans = 0
    for item in turtleword:
        sum = item[0] + item[1]
        if sum == (numofturtles - 1):
            ans += 1
    print(ans)


turtlewords()