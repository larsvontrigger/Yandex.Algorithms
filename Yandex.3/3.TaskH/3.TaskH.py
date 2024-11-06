numofbird = int(input())
birdscoord = []

#Making a birds coordinates tuple
while len(birdscoord) < numofbird:
    word = list(input().split())
    birdscoord.append(word[0])

#We are interested only in first coordinate, 
#so we just look how many unique numbers of first coordinate exist
def angrybirds():
    pigattack = []
    for item in birdscoord:
        if item not in pigattack:
            pigattack.append(item)
    print(len(pigattack))

angrybirds()
