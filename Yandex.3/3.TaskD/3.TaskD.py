import sys

inputtxt = sys.stdin.read().strip()

def uniquewords():
    words = inputtxt.split()
    uniq = set(words)
    print(len(uniq))

uniquewords()
