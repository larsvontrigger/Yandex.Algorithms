word_dict = {}
numberofpairs = int(input())

def synonym():
    for _ in range(numberofpairs):
        key, value = input().split()
        word_dict[key] = value
    yoursynonym = input()
    for key,value in word_dict.items():
        if key == yoursynonym:
            print(value)
            break
        elif value == yoursynonym:
            print(key)
            break
        

synonym()
