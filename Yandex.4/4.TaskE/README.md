# Pyramide
To build a two-dimensional pyramid, rectangular blocks are used, each of which is 
characterized by its width and height.
You can put one block on top of another only if the width of the top block is 
strictly less than the width of the bottom one (blocks cannot be rotated). The 
bottommost block in the pyramid can be any width.
Given a set of blocks, determine what is the highest pyramid that can be built 
from them.

## Input format
The first line of the input data specifies the number N - number of blocks (1 <= N <= 100 000).
In the next N lines you should write a pairs of Wi and Hi — the width and height of the block, respectively.

## Output format
Print one integer — the maximum height of the pyramid.