# Running in Manhattan
The roads of New Manhattan are arranged as follows. From south to north, every 
hundred meters there is an avenue, from west to east, every hundred meters there 
is a street. Avenues and streets are numbered with whole numbers. Smaller numbers 
correspond to western avenues and southern streets. Thus, it is possible to 
construct a rectangular coordinate system so that the point (x, y) lies at the 
intersection of the x-th avenue and the y-th street. It is easy to see that in 
order to get from the point (x1, y1) to the point (x2, y2) in New Manhattan, you 
need to walk |x2 − x1| + |y2 − y1| blocks. This value is called the Manhattan 
distance between points (x1, y1) and (x2, y2).

Misha lives in New Manhattan and jogs around the city every morning. He starts 
from his house, which is located at (0, 0), and runs along a random route. Every 
minute, Misha either stays at the same intersection as a minute ago or moves one 
block in any direction. To avoid getting lost, Misha takes a navigator with him, 
which tells Misha where he is every t minutes. Unfortunately, the navigator does 
not show Misha's exact location, it can show any of the points whose Manhattan 
distance to Misha does not exceed d.

After t × n minutes from the start of the run, having received the n-th message 
from the navigator, Misha decided that it was time to run home. To do this, he 
wants to understand at what points he can be. Help Misha do this.

## Input format
The first line of the input file contains the numbers t, d, and n (1 ≤ t ≤ 100, 1 
≤ d ≤ 100, 1 ≤ n ≤ 100).

Then n lines describe the data received from the navigator. Line number i 
contains the numbers xi and yi — the data received from the navigator ti minutes 
after the start of the run.


## Output format
In the first line of the output file, output the number m — the number of points 
where Misha can be. Then output m pairs of numbers — the coordinates of the 
points. The points can be output in any order.

It is guaranteed that the navigator is working properly and that there is at 
least one point where Misha can be.