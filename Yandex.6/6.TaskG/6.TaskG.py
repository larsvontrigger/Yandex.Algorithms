n = int(input())
m = int(input())
t = int(input())

def square(n, m, cnt):
    if n - 2 * cnt <= 0 or m - 2 * cnt <= 0:
        return n*m
    total_area = n * m
    inner_area = (n - 2 * cnt) * (m - 2 * cnt)
    return total_area - inner_area

def citysquare(n, m, t):
    left, right = 0, min(n, m) // 2
    bestcnt = 0

    while left <= right:
        cnt = (left + right) // 2
        area = square(n, m, cnt)

        if area == t:
            return cnt
        elif area > t:
            right = cnt - 1
        else:
            bestcnt = cnt
            left = cnt + 1

    return bestcnt

print(citysquare(n, m, t))
