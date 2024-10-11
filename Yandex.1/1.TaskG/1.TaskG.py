N = int(input())
K = int(input())
M = int(input())
#Number of parts produced
parts = 0
#In case when some idiot wants to laugh and enter three zeros (Then we’ll laugh together)
if N != 0 and K != 0 and M != 0:
    #Remaining when producing one batch of parts from one workpiece
    remainder = K%M
    #We count the number of parts produced from each workpiece and subtract all the necessary costs from the alloy (not forgetting to return the remainder)
    while N >= K:
        parts += K//M
        N -= K - remainder
    #Here's the result, gentlemens
    print(f'У нас вышло {parts} детали/ей')  
    print(f'А от сплава осталось {N} кг, милорд!')
else:
    print('Милорд, тут какой-то окаянный привез 0кг железа...')
