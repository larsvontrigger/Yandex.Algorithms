firstnums = list(input())
secondnums = list(input())

def intersection():
    return set(firstnums) & set(secondnums)

print(intersection())