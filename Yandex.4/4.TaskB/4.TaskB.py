import sys
inputtxt = sys.stdin.read().strip()

def dictwords():
    dictwords = [inputtxt.split()]
    countwords = []
    for word in dictwords:
        if word in dictwords:
            countwords[word] += 1
    print(countwords)
dictwords()