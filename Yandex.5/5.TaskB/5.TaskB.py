maininput = input()
cnt,goalnum = map(int,maininput.split())
carnumbers = list(map(int,input().split()))

def count_subarrays_with_sum(array, K):
    prefix_sum = 0 
    prefix_count = {0: 1}  # Dictionary for numbers of prefixsum 
    count = 0 
    
    for i in array:
        prefix_sum += i  # 
        # Check, if there is a section with sum = K
        if prefix_sum - K in prefix_count:
            count += prefix_count[prefix_sum - K]
            
        # Add or updating a numbers of prefixsum in dict
        if prefix_sum in prefix_count:
            prefix_count[prefix_sum] += 1
        else:
            prefix_count[prefix_sum] = 1
    
    return count


if cnt == len(carnumbers):
    print(count_subarrays_with_sum(carnumbers,goalnum))
else:
    print('error')





