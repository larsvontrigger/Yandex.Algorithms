numword,numsym = map(int,input().split())

word = list(input().strip())
symbols = list(input().strip()) 

def mayan():
    ans = 0
    for item in range(len(symbols) - numword):
        
        symbolstest = []
        symbolstest = symbols[item: item + numword]
      
        if set(symbolstest) == set(word):
            ans += 1
        symbolstest.clear()
    print(ans)

if len(word) != numword or len(symbols) != numsym:
    print('Error')
else:
    mayan()


