keys = list(input().split())
ournum = list(input())

def calculator():
    nums = []
    for num in ournum:
        if num not in keys and num not in nums:
            nums.append(num)
    print(len(nums))
calculator()