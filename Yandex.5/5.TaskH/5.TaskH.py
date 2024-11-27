maininput = input()
numofsymb, uniqsymb = map(int, maininput.split())
symbols = list(input().strip())  

def substring():
    hashtable = {}
    left = 0
    substringlenght = 0
    start_index = 0  
    
    for i in range(len(symbols)):
        hashtable[symbols[i]] = hashtable.get(symbols[i], 0) + 1
        while hashtable[symbols[i]] > uniqsymb:
            hashtable[symbols[left]] -= 1
            print(hashtable)
            print(hashtable[symbols[left]])
            if hashtable[symbols[left]] == 0:
                del hashtable[symbols[left]]
            left += 1

        if i - left + 1 > substringlenght:
            substringlenght = i - left + 1
            start_index = left  

    print(f'{substringlenght} {start_index + 1}')  

if numofsymb == len(symbols):
    substring()
else:
    print('Error')
