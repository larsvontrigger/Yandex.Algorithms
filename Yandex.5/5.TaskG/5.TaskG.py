maininput = input()
numcards,k = map(int,maininput.split())
cards = list(map(int,input().split()))

def numbers():
    cards.sort()
    cnt = 0
    trionum = {}
    for i in range(len(cards) - 2):
       
        if (cards[i] * k) >= cards[i+2]:
            a,b,c = cards[i:i+3]
            
            #Making a hash table to avoid re-calculating the same combinations
            if (a,b,c) in trionum.keys():
                pass
            else:
                trionum[(a,b,c)] = 1
                
                if a == b == c:  
                    cnt += 1
                elif a == b or b == c or a == c:  
                    cnt += 3
                else:  
                    cnt += 6

if numcards == len(cards):
    numbers()
else:
    print('Error')
