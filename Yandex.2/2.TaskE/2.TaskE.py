numofcompet = int(input())
competplace = list(map(int,input().split()))

def findfifth(ctp):
    for n in range(0,len(ctp) - 1):
        #Check for elements with 5s, and next element in list
        if str(ctp[n]).endswith('5') and ctp[n+1] < ctp[n]:
            for i in range(0,n):
                #Check list of numbers from 0 to n, and find if theres at least one number bigger then [n]
                if ctp[i] > ctp[n]:
                    print(f'Vasya on {n+1} place')
                else:
                    print('Thats wrong')
                    break
        else:
            print('Thats wrong')
            break

findfifth(competplace)
            
            


