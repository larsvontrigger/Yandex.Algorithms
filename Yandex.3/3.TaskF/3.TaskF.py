firstgen = list(input())
secondgen = list(input())
firstgenpairs = []
secondgenpair = []

def paircompare():
    #Pair counter
    ans = 0
    #Making a pairs list of first and second genes
    for z in range(0,len(firstgen)-1):
        firstgenpairs.append(firstgen[z]+firstgen[z+1])
    
    for t in range(0,len(secondgen)-1):
        secondgenpair.append(secondgen[t]+secondgen[t+1])
    #Looking for similar pairs of genes
    for item in firstgenpairs:
        if item in secondgenpair:
            ans += 1
    print(ans)

paircompare()