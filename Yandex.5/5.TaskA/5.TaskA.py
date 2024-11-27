numshirt = int(input())
shirtcolors = list(map(int,input().split()))
if numshirt == len(shirtcolors):
    numpants = int(input())
    pantscolors = list(map(int,input().split()))
else:
    print('Error')

def findthebestcombo():
    i,j = 0,0
    bestshirt = 0
    bestpants = 0
    mindiff = float('inf')
    while i < len(shirtcolors) and j < len(pantscolors):
        diff = abs(shirtcolors[i] - pantscolors[j])
        
        if diff < mindiff:
            mindiff = diff
            bestshirt,bestpants = shirtcolors[i],pantscolors[j]
            
        
        if shirtcolors[i] < pantscolors[j]:
            i += 1
    
        else:
            j += 1
    
    print(bestshirt,bestpants)

findthebestcombo()

