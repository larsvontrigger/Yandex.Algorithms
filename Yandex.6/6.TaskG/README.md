# City square
The city square has dimensions n×m and is covered with square tiles 
measuring 1×1. During a scheduled replacement of the tiles, it turned 
out that the new tiles were not enough to cover the entire area, so it 
was decided to cover only the path along the edge of the square with 
tiles, and to plant a rectangular flowerbed in the center of the square 
(see the figure for example). In this case, the path should have the 
same width on all sides of the square. Determine the maximum width of 
the path that can be laid out from the available tiles.

## Input format
The first and second lines of the input data contain one number n and m 
(3≤ n ≤ 2×109, 3≤ m ≤ 2×109) — the dimensions of the square.

The third line contains the number of available tiles t, 1≤ t< nm.

Note that the value of t may be larger than the possible value of a 
32-bit integer variable, so you must use 64-bit numbers (int64 type in 
Pascal, long long type in C and C++, long type in Java and C#).

## Output format
The program should output a single number — the maximum width of the 
track that can be laid out from the available tiles.