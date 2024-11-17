text = str(input()).split()
counter = dict()

def lookingforword():
    for word in text:
        counter[word] = counter.get(word,0) + 1
    maxword = max(counter.values())

    for key,values in counter.items():
        if values == maxword:
            print(key)
   
    
lookingforword()