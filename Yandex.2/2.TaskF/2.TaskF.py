n = int(input())  
seq = list(map(int, input())) 

def is_palindrome(seq):
    return seq == seq[::-1]

def min_add_to_make_palindrome(seq):
    n = len(seq)
    for i in range(n):
        #If str from i is palindrome
        if is_palindrome(seq[i:]):
            return seq[:i][::-1]
    return []

to_add = min_add_to_make_palindrome(seq)

if to_add:
    print("".join(map(str, to_add)))