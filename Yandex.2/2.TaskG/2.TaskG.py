seq = list(map(int, input().split()))

def findanswer(ans):
    newseq = sorted(seq)
    if (newseq[0] * newseq[1]) > (newseq[-1] * newseq[-2]):
        return newseq[0],newseq[1]
    else:
        return newseq[-1],newseq[-2]

print(findanswer(seq))