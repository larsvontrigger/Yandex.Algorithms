N = int(input())

notes = []
firstfreq = int(input())
notes.append((firstfreq))

for i in range(N-1):
    #Input note frequnce and str(closer or further)
    x,y = input().split()
    x = int(x)
    notes.append((x,y))  # Add them to the list

def notefinder():
    lowbord = float(30)
    highbord = float(4000)
    diffreq = firstfreq
    for freq in notes[1:]:
        
        if freq[0] > diffreq and 'closer' in freq:
            lowbord = ((freq[0] - diffreq)/2) + diffreq
            diffreq = freq[0]
        elif freq[0] > diffreq and 'further' in freq:
            highbord = ((freq[0] - diffreq)/2) + diffreq
            diffreq = freq[0]


        elif freq[0] < diffreq and 'closer' in freq:
            highbord = ((diffreq - freq[0])/2) + freq[0]
            diffreq = freq[0]
        elif freq[0] < diffreq and 'further' in freq:
            lowbord = ((diffreq - freq[0])/2) + freq[0]
            diffreq = freq[0]
    
    print(lowbord,highbord)
            
notefinder()
