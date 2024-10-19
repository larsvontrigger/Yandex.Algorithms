# Initialize an empty list to store the sequence
sequence = []
# The number indicating the end of input
end_signal = -2 * 10**3
while True:  # Start an infinite loop
    num = int(input())  # Read a number from input and convert it to an integer
    if num == end_signal:  # Check if the number is the end signal
        break  # Exit the loop if it is
    sequence.append(num)  # If not the end signal, add the number to the sequence
def seqanalyzer(sequence):
    firstsymbol = sequence[0]
    #Making a counter for every type of progression
    ran = 1
    eq = 1
    asc = 1
    for item in sequence[1:]:
        if item > firstsymbol:
            asc += 1
            firstsymbol = item
        elif item < firstsymbol:
            ran += 1
            firstsymbol = item
        elif item == firstsymbol:
            eq += 1 
    if asc == len(sequence) and  ran == 1 and eq == 1:
        print('ASCENDING')
    elif asc > 1 and eq > 1 and ran == 1:
        print('WEAKLY ASCENDING')
    elif ran == len(sequence) and asc == 1 and eq == 1:
        print('DESCENDING')
    elif ran > 1 and eq > 1 and asc == 1:
        print('WEAKLY DESCENDING')
    elif eq == len(sequence) and ran == 1 and asc == 1:
        print('CONSTANT')
    else:
        print('RANDOM')
        
seqanalyzer(sequence)

