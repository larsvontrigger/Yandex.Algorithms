papers, x, y = map(int, input().split())

def goaltime(N, x, y):

    faster, slower = min(x, y), max(x, y)

    low, high = 0, N * slower

    while low < high:
        mid = (low + high) // 2
        
        copies = mid // faster + mid // slower

        if copies >= N - 1:
            high = mid
        else:
            low = mid + 1

    return low + faster

print(goaltime(papers, x, y))
