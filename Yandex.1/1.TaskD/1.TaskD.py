import math 
a,b,c = int(input()),int(input()),int(input())
z = []
for x in range(-100,100):
    if ((a*x+b)**(1/2) == c):
        z.append(x)
N = len(z)
if N > 100:
    print("MANY SOLUTIONS")
elif N == 0:
    print("NO SOLUTIONS")
else:
    z_sorted = sorted(z,reverse=True)
    for solution in z_sorted:
        print(solution)
