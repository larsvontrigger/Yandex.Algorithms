nums = list(input())
sortednums = []

def numbers():
    for num in nums:
        if num not in sortednums:
            sortednums.append(num)
    print(len(sortednums))

numbers()


