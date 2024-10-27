# Maxim's triangle
Since childhood, Maxim has been a good musician and a 
jack of all trades. Recently, he made a simple percussion 
musical instrument on his own - a triangle. He needs to 
find out what frequency the sound produced by his 
instrument is.

Maxim has a professional music tuner, with which he can 
play a note with a given frequency. Maxim does the 
following: he turns on notes with different frequencies 
on the tuner and for each note, he determines by ear 
whether it is closer or further from the sound produced 
by the triangle than the previous note. Since Maxim has 
perfect pitch, he always determines this absolutely 
correctly.

Maxim showed you a recording that shows the sequence of 
frequencies he sets on the tuner, and for each note, 
starting with the second, it is written down - closer or 
further from the sound of the triangle than the previous 
note. It is known in advance that the frequency of 
Maxim's triangle is no less than 30 hertz and no more 
than 4000 hertz.

It is required to write a program that determines the 
interval in which the triangle's frequency can be found.

## Input format
The first line of the input file contains an integer n — 
the number of notes that Maxim played using the tuner (2 
≤ n ≤ 1000). The next n lines contain Maxim's notes, with 
each line containing two components: a real number fi — 
the frequency set on the tuner, in hertz (30 ≤ fi ≤ 
4000), and the word "closer" or the word "further" for 
each frequency except the first.

The word "closer" means that the frequency of the given 
note is closer to the triangle's frequency than the 
frequency of the previous note, which is formally 
described by the ratio: |fi − ftriangle| < |fi − 1 − 
ftriangle| .

The word "further" means that the frequency of the given 
note is further than the previous one.

If it turned out that the next note was as close to the 
sound of the triangle as the previous note, then Maxim 
could write down any of the two words specified above.


It is guaranteed that the results obtained by Maxim are 
consistent.



## Output format
The output file must contain two real numbers separated 
by a space — the smallest and largest possible value of 
the sound frequency of the triangle made by Maxim. The 
numbers must be output with an accuracy of no worse than 
10−6