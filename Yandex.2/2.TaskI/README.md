# Minesweeper
You need to build a field for the game "Minesweeper" 
based on its configuration - the sizes and coordinates of 
the mines placed on it.

We will briefly recall the rules for building a field for 
the game "Minesweeper":

The field consists of cells with mines and empty cells
Cells with a mine are designated by the symbol *
Empty cells contain the number ki,j, 0≤ ki, j ≤ 8 - the 
number of mines on adjacent cells. Adjacent cells are 
eight cells that have an adjacent corner or side.

## Input format
The first line contains three numbers: N, 1 ≤ N ≤ 100 - 
the number of rows on the field, M, 1 ≤ M ≤ 100 - the 
number of columns on the field, K, 0 ≤ K ≤ N ⋅ M - the 
number of mines on the field.

The next K lines contain two numbers with the coordinates 
of the mines: p, 1 ≤ p ≤ N is the mine's row number, q, 1 
≤ 1 ≤ M is the mine's column number.

## Output format
Output the constructed field, separating the field's rows 
with a line feed and the columns with a space.