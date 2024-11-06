# Angry Pigs
Have you ever wondered why the birds in Angry Birds don't have wings? The 
developers of the new game asked themselves the same question. In their version, 
the game's meaning is the exact opposite of Angry Birds: a green pig shoots at 
angry birds with a laser gun (the plot is clearly no worse than the original 
game).

Birds in the game are represented by points on a plane. A shot only shoots down 
the closest bird in the line of fire. At the same time, a shot bird, falling, 
shoots down all the birds located directly below it. Two birds cannot be at the 
same point. Given the location of the birds, it is necessary to determine the 
minimum number of shots required to shoot down all the birds.

## Input format
The first line of the input file contains a single integer N (1 ≤ N ≤ 1000) — the 
number of birds.

The next N lines contain two natural numbers each xi, yi — coordinates of the 
i-th bird (0 < x, y ≤ 109). The pig is located at the point with coordinates (0, 
0).

## Output format
The only line of the output file should contain one integer — the minimum number 
of shots needed to shoot down all the birds.